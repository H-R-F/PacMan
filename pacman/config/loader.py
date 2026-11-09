"""
Configuration File Parser & Validator.

Responsibility:
- Read JSON configuration files supporting line comments (e.g., lines starting with '#')
  and optional C-style comments ('//').
- Validate required game parameters:
  * lives, pacgum count, points_per_pacgum, points_per_super_pacgum, points_per_ghost.
  * level array with width & height for each level.
  * seed, level_max_time, and highscore_filename.
- Implement robust fault-tolerant handling:
  * On missing or invalid values, log a clean informative message and clamp to safe defaults.
  * Silently ignore unknown keys.
  * Never raise unhandled exceptions or show tracebacks to the user.

Assigned Developer:
- P2
"""

import json
import os
from typing import Any

DEFAULTS = {
    "lives": 3,
    "pacgum": 0,

    "points_per_pacgum": 10,
    "points_per_super_pacgum": 50,
    "points_per_ghost": 200,

    "seed": 42,
    "level_max_time": 90,

    "highscore_filename": "highscores.txt",

    # (width, height) for each level
    "levels": [
        (15, 11),
        (17, 13),
        (19, 15),
        (21, 15),
        (23, 17),
        (25, 19),
        (27, 21),
        (29, 21),
        (31, 23),
        (33, 25)
    ],
}

LIMITS = {
    "lives": (1, 9),
    "pacgum": (0, 10000),
    "level_max_time": (10, 999),

	"points_per_pacgum": (1, 100),
	"points_per_super_pacgum": (1, 1000),
	"points_per_ghost": (1, 1000),

    "seed": (0, 4294967295),

    "width": (5, 45),
    "height": (5, 35),
    "levels": (1, 10),
}

NUMERIC_KEYS = ("lives", "pacgum", "level_max_time", "points_per_pacgum",
                "points_per_super_pacgum", "points_per_ghost", "seed")


def warn(message):
    """Print a non-fatal configuration warning to the user."""
    print(f"[CONFIG] Warning: {message}")


def read_text(path):
    """Read the config file as UTF-8 text; return None (with a warning) on failure."""
    try:
        with open(path, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        warn("Config file not found.")
    except OSError as error:
        warn(f"Could not read config file: {error}")
    except UnicodeDecodeError:
        warn("Config file is not valid UTF-8.")
    return None


def blank_comments(text):
    """Replace full-line '#' and '//' comments with spaces.

    Line and column numbers stay the same, so JSON error messages
    still point to the right place in the original file.
    """
    lines = []
    for line in text.splitlines(keepends=True):
        content = line.rstrip("\r\n")
        newline = line[len(content):]
        if content.lstrip().startswith("#") or content.lstrip().startswith("//"):
            lines.append(" " * len(content) + newline)
        else:
            lines.append(line)
    return "".join(lines)


def parse(text):
    """Parse JSON text and return it as a dict, or None if it is invalid."""
    try:
        result = json.loads(text)
    except json.JSONDecodeError as e:
        warn(f"Invalid JSON at line {e.lineno}, column {e.colno}: {e.msg}")
        return None
    if not isinstance(result, dict):
        warn("Top level must be an object { }.")
        return None
    return result


def read_setting(raw: dict[str, Any], key: str, expected_type: type, low: int, high: int, default: int) -> int:
    """Return raw[key] validated as an integer clamped to [low, high].

    Missing keys give the default; wrong types (including bools) give the
    default with a warning; out-of-range values are clamped with a warning.
    """
    if key not in raw:
        return default
    value = raw[key]
    if isinstance(value, bool) or not isinstance(value, expected_type):
        warn(f"{key} = {value!r} is not a valid {expected_type.__name__}; "
             f"using default {default}")
        return default
    if value < low:
        warn(f"{key} = {value} is below the minimum {low}; using {low}")
        return low
    if value > high:
        warn(f"{key} = {value} is above the maximum {high}; using {high}")
        return high
    return value


from typing import Any


def read_levels(raw_list: Any) -> list[tuple[int, int]]:
    """Validate the 'levels' list and return (width, height) for each level.

    Invalid entries fall back to that level's default size, extra levels
    are dropped, and missing levels are filled in from the defaults.
    """
    defaults = DEFAULTS["levels"]
    min_levels, max_levels = LIMITS["levels"]
    w_low, w_high = LIMITS["width"]
    h_low, h_high = LIMITS["height"]

    if not isinstance(raw_list, list) or not raw_list:
        warn("'levels' is missing or is not a non-empty list; "
             "using the default levels")
        return list(defaults)

    if len(raw_list) > max_levels:
        warn(f"{len(raw_list)} levels given; using only the first {max_levels}")
        raw_list = raw_list[:max_levels]

    levels = []
    for index, entry in enumerate(raw_list):
        default_w, default_h = defaults[min(index, len(defaults) - 1)]
        if not isinstance(entry, dict):
            warn(f"level {index + 1} is not an object; using its default size")
            levels.append((default_w, default_h))
            continue
        width = read_setting(entry, "width", int, w_low, w_high, default_w)
        height = read_setting(entry, "height", int, h_low, h_high, default_h)
        levels.append((width, height))

    if len(levels) < min_levels:
        warn(f"only {len(levels)} levels given, at least {min_levels} are "
             "needed; adding default levels")
        while len(levels) < min_levels:
            levels.append(defaults[min(len(levels), len(defaults) - 1)])
    return levels


def read_filename(raw: dict[str, Any], key: str, default: str) -> str:
    """Return a safe file name (no folders, no control characters)."""
    if key not in raw:
        return default
    value = raw[key]
    if not isinstance(value, str) or not value.strip():
        warn(f"{key} = {value!r} is not a valid file name; "
             f"using default {default!r}")
        return default
    if (any(sep in value for sep in "/\\") or value in (".", "..")
            or any(ord(char) < 32 for char in value) or len(value) > 100):
        warn(f"{key} = {value!r} must be a plain file name (no folders); "
             f"using default {default!r}")
        return default
    return value


def load_config(path: str) -> dict[str, Any]:
    """Load the config file; always return a complete, valid dictionary."""
    config: dict[str, Any] = dict(DEFAULTS)
    config["levels"] = list(DEFAULTS["levels"])

    text = read_text(path)
    if text is None:
        return config
    raw = parse(blank_comments(text))
    if raw is None:
        return config

    for key in NUMERIC_KEYS:
        low, high = LIMITS[key]
        config[key] = read_setting(raw, key, int, low, high, DEFAULTS[key])
    config["highscore_filename"] = read_filename(
        raw, "highscore_filename", DEFAULTS["highscore_filename"])
    config["levels"] = read_levels(raw.get("levels"))

    for key in raw:
        if key not in DEFAULTS:
            warn(f"Unknown key {key!r} ignored")
    return config
