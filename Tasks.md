# Plan dyal l-Khidma (ToDo List) & Gestion d les Risques - Projet PacMan

> Had l-document kay-qsem l-khdma bin **Person 1 (P1)** w **Person 2 (P2)** b tariqa m-tewzna, m3a ga3 les pieges, les problemes li i-qdro i-wqe3o, w l-holol dyalhom.

---

## 1. Taqsim d l-Adwar (Role Distribution)

| Person | Domaine l-Mass'oul 3lih (Primary Responsibilities) |
|---|---|
| **P1: Engine, Gameplay & Maze** | - Game Engine & Loop Logic<br>- Player (Pac-Man) movement, collision & lives<br>- Ghosts AI (Scatter, Chase, Frightened/Edible, Respawn)<br>- A-Maze-ing Adapter & Maze generation<br>- Cheat mode triggers & mechanics |
| **P2: UI, Config, Highscore & Packaging** | - Config loader (JSON + comments parser + fallback defaults)<br>- Highscore manager (persistence, validation, top 10)<br>- GUI rendering (Menus, HUD, Screens, Fonts, Sprites)<br>- Packaging (PyInstaller, build script, Itch.io release)<br>- Project Management documents & Makefile |
| **P1 + P2 (Shared)** | - Architecture design & Code review<br>- Mypy & Flake8 compliance<br>- Integration testing & Mock Defense / Recode drill |

---

## 2. ToDo List b les Phases (Milestones)

### Phase 1: Setup, Architecture & Rules Setup
- [ ] **P1 & P2**: Mtafqo 3la l-architecture d les classes w packages (`pacman/engine`, `pacman/ui`, etc.).
- [ ] **P2**: Cree l-`Makefile` kamel m3a ga3 les targets (`install`, `run`, `debug`, `clean`, `lint`, `lint-strict`).
- [ ] **P2**: Cree l-`.flake8` w configure `mypy.ini` aw `pyproject.toml` bach kolchi ikoun strict mn n-nhar l-lowel.
- [ ] **P2**: Cree l-`.gitignore` (bach t-mne3 cache files, build folders, virtualenvs).
- [ ] **P1**: Cree skeleton d les fichiers m3a type hints w docstrings (PEP 257 format).

---

### Phase 2: Configuration & Highscore (P2 Lead)
- [ ] **P2 - Task 2.1**: Implementer JSON-with-comments parser (ignorer les lignes `#` w support d C-style comments `//`).
- [ ] **P2 - Task 2.2**: Valider les cles d config (`lives`, `pacgum`, `points_per_*`, `level_max_time`, `levels`, `seed`).
- [ ] **P2 - Task 2.3**: Implementer fallback defaults & clamping (ila kan nombre negatif aw valeur manquante).
- [ ] **P2 - Task 2.4**: Implementer highscore manager (read/write JSON, check max 10 chars name alphanumeric, positive score, top 10 sort).
- [ ] **P2 - Task 2.5**: Unit tests l config parser w highscore manager b pytest.

---

### Phase 3: Maze Adapter & Grid Representation (P1 Lead)
- [ ] **P1 - Task 3.1**: T-le3bo b package `A-Maze-ing` w tfhmo l-interface dyalo bla ma t-beddlo fih walo.
- [ ] **P1 - Task 3.2**: Cree `MazeAdapter` li kay-akhod output dyal `A-Maze-ing` (m3a `PERFECT=False`) w kay-convertih l 2D grid matrix.
- [ ] **P1 - Task 3.3**: Placement d Pacgums f les corridors.
- [ ] **P1 - Task 3.4**: Placement d 4 Super-pacgums f les 4 corners d l-grid.
- [ ] **P1 - Task 3.5**: Placement d Pacman f l-center w les 4 ghosts f les 4 coins.
- [ ] **P1 - Task 3.6**: Gestion d fixed seed l Level 1 (ex: seed=42) w random seeds l les 9+ levels li jayin.

---

