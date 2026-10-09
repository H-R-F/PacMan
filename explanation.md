# Charh dyal Projet PacMan (Ghosts! More ghosts!) - Part b Part


## Moqaddima (Overview 3am 3la l-projet)
L-hadaf dyal had l-projet howa t-sawbo l3ba dyal **Pac-Man** kamla w khedama b **Python (3.10 awla kter)**, b l-mantiq dyal **OOP (Object-Oriented Programming)**, m3a graphical library sahla (bhal Pygame aw MLX-python), w architecture mferqa w clean. 
L-projet fih bzaf d les pieges: gestion d les erreurs bla crash, integration d maze generator dyal group akhor, systeme d highscore, packaging bhal f Itch.io, w documentation s-hiha.

---

## Chapter I: Forewords (Tarikh w Context)
- Pac-Man khorjat f 1980 mn Namco (creeha Toru Iwatani).
- L-khasais l-mohimma: AI dyal les 4 fantomes (Blinky kay-tbe3 direct, Pinky kay-dir l-kamin/ambush, Inky unpredictable, Clyde kay-tserref b tariqa bizarre).
- Fikra d power-ups (Pacgum / Power Pellet) li katkhlli Pacman yakol les fantomes l-wahed l-weqt qssir.
- F had l-projet, ghadi t-3awdo thyiw had l-arcade classic b Python w b standard modern.

---

## Chapter II: AI Instructions (Qawa3id l-isti3mal d l-AI)
- 42 katgol lik tqder t-kheddem AI bach t-nqos l-khdma l-m3awda (boilerplate, refactoring, ideas).
- **Mais attention:**
  - Khassek tkoun fahem ay ster f l-code. F l-evaluation (peer-review / defense), ghadi t-tsowl 3la kolchi.
  - Ila knti m-copier code bla ma tfhemo, ghadi t-fchel f recode aw l-as'ila d peer-review.
  - Khassek t-noti f README kifach kheddemti l-AI w f ashmn blasa b dabt.

---

## Chapter III: Common Instructions (L-qawa3id l-3amma li mafihomch l-l3eb)

### III.1 General Rules
1. **Python 3.10+**: Khas l-code ikoun compatible m3a Python 3.10 awla jdid.
2. **flake8**: L-code kamel khasso ikoun naqi w kay-htarem flake8 (0 errors, 0 warnings).
3. **No Crash (Graceful Error Handling)**:
   - Ila l-programme dar crash b **traceback** f terminal f l-defense = l-projet kay-t3taber non-functional direct.
   - Ay exception khassha t-ched b `try-except` w t-affichi message wadah w cleanly.
   - Kheddem context managers (`with open(...)`) bach ma i-bqa ta chi file handle mhlol.
4. **Type Hints & mypy**:
   - Ay fonction khassha type hints dyal parameters w return types (`from typing import ...`).
   - Khass l-projet i-doz f `mypy` bla ta chi error.
5. **Docstrings (PEP 257)**:
   - Kol class w kol function khassha docstring wadha (Google style aw NumPy style) katchreh chno katdir, parameters, w chno kat-retuourni.

### III.2 Makefile
Khass darori Makefile f l-racine fih had les rules:
- `make install`: Kay-installe les dependencies (b `pip`, `poetry`, aw `uv`).
- `make run`: Kay-lanci l-l3ba (ex: `python3 pac-man.py config.json`).
- `make debug`: Kay-lanci l-l3ba b debugger d Python (bhal `pdb`).
- `make clean`: Kay-msehh cache files (`__pycache__`, `.mypy_cache`, etc.).
- `make lint`: Kay-lanci:
  ```bash
  flake8 . && mypy . --warn-return-any --warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs
  ```
- `make lint-strict` (optional walakin mezyan): `flake8 . && mypy . --strict`.

