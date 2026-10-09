"""
External A-Maze-ing Package Adapter.

Responsibility:
- Integrate the external third-party 'A-Maze-ing' package without modifying its code.
- Enforce the required generator parameter: PERFECT = False (to produce looping corridors).
- Translate external maze structure (graph, matrix, or custom objects) into internal Grid format.
- Provide clean fallback / error recovery if external generator fails or crashes.

Assigned Developer:
- P1
"""