### Phase 4: Gameplay Core & Entities (P1 Lead)
- [ ] **P1 - Task 4.1**: Movement d Pac-Man (Grid-based aw smooth tile movement) bla ma i-dkhol f les murs.
- [ ] **P1 - Task 4.2**: Scoring logic (eating pacgum -> +X, super-pacgum -> +Y).
- [ ] **P1 - Task 4.3**: Ghost AI 1: Normal mode (chase player b distance/BFS aw basic pathfinding).
- [ ] **P1 - Task 4.4**: Ghost AI 2: Frightened mode melli Pacman i-akol super-pacgum (slow down + herba mn player + color change).
- [ ] **P1 - Task 4.5**: Ghost AI 3: Eaten mode (respawn f corner dyalo apres 5-10s + score +Z).
- [ ] **P1 - Task 4.6**: Player death logic (toucher ghost non-edible -> naqis 1 life -> respawn center).
- [ ] **P1 - Task 4.7**: Cheat Mode mechanics:
  - Invincibility (toggle)
  - Level skip (instant win current level)
  - Ghost freeze (toggle)
  - Extra lives (+1 life)
  - Speed boost

---

### Phase 5: GUI, Graphics & Audio/Effects (P2 Lead)
- [ ] **P2 - Task 5.1**: Main Window setup b Pygame (aw graphical library li khtarto).
- [ ] **P2 - Task 5.2**: Render Maze grid, walls, corridors, pacgums, w super-pacgums.
- [ ] **P2 - Task 5.3**: Render animated sprites (Pac-Man chomp, 4 distinct ghosts colors, frightened blue ghost).
- [ ] **P2 - Task 5.4**: Render HUD dima f l-gameplay (Score, Lives icons, Level number, Remaining time countdown).
- [ ] **P2 - Task 5.5**: Render Main Menu (Start, Highscores list, Instructions, Exit).
- [ ] **P2 - Task 5.6**: Render Pause Menu (Resume, Quit to menu).
- [ ] **P2 - Task 5.7**: Render Game Over & Victory screens m3a text input field bach l-la3ib i-kteb smito l-highscore.

---

### Phase 6: Game Flow & Progression (P1 & P2 Pair)
- [ ] **P1 & P2 - Task 6.1**: Level completion check (ga3 pacgums t-klo -> transition l level maji).
- [ ] **P1 & P2 - Task 6.2**: Multi-level progression (10 levels minimum, score w lives kay-douzo m3ak).
- [ ] **P1 & P2 - Task 6.3**: Level timer expiration handling (ex: lose life ila t-sala l-weqt).
- [ ] **P1 & P2 - Task 6.4**: Win condition (kamlo 10 levels -> Victory screen).
- [ ] **P1 & P2 - Task 6.5**: Lose condition (lives = 0 -> Game Over screen).

---

### Phase 7: Packaging & Deployment (P2 Lead)
- [ ] **P2 - Task 7.1**: Setup `PyInstaller` spec file bach i-cree single executable standalone.
- [ ] **P2 - Task 7.2**: Bundle assets (images, fonts, default config) dakhel l-package.
- [ ] **P2 - Task 7.3**: Cree packaging script f l-racine (ex: `build_package.sh`).
- [ ] **P2 - Task 7.4**: Cree account f Itch.io w upload build unlisted/private m3a instructions f la page.
- [ ] **P2 - Task 7.5**: Tester installation w launch f machine jdida clean.

---

### Phase 8: Project Management Docs & README (P1 & P2)
- [ ] **P1 & P2 - Task 8.1**: Cree dossier `management/` m3a:
  - `gantt_timeline.md`: Chronologie w planning.
  - `tracking_kanban.md`: Tasks finished, blocked, reviewed.
  - `technical_decisions.md`: 3lach khtarto Pygame, architecture choices.
  - `risk_analysis.md`: Risks w mitigation solutions.
  - `team_organization.md`: Who did what, communication protocol.
  - `test_plan.md`: Acceptance test matrix, bug log.
- [ ] **P1 & P2 - Task 8.2**: Kteb `README.md` kamel b English b ga3 les 10 sections l-mefroudin f l-subject.
- [ ] **P1 & P2 - Task 8.3**: Verification d `make lint` w `flake8 .` w `mypy .` (0 errors!).

---

## 3. Les Problemes, Les Pieges (Troubles) & Kifach T-helouhom

