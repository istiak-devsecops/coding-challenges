# Python Script Runner with Metadata
Modules: sys, os, subprocess, datetime
Goal: Run another Python script and log its metadata.
Steps:
- Accept a .py filename via sys.argv.
- Use subprocess.run() to execute it.
- Log script name, start time, end time, and exit code.
