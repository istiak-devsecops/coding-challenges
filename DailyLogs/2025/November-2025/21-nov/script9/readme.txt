File Organizer by Extension

- Import os, shutil
- Accept target folder via sys.argv
- For each file in folder:
    - Get extension (e.g., .txt, .jpg)
    - Create subfolder named after extension if not exists
    - Move file into that subfolder using shutil.move()


