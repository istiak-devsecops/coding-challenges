import sys
import os
import subprocess
from datetime import datetime, timedelta

if len(sys.argv) < 2:
    print("Usage: python3 script.py <command name>")
    sys.exit(2) # invalid arguments

