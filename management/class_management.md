# Class Management (Upgraded)

## 1) Goal

This document defines a **clean class and package architecture** for the PacMan project.

---

## 2) Layered Architecture

```text
pac-man.py (entry point / wiring)
    └── pacman/
        ├── core/        -> game state machine, progression, scoring, cheats
        ├── entities/    -> player, ghosts, pellets
        ├── maze/        -> grid model + external maze adapter
        ├── config/      -> config loading/validation
        ├── highscore/   -> leaderboard persistence
        └── ui/          -> rendering, menus, screens, assets (pygame side)
```

### Dependency rules (must stay true)

- `ui` can import `core`, `entities`, `maze`, `config`, `highscore`.
- `core` can import `entities`, `maze`, `config`, `highscore`.
- `entities` can import `maze`, `config`, `core.constants`.
- `maze` can import `core.constants` and external adapter dependency.
- `config` and `highscore` should remain low-dependency utility layers.
- Non-UI logic (`core`, `entities`, `maze`) must not depend on pygame.

---

## 3) Package & Class Catalogue

## 3.1 `pacman/config/loader.py` (P2)

**Responsibility:** Parse and validate runtime configuration safely.

Classes:
- `GameConfig`: validated configuration object for gameplay settings.
- `LevelConfig`: validated per-level dimensions/settings.
- `ConfigLoader`: robust parser/validator with safe defaults and warning messages.

Contract highlights:
- Accept JSON with controlled comment support.
- Validate types/ranges.
- Clamp invalid values.
- Never expose raw traceback to end user on bad config input.

---

## 3.2 `pacman/highscore/manager.py` (P2)

**Responsibility:** Top-10 persistence and validation.

Classes:
- `HighScoreEntry`: one leaderboard record (`name`, `score`).
- `HighscoreManager`: load/save/sort/filter leaderboard records.

Contract highlights:
- Keep list sorted descending by score.
- Enforce safe player-name policy (length + allowed chars).
- Recover gracefully from missing/corrupted score file.

---

## 3.3 `pacman/maze/grid.py` and `pacman/maze/adapter.py` (P1)

**Responsibility:** Maze data model and external generator integration.

Classes:
- `Grid` (`grid.py`): 2D maze representation and movement/collision queries.
- `MazeAdapter` (`adapter.py`): adapter to external A-Maze-ing generator output.
- `EntityPlacer` (recommended, can be in `grid.py` or `adapter.py`): spawn and pellet placement policy.

Contract highlights:
- Provide walkability queries (`is_walkable`, bounds checks).
- Expose canonical center/corners/corridor cells for placements.
- Adapter must isolate all external generator quirks/failures.

---

## 3.4 `pacman/entities/` (P1)

**Responsibility:** All movable actors and collectible gameplay entities.

Classes:
- `Entity` (`entity.py`): abstract base with position/direction/update contract.
- `Player` (`player.py`): input buffering, movement, life/respawn state.
- `Ghost` (`ghost.py`): chase/frightened/eaten behavior and movement policy.
- `Pellet` + `SuperPellet` (`pellet.py`): collectible score/power entities.

Contract highlights:
- Movement always constrained by grid walkability.
- Player supports buffered turn intent for smooth cornering.
- Ghost mode/state transitions remain explicit and testable.

---

## 3.5 `pacman/core/` (P1)

**Responsibility:** Gameplay orchestration and state machine.

Classes:
- `Game` (`game.py`): main logic tick, transitions, orchestration.
- `FrameData` (`game.py`): read-only DTO from core to UI.
- `LevelManager` (`level.py`): level progression, timers, level construction.
- `Scorer` (`scoring.py`): monotonic scoring logic.
- `CheatController` (`cheats.py`): isolated cheat toggles/actions.

Contract highlights:
- `Game` is the single owner of mutable gameplay state.
- UI should render from `FrameData`, not mutate core objects directly.
- Scoring and level transitions must be deterministic and test-covered.

---

## 3.6 `pacman/ui/` (P2)

**Responsibility:** Presentation and user interaction.

Classes:
- `AssetManager` (`assets.py`): asset loading and resource-path handling.
- `Renderer` (`renderer.py`): frame drawing from `FrameData`.
- `MainMenu` / `PauseMenu` (`menu.py`): menu flows and actions.
- `EndScreen` (`screens.py`): game-over/victory flow and name entry.
- `InputMapper` (if implemented): maps library events to game actions.

Contract highlights:
- UI reads game state; it does not own gameplay rules.
- Resource path strategy must work in both development and packaging contexts.

---

## 3.7 Entry Point `pac-man.py` (Pair)

**Responsibility:** Bootstrap and wire all subsystems.

Flow:
1. Validate CLI inputs.
2. Load config.
3. Build services (highscore, game, renderer).
4. Run loop: input -> `Game.tick(...)` -> `Renderer.draw(...)`.

---

## 4) Shared Enums & Constants

`pacman/core/constants.py` should centralize shared enums/constants used across layers (e.g., directions, game states, ghost modes, cell types) to avoid duplication and drift.

---

## 5) Implementation Rules (Upgraded)

1. Keep interfaces explicit with type hints and docstrings.
2. Keep modules single-responsibility; avoid utility dumping grounds.
3. Avoid circular imports by pushing shared contracts to stable low-level modules.
4. Keep external dependency handling confined to adapter boundaries.
5. Keep failures user-friendly: warnings/recovery for config/highscore/adapter issues.
6. Add/maintain tests when changing class contracts.

---

## 6) Ownership Summary

- **P1**: `maze`, `entities`, `core`
- **P2**: `config`, `highscore`, `ui`
- **Pair**: root wiring, shared constants/enums, integration decisions

---

