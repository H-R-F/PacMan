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
        (21, 21),
        (23, 21),
        (25, 21),
        (25, 23),
        (27, 23),
        (27, 25),
        (29, 25),
        (29, 27),
        (31, 27),
        (31, 29),
    ],
}


LIMITS = {
    "lives": (1, 9),
    "pacgum": (0, 10000),
    "level_max_time": (10, 999),

    "width": (5, 45),
    "height": (5, 35),

    "points_per_pacgum": (0, 10000),
    "points_per_super_pacgum": (0, 10000),
    "points_per_ghost": (0, 10000),

    "seed": (0, 4294967295),

    "levels": (10, 10),
}

# FUNCTION read_text(path) -> text or NOTHING
#     TRY open(path, encoding="utf-8") and read everything
#     ON FileNotFoundError        -> warn("config file not found"); RETURN NOTHING
#     ON OSError (permissions...) -> warn(reason);                  RETURN NOTHING
#     ON UnicodeDecodeError       -> warn("file is not valid UTF-8"); RETURN NOTHING
#     RETURN text

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
    for line in text.split():
        if line[0] == "#" or line[0] == "//":
            line.replace()
    return "".join(line)

# FUNCTION blank_comments(text) -> text
#     FOR EACH line IN text.splitlines(keep line endings)
#         IF first non-space character of line is "#"   (or starts with "//")
#             REPLACE the line's content with the same number of spaces, KEEP the newline
#         ELSE keep line unchanged
#     RETURN lines joined with ""

# FUNCTION parse(text) -> dict or NOTHING
#     TRY json.loads(text)
#     ON JSONDecodeError e -> warn("invalid JSON at line {e.lineno}, column {e.colno}: {e.msg}")
#                             RETURN NOTHING
#     IF result is not a dict -> warn("top level must be an object { }"); RETURN NOTHING
#     RETURN result

# FUNCTION read_setting(raw, key, expected type, (min, max), default) -> value
#     IF key missing                       -> RETURN default  (quietly or with an info message)
#     IF type is wrong (bool counts as wrong for int!) -> warn(key, value, "using default"); RETURN default
#     IF value < min                       -> warn(key, value, "clamped to min"); RETURN min
#     IF value > max                       -> warn(key, value, "clamped to max"); RETURN max
#     RETURN value

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