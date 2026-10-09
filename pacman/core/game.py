"""
Main Game Controller & State Machine.

Responsibility:
- Maintain current game state (e.g., MAIN_MENU, PLAYING, PAUSED, GAME_OVER, VICTORY).
- Coordinate the primary game loop:
  * Event handling (keyboard input WASD / Arrow keys, pause toggle, cheat activations).
  * State updates (player move, ghost AI tick, collision detection, timers).
  * Frame rendering coordination with UI module.
- Manage transition when player loses a life, respawning at maze center.
- Handle end-of-game conditions (all levels won or all lives lost).

Assigned Developer:
- P1 (with UI integration support from P2)
"""
