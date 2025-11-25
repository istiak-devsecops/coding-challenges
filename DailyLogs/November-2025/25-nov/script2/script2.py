import json
from pathlib import Path

data = {
    "theme": "dark",
    "autosave": True,
    "backup_interval": 15
}

setting_path = Path("settings.json")

with setting_path.open("w")as file:
    json.dump(data, file, indent=4)