### III.3 Additional Guidelines
- Dir unit tests (b `pytest` aw `unittest`) bach t-testi l-logic (parsing config, highscore, maze loading, score, etc.).
- Khass darori `.gitignore` bach ma t-pushech `__pycache__`, `.venv`, `.mypy_cache`.

---

## Chapter IV: Mandatory Part (L-core d l-projet)
Khass l-game t-koun kamla w khedama, fiha:
1. **Config file (JSON with comments)**: Tqra config fih comments.
2. **Robust error handling**: Ma kayench crash ga3!
3. **Maze generator integration**: Khass t-integri l-package `A-Maze-ing` li ghadi i-t3ta likom mn group akhor.
4. **Persistent Highscore**: Kay-tsejel f file JSON f disk.
5. **Polished GUI**: Main menu, game view, in-game HUD, pause menu, game over screen, victory screen.
6. **Cheat mode**: Bach l-evaluator i-qder i-testi kolchi b sehla.
7. **Packaging**: Tqder t-installeh w t-lancih bhal f Itch.io / Steam (build unlisted/private).
8. **Game Loop**:
   - `Main Menu` -> `Start game` -> `Win aw Lose` -> `Enter name for highscore` -> `Back to Main Menu`.

---

## Chapter V: Detailed Specifications (Tafasil l-khedma)

### V.1 Usage
- L-programme kay-tlansa b tariqa whda:
  ```bash
  python3 pac-man.py config.json
  ```
- Khasso yaqbel **exactement 1 argument**: l-chemin d config file (khass ikoun `.json`).
- Ila kan argument zayed, naqess, file ma kayench, aw fih format ghalat: khass message d'erreur clean bla traceback!

### V.2 Configuration File
- L-format: JSON walakin kay-supporti **comments**:
  - Ay ster kay-bda b `#` khasso i-t'ignora.
  - Tqder t-supporti hta `//` aw `/* */` d C/C++.
- Les cles li khass i-kouno supportes (b des valeurs par defaut ila ma kanouch):
  - `highscore_filename`: fin kay-tsejel highscore.
  - `levels` (array d les niveaux): kola level fih `width`, `height`.
  - `lives`: 3 (3 d l-arwah).
  - `pacgum`: 42 (3adad l-pacgums).
  - `points_per_pacgum`: 10.
  - `points_per_super_pacgum`: 50.
  - `points_per_ghost`: 200.
  - `seed`: 42 (seed d level 1).
  - `level_max_time`: 90 (weqt b les secondes f kola level).

### V.3 Faulty Config Handling (T3amol m3a l-ghalat f config)
- **Attention kbira**: F l-defense, l-evaluator ghadi i-beddel l-config w i-dir fih aghlat!
- Ila kan chi champ naqess aw fih valeur ghaltha (ex: `lives: -5` aw string blast int): l-programme khasso i-raddek l-valeur par defaut s-hiha (clamp to safe defaults), i-kteb message f console blli l-valeur tsalhat, w i-kmml l-l3ba bla ma i-t'bloqua w bla traceback!
- Les cles li ma kayninsh f l-specification khasshom i-t'ignoraw direct.

