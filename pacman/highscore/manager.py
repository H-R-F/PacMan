"""
Persistent Highscore Storage & Leaderboard Manager.

Responsibility:
- Load highscores from JSON file on disk at startup and save upon game completion.
- Maintain and sort Top 10 scores in descending order.
- Validate player names (strictly max 10 characters, alphanumeric and spaces only).
- Validate scores (strictly non-negative integers).
- Ensure total robustness against missing, corrupted, or permission-restricted files.

Assigned Developer:
- P2
"""