### Trouble 1: Crash dyal Config b Traceback (Red Flag f Defense!)
- **L-mochkil**: L-evaluator ghadi i-mseh key, i-dir string blast int (ex: `"lives": "three"`), aw i-kteb negative number. Ila programme dar `KeyError` aw `ValueError` w t-la7 traceback f terminal = FAIL instantane!
- **L-hal**: 
  - Khass function `ConfigLoader.get(key, default, validator_func)`.
  - Ay exception kay-tched b `try-except`.
  - Ila l-valeur invalide: Afficher message clean: `[CONFIG WARNING] Invalid value for 'lives'. Clamping to default 3.` w kmml l-l3ba 3adi.

### Trouble 2: Comments f JSON
- **L-mochkil**: Standard `json.loads()` f Python ma kay-qbelch comments (`#` aw `//`). Ila qritih direct ghadi i-tla7 `json.decoder.JSONDecodeError`.
- **L-hal**:
  - Qbel ma t-passi l-string l `json.loads()`, dwez regex aw line-by-line filter li kay-hyed ay ster kay-bda b `#` aw spaces + `#`.
  - Gestion dyal inline comments m3a l-ihtiyat ma t-qyasch string fih `#`.

### Trouble 3: Integration d A-Maze-ing Package dyal group akhor
- **L-mochkil**: Kola group i-qder i-dir format d output f chekl (matrix d booleans, list of coordinates, graph object, etc.). Ila bghito t-beddlo code dyalhom, mamnou3!
- **L-hal**:
  - **Adapter Pattern**: Cree classe `MazeAdapter`. Had l-classe kat-chouf l-output d package dyalhom w kat-terjmo l 2D array d tiles li kat-fhem l3ba dyalkom (`WALL`, `CORRIDOR`, etc.).
  - Diro try-except 3la generation: ila package dyalhom dar crash, fallback 3la default backup maze w afficher warning message naqi.

### Trouble 4: Highscore File Corruption & Name Injection
- **L-mochkil**: L-evaluator i-qder i-kteb smia fiha 100 caracteres, emojis, aw symboles bhal `\n`, aw i-mseh file d highscores f west l-l3ba.
- **L-hal**:
  - Validation strict: `name = re.sub(r'[^a-zA-Z0-9 ]', '', name)[:10]`.
  - Highscore file save/load m-hmi b context managers w try-except. Ila file missing aw corrupted, initier tableau fih Top 10 khawi aw par defaut bla crash.

### Trouble 5: Flake8 & Mypy f GUI Library (Pygame)
- **L-mochkil**: Pygame fih bzaf d dynamisme w no-type stubs f chi versions, li kay-khelli `mypy` i-tla7 missing stubs errors.
- **L-hal**:
  - Installi `pygame-stubs` aw configure `mypy.ini` m3a `ignore_missing_imports = True` ghir l pygame ila kan darori (f Makefile had l-flag deja mefroud: `--ignore-missing-imports`).
  - Ma t-khelletch logic d gameplay m3a display: 3zel l-engine 3la pygame bach t-tester l-engine b mypy strict 100%.

### Trouble 6: Pac-Man Corner Stuck (Tile Alignment Bug)
- **L-mochkil**: Melli Pacman kay-koun ghadi w l-la3ib kay-wrek 3la Up aw Down qbel ma i-wsal l intersection b 2 pixels, kay-t'bloqua f l-hayt.
- **L-hal**:
  - Dir "Cornering buffer" aw "Next intended direction" buffer: melli l-la3ib kay-wrek 3la direction, Pacman kay-hfedha w ghyr kay-wsal l l-center d l-case (tile) kay-tourni automatique.

### Trouble 7: Ghosts Trap / Ghost Stacking
- **L-mochkil**: Les 4 fantomes i-qdro i-t-jme3o f nafs l-case w i-wliw bhal wahed, aw i-bqa i-dor f boucle ma i-khorjch mnha.
- **L-hal**:
  - Kola fantome khasso i-koun 3ndo chwiya d personality aw target offset (ex: Blinky target direct Pacman, Pinky target 4 cases qdam Pacman, etc.).
  - Mamnou3 fantome i-dir demi-tour 180 degrees illa ila dkhlo f Frightened mode.

