# File Cleanup Utility

Goal: Delete files older than X days in a given folder.
Steps:
- Accept folder path and number of days via sys.argv.
- Walk through files using os.walk().
- Use os.path.getmtime() and datetime to check age.
- Delete old files using os.remove() or shutil.rmtree()