### V.4 Maze Generator Integration (Integration dyal A-Maze-ing)
- **Mamnou3** t-kheddem maze generator dyalk!
- Ghadi t-akhdo package smito `A-Maze-ing` sawboh group akhor.
- Khassek t-kheddmo **as-is** bla ma t-beddel fih hta ster (f review ghadi i-t'reinstalla mn jdid).
- Khass dir **Adapter Pattern** (loader) li kay-akhod output d l-package dyalhom w kay-rodha compatible m3a l-format d Pac-Man.
- L-parametre `PERFECT` khasso ikoun `False` f l-generator bach corridors ikoun fihom bzaf d les chemins w l-lfyat (mashi labyrinth b chemin unique).
- Ila l-generator crasha aw fchel, khassk t-geri l-erreur b tariqa naqiya.

### V.5 Highscore System
- Kay-tsejel f disk (ex: `highscores.json`).
- Khas i-koun resistant l les corruptions (file ma kayench, json m-kherbeq, file fih permission error).
- Smeyat l-la3aba: Max 10 horof, ghir alphanumeric w spaces (A-Z, a-z, 0-9, space).
- Scores: arqam positifs (non-negative integers >= 0).
- Kay-hfed **Top 10** faqat (mretbin mn l-kbir l s-ghir).
- Kay-t'charga f l-bedya, w kay-tsauvegarda melli l-l3ba t-sali.
- Melli l-la3ib i-rbah aw i-khser: kay-dkhel smito, w kay-t'afficha l-highscore f Main Menu.

---

## Chapter VI: Game Specifications (Qawa3id l-l3ba w Gameplay)

### VI.1 Level Structure
- Labyrinthe fih hayt (walls) w mqadrat/mmerrat (corridors) m-creyeen b `A-Maze-ing`.
- **Level 1**: Mazegenerated b **fixed seed** (ex: 42) bach ikoun dima bhal bhal.
- **Levels 2 htal 10+**: Random mazes f kola level jdid.
- **Pacgums**: Noqat sghar f aghlabiyat les corridors.
- **Super-pacgums**: 4 d noqat kbar f les 4 qnat (corners) d l-map.
- **4 Fantomes (Ghosts)**: Wahed f kola qent (corner).
- **Pac-Man**: Kay-bda dima f wast l-map (center/middle).

### VI.2 Player (Pac-Man)
- Kay-t-temcha ghir f corridors (mamnou3 i-doz mn les murs).
- 4 itijahat: Up, Down, Left, Right b les fleches aw WASD.
- 3 d les arwah (lives).
- Ila qaso fantome: kay-khser rooh, w kay-3awd i-t-crea f l-wast (middle respawn).
- Ila salaw 3 d les arwah: **Game Over**.
- Kay-rbah l-level melli kay-akol ga3 les pacgums.
- Kay-rbah l-l3ba كامله melli i-kmml ga3 les levels (minimum 10 levels).
- Scoring:
  - Pacgum = +X pts.
  - Super-pacgum = +Y pts + les fantomes kay-wliw edible (kay-t'aklo) l-wahed l-weqt qssir.
  - Akol fantome edible = +Z pts.

### VI.3 Ghosts (Les Fantomes)
- Kay-t-harqo b tariqa automatique f les corridors.
- Melli kay-kouno f l-hala l-3adiya: kay-tbe3 Pacman (chase AI).
- Melli Pacman kay-akol Super-pacgum: les fantomes kay-herbo mn Pacman (run away AI).
- Ila t-klo: kay-rej3o l l-coin dyalhom w kay-tsennaw chwiya (5 htal 10 seconds) qbel ma i-khorjo tani.

### VI.4 Pacgums & Super-Pacgums
- Pacgums: dots sghar f les corridors.
- Super-pacgums: kbar f les 4 coins.

### VI.5 Cheat Mode (Mode Ghich bach t-sahel l-defense)
- Khass bouton aw raccourci clavier i-aktivi cheat mode:
  - **Invincibility**: Pacman ma kay-moutsh ila qassoh les fantomes.
  - **Level Skip**: T-doz direct l level l-maji b rbah.
  - **Ghost Freeze**: Les fantomes kay-t'jmdo f blast-hom.
  - **Extra Lives**: T-zid arwah l Pacman.
  - **Increased Speed**: T-sre3 Pacman.
- Hadchi kay-htajo l-peer reviewer bach i-tester les 10 levels b z-zerba bla ma i-bqa wahel.

### VI.6 Scoring
- Points d Pacgum (+X), Super-pacgum (+Y), Ghost (+Z).
- L-score **ma kay-nqosch ga3**.

### VI.7 Game Progression
- Au moins **10 levels**.
- Kola level fih **Time Limit** (ex: 90 seconds).
- Ila sala l-weqt: khtaro chno i-wq3 (ex: t-nqos rooh w t-3awd l-level, aw Game Over).
- Score w les arwah li baqyin kay-bqa m-hafad 3lihom bin les levels.
- Kayna Pause / Resume.
- F l-kher (Win aw Lose): affichage d score final, t-dkhel smitek f highscore, w rjoo3 l Main Menu.

### VI.8 User Interface (GUI Screens)
1. **Main Menu**:
   - Start Game.
   - View Highscores (Top 10 b smeyat w scores).
   - Instructions (Les touches w l-qawa3id).
   - Exit.
2. **In-Game HUD** (dima bayen f l-l3ba):
   - Current score.
   - Remaining lives.
   - Current level.
   - Remaining time.
3. **Pause Menu**:
   - Resume game.
   - Return to main menu.
4. **Game Over Screen**: Final score + input d smiya l highscore.
5. **Victory Screen**: Final score + tebrik (congrats) + input d smiya l highscore.

---

## Chapter VII: Project Packaging
- Khass l-l3ba t-koun m-packagea w t-t-lanca b tariqa standalone / bhal f **Itch.io** (aw Steam).
- Khedmo b `PyInstaller` aw tool bhalha bach t-creyw executable standalone w zip package.
- Khass ikoun f l-package instructions sghar (controls, configuration, README).
- Script d packaging (ex: `build_package.sh` aw `setup.py` / `.spec` file) khasso ikoun f racine d git repo.
- F l-defense ghadi i-tlbo mnkom t-3awdo t-creyiw l-package f l-blasa.

---

## Chapter VIII: Project Management (Idarat l-machrou3)
Khass darori dossier f l-repo smito masalan `management/` fih les preuves blli khedmto b tariqa m-nzzma binatkom:
- Timeline / Gantt chart / Kanban export (Trello, GitHub Projects, etc.).
- Suivi d l-progress m3a l-weqt.
- Project analysis & technical choices (3lach khtarto Pygame? 3lach had l-AI algorithm?).
- Risk analysis & mitigation (les risques li kano bhal adapter maze generator, packaging, etc.).
- Team organization: Chkon dar chno (P1 chno dar, P2 chno dar, kifach khdito les decisions).
- Acceptance test plan: Liste d les tests, les bugs li lqito w kifach slhetohom.
- Summary d les blocages w conflicts li wq3o binatkom.

---

## Chapter IX: README Requirements
L-README.md khasso ikoun b **l-lougha l-engliziya (English)** w fih had les sections obligatory:
1. **First Line**: Khas t-koun italic:
   `*This project has been created as part of the 42 curriculum by login1, login2.*`
2. **Description**: Overview 3la l-projet w l-ahdaf dyalo.
3. **Instructions**: Kifach t-installi, t-compile, w t-lanci.
4. **Resources**: Les liens, documentations, w **tafsir wadah kifach t-kheddem AI w f ina tasks**.
5. **Configuration**: Explanation d ga3 les keys d JSON w les valeurs par defaut.
6. **Highscore**: Kifach kheddam w 3lach t-tsawb b hadik l-tariqa.
7. **Maze Generation**: Kifach derto l'integration dyal package `A-Maze-ing`.
8. **Implementation**: Summary technique d l-code.
9. **General Software Architecture**: Diagramme aw chart d les classes w l-modules w l-3alaqat binathoum.
10. **Project Management**: Mokhtasar d kifach sayrto l-projet m3a lien l dossier `management/`.

---

## Chapter X: Submission and Peer-Review + Recode
- Git repo clean, kolchi m-pusti fih.
- **Recode**: F l-peer review, l-evaluator i-qder i-tlob mnnek t-beddel chi haja s-ghira f l-code direct f 5-10 dqiqa (ex: t-zid bouton, t-beddel couleur, t-zid information f display, t-beddel score calculation). Hadchi bach i-t'akd blli nta li katb l-code w fahemo 100%.
