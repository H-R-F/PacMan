"""
Player (Pac-Man) Entity Class.

Responsibility:
- Handle Pac-Man mechanics:
  * Restrict movement strictly to corridors (prevent walking through walls).
  * Respond to user input (Arrow keys or WASD) with pre-turn direction buffering.
  * Maintain remaining lives (starting at configured count, typically 3).
  * Manage life loss and center-of-maze respawn upon touching a non-edible ghost.
  * Animate mouth chomp cycle based on current movement state and direction.

Assigned Developer:
- P1
"""
