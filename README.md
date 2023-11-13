# intellisnake

# Get Started

## VSCode

1. Open Command Palette
   `ctrl+shift+p`
2. Search for and activate the `Python: Create Environment` option
3. Click on the `Venv` option
4. Use (click on) default Python Version (should be highlighted)
5. Select `requirements.txt` for dependencies to install, then click Ok

✨You're ready to go! ✨

## Manual

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
