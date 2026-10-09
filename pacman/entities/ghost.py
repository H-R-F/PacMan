"""
Ghost Entity & Autonomous AI Logic.

Responsibility:
- Implement 4 individual ghosts with distinct starting corners and personalities.
- Manage Ghost behavioral states:
  * CHASE: Autonomously navigate corridors targeting the player (BFS, distance, heuristic).
  * FRIGHTENED / EDIBLE: Run away from player when super-pacgum is consumed, flash color, slower speed.
  * EATEN: Return / respawn to assigned starting corner after a cooldown (5 to 10 seconds).
- Ensure ghosts strictly move along corridors and do not get stuck or cluster indefinitely.

Assigned Developer:
- P1
"""
