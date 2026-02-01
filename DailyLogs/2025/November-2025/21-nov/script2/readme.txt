# Backup and Archive Folder


Goal: Copy a folder and zip it with a timestamp.
Steps:
- Accept folder name via sys.argv.
- Use shutil.copytree() to copy it to backup_<timestamp>.
- Use shutil.make_archive() to zip the backup folder.

