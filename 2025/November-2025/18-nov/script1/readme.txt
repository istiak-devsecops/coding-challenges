# Log File Organizer


Import os, datetime
Get list of all files in current directory
For each file:
    If file ends with ".log":
        Get creation date
        Format date as YYYY-MM-DD
        Create folder named after date if it doesn't exist
        Move log file into that folder
