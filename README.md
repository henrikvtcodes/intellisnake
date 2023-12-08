# intellisnake

By Henrik VT [@henrikvtcodes](https://github.com/henrikvtcodes) and Kelsyn C [@LegendOfDust](https://github.com/LegendOfDust)

IntelliSnake is a fun new version of the classic game Snake that comes with features such as:

- Classic Single Player
- 2P Multiplayer
- An AI Algoritmic Opponent
- Sound Effects

See below for different gamemodes!

### Running the Game

**Required Modules**

```txt
pygame==2.5.2
pygame-widgets==1.1.4
```

**How to run**

```sh
# --- Create Virtual Environment ---
python -m venv .venv
# --- Activate Virtual Environment ---
# Mac OS / Linux
source .venv/bin/activate
# Windows
./.venv/bin/Activate.ps1
# --- Install Dependencies ---
pip install -r requirements.txt
# --- Run Program! ---
python src/main.py
```

**Fun Trick**
If you go into the `src/constants.py` file and find line 46, you can change the game speed. This increases the overall framerate therefore speeding up the game overall. It's extremely entertaining to crank up the speed, play AI mode, and just watch the AI fly around the board.

## Gamemodes

### Classic

The snake game that you know and love. Eat grapes like a Roman emperor and grow longer.

### PvP

Ever wanted to play snake with a friend? PvP mode features collision mechanics that allow you to battle it out - who will get the grapes first? Can you cut eachother off and take the win?

### AI Mode

Man Vs. Machine. The machine is quick to get the grapes, so you better outsmart it!

### God Mode
Classic but with a twist - whenever you eat, a new effect befalls you! Some effects will stack. Can you beat this near-impossible challenge?

### Development

**Testing**  
The process we used to test functions of the game is simply playtesting. Whenever we updated/fixed anything, we would run the game and try to cause problems. This would involve things like keysmashing, intentionally running into walls, and setting the snakes to collide with eachother in various ways. In order to test the AI, we set the speed extremely high to make sure that it doesn't fail too quickly.

**Work Distribution**
| Henrik | Kelsyn |
| ------ | ------ |
| - AI Algorithm v1 | - AI Algorithm v2 |
| - Main Loop Structure | - Art Assets & Color |
| - Organization and Conventions | - Classic and pvp base programming |

### Known Issues

- The game will generally prevent you from doubling back on yourself, but if you press the right keys quick enough it will "break the snake's neck"
- If allowed to run long enough, the AI algorithm will eventually trap itself, run into the human player, or hit the wall. Fixing this would be an order of magnitude more work because we would have to calculate moves ahead of time.

## Credits and Citations

- **Initial Game Inspiration:** https://www.edureka.co/blog/snake-game-with-pygame/
- Prof. Cafiero for discovering the race condition that was making Henrik tear his hair out

## Development: Get Started

### VSCode

1. Open Command Palette with
   `Ctrl + Shift + P`
2. Search for and click on the `Python: Create Environment` option
3. Click on the `Venv` option
4. Use (click on) default Python Version (should be highlighted)
5. Select `requirements.txt` for dependencies to install, then click Ok

✨You're ready to go! ✨

### Manual

1. Create the Virtual Environment

```sh
python -m venv .venv
```

2. Activate the Virtual Environment (may be able to ignore this if using VSCode)
   MacOS

```sh
# Mac OS / Linux
source .venv/bin/activate
# Windows
./.venv/bin/Activate.ps1
```

3. Install Packages

```sh
pip install -r requirements.txt
```

### Adding Packages

1. Install packages

```sh
pip install <package>
```

2. Delete and recreate `requirements.txt`

```sh
# Does not work on Windows
rm -f requirements.txt && pip freeze > requirements.txt
```
