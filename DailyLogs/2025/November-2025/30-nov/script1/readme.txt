Log Rotation & Archiving Script
- Modules: os, pathlib, shutil, datetime, logging
- Task:
- Scan /var/log/ (or a test directory) for log files older than 7 days.
- Compress them into a .tar.gz archive with a timestamped filename.
- Move the archive to a backup directory.
- Write a log entry for every file rotated.
- DevOps Relevance: Automates log management, prevents disk bloat.
