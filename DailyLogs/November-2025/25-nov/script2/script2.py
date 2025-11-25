import sys
import json
from pathlib import Path

data = {
    "theme": "dark",
    "autosave": True,
    "backup_interval": 15
}

setting_path = Path("settings.json")

# stores the setting into the settings.json file
with setting_path.open("w")as file:
    json.dump(data, file, indent=4)


# opens the file to show output
with setting_path.open()as file:
    setting = json.load(file)


# check if user only wants to print the current setting
if  len(sys.argv) == 1:
    print("Current settings: \n")
    print(json.loads(setting, indent=4))
    sys.exit(0) # success

if len(sys.argv) != 3:
    print("Usage: python3 script.py <key> <value>")
    sys.exit(1) # exit code missing arguments

key = sys.argv[1]
value = sys.argv[2]

if value.lower() == "true":
    value = True
elif value.lower() == "false":
    value = False
else:
    # Try converting numeric values
    try:
        value = int(value)
    except ValueError:
        pass  # keep string

# Update the setting
setting[key] = value

# Save back to file
with setting_path.open("w") as file:
    json.dump(setting, file, indent=4)

print(f"Updated '{key}' → {value}")