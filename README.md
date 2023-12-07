# intellisnake

By Henrik VT [@henrikvtcodes](https://github.com/henrikvtcodes) and Kelsyn C [@LegendOfDust](https://github.com/LegendOfDust)

IntelliSnake is a fun new version of the classic game Snake that comes with features such as:

- 2P Multiplayer
- an algorithmic opponent (not yet developed)
- Chaos Mode

## Gamemodes

### Classic

The snake game that you know and love. Eat grapes like a Roman emperor and grow longer.

### PvP

Ever wanted to play snake with a friend? PvP mode features collision mechanics that allow you to battle it out - who will get the grapes first? Can you cut eachother off and take the win?

### AI Mode

Man Vs. Machine. But, the machine is stupid. Can you outsmart it? Probably.

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

## Credits and Citations

- **Initial Game Inspiration:** https://www.edureka.co/blog/snake-game-with-pygame/