### Trouble 8: Packaging PyInstaller Assets Not Found
- **L-mochkil**: Melli t-dir PyInstaller `--onefile`, assets (sprites, fonts, config) ma kay-tlqawch hit path kay-tbdel f temporary folder `sys._MEIPASS`.
- **L-hal**:
  - Dir helper function `resource_path(relative_path)` li kat-chouf `getattr(sys, '_MEIPASS', os.path.abspath("."))` bach tlqa les assets dima s-hah f development w f standalone bundle.

### Trouble 9: Recode Test f Defense
- **L-mochkil**: L-examinateur i-qol lik f l-defense: *"Zid lia button f l-menu kay-dir Mute l-sowt"*, aw *"Beddel score d pacgum i-wli 50"*, aw *"Dir cheat code f touche C kay-dir kill l ga3 les ghosts"*.
- **L-hal**:
  - Khas l-code ikoun modular bzaf (Kola haja f blast-ha).
  - P1 w P2 bjoj i-kouno qaryin w fahemin ga3 les fichiers machi ghir l-partie dyalhom.
  - Dir mock evaluation binatkom qbel l-defense.



# PacMan Project Structure

## Structure

```text
PacMan/
├── pac-man.py                          # [P1 & P2] Entry point & CLI argument validator
├── Makefile                            # [P2] Automating install, run, debug, clean, lint
├── config.json                         # [P2] Config template with comments
├── build_package.sh                    # [P2] Packaging script for Itch.io / Steam
├── requirements.txt                    # [P2] Runtime and dev dependencies
├── .gitignore                          # [P2] Ignore caches, virtualenvs, builds
├── README.md                           # [P1 & P2] 10 mandatory subject sections
│
├── pacman/
│   ├── config/
│   │   ├── __init__.py                 # [P2]
│   │   └── loader.py                   # [P2] JSON comments parser, fallback & clamping
│   │
│   ├── core/
│   │   ├── __init__.py                 # [P1]
│   │   ├── game.py                     # [P1] Main game loop & state machine controller
│   │   ├── level.py                    # [P1] Level progression & timer countdown
│   │   ├── scoring.py                  # [P1] Non-decreasing scoring calculations
│   │   └── cheats.py                   # [P1] Reviewer cheat toggles (freeze, skip, etc.)
│   │
│   ├── entities/
│   │   ├── __init__.py                 # [P1]
│   │   ├── entity.py                   # [P1] Base moving actor class
│   │   ├── player.py                   # [P1] Pac-Man movement, lives & respawn
│   │   ├── ghost.py                    # [P1] 4 ghosts AI (Chase, Frightened, Respawn)
│   │   └── pellet.py                   # [P1] Pacgums & Super-pacgums
│   │
│   ├── maze/
│   │   ├── __init__.py                 # [P1]
│   │   ├── adapter.py                  # [P1] A-Maze-ing external package adapter
│   │   └── grid.py                     # [P1] 2D matrix, walls, corridors, spawn points
│   │
│   ├── highscore/
│   │   ├── __init__.py                 # [P2]
│   │   └── manager.py                  # [P2] Top 10 persistent storage & name validation
│   │
│   └── ui/
│       ├── __init__.py                 # [P2]
│       ├── renderer.py                 # [P2] Window display, grid drawing & in-game HUD
│       ├── menu.py                     # [P2] Main menu & pause menu
│       ├── screens.py                  # [P2] Game Over / Victory & name input
│       └── assets.py                   # [P2] Resource path resolution for PyInstaller
│
├── management/
│   ├── timeline_gantt.md               # [P2] Planned schedule & milestones
│   ├── progress_tracking.md            # [P1 & P2] Actual progress vs timeline
│   ├── technical_choices.md            # [P1 & P2] Architecture & library analysis
│   ├── risk_analysis.md                # [P1 & P2] Risks & mitigation plans
│   ├── team_organization.md            # [P1 & P2] Task ownership & decision logs
│   └── acceptance_test_plan.md         # [P1 & P2] Test plan & bug tracking matrix
│
└── tests/
    ├── __init__.py                     # [P1 & P2]
    ├── test_config.py                  # [P2] Config loader & fault handling tests
    ├── test_highscore.py               # [P2] Highscore persistence tests
    ├── test_maze_adapter.py            # [P1] Maze adapter & seed generation tests
    └── test_gameplay.py                # [P1] Player lives, scoring & cheat tests
```
