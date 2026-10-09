"""
Scoring Logic & Calculations.

Responsibility:
- Maintain non-decreasing player score throughout the game session.
- Award points according to config rules:
  * Eating regular pacgum (+X points).
  * Eating super-pacgum / power pellet (+Y points).
  * Eating an edible ghost (+Z points).
- Prevent score decrements under any circumstance.
- Provide clean score queries for HUD and Highscore screens.

Assigned Developer:
- P1
"""
