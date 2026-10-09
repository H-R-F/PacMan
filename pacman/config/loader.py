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
