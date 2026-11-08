# """
# Configuration File Parser & Validator.

# Responsibility:
# - Read JSON configuration files supporting line comments (e.g., lines starting with '#')
#   and optional C-style comments ('//').
# - Validate required game parameters:
#   * lives, pacgum count, points_per_pacgum, points_per_super_pacgum, points_per_ghost.
#   * level array with width & height for each level.
#   * seed, level_max_time, and highscore_filename.
# - Implement robust fault-tolerant handling:
#   * On missing or invalid values, log a clean informative message and clamp to safe defaults.
#   * Silently ignore unknown keys.
#   * Never raise unhandled exceptions or show tracebacks to the user.

# Assigned Developer:
# - P2
# """
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


def warn(message):
    print(f"[CONFIG] Warning: {message}")


def read_text(path):
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


def read_levels(raw):
    
# FUNCTION read_levels(raw_list) -> list of (width, height)
#     IF raw_list missing or not a list    -> warn; RETURN default levels
#     levels = empty list
#     FOR EACH (index, entry) IN raw_list
#         IF entry is not a dict -> warn("level {index+1} is not an object, using default"); use default entry
#         width  = read_setting(entry, "width",  int, WIDTH_LIMITS,  default for that level)
#         height = read_setting(entry, "height", int, HEIGHT_LIMITS, default for that level)
#         append (width, height)
#     IF len(levels) < 10 -> warn; pad with default levels up to 10
#     RETURN levels

# FUNCTION load_config(path) -> Config          # the only function the game calls; NEVER raises
#     config = copy of DEFAULTS
#     text = read_text(path)
#     IF text is NOTHING                    -> RETURN defaults
#     raw = parse(blank_comments(text))
#     IF raw is NOTHING                     -> RETURN defaults
#     FOR EACH simple key (lives, pacgum, seed, points..., level_max_time)
#         config[key] = read_setting(raw, key, int, LIMITS[key], DEFAULTS[key])
#     config.highscore_filename = read_filename(raw)    # str, not empty, no folder parts ("/" or "..")
#     config.levels = read_levels(raw.get("levels"))
#     FOR EACH key in raw that is not known -> ignore (maybe a debug log)
#     RETURN config