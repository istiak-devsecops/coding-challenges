# Use collections.deque with maxlen=5.

# Keep appending log entries (like "Error at 12:01", "OK at 12:02").

# Once max length is hit, old entries should drop automatically.

# Print final deque to show only last 5 logs.

from collections import deque

#log entries won't hold value more than 5
log_entries = deque(maxlen=5)


#simulating the log entries
log_entries.append("Error at 12:30 PM")
log_entries.append("ok at 12:50 PM")
log_entries.append("Error at 1:30 PM")
log_entries.append("Error at 2:30 PM")
log_entries.append("Error at 3 PM")
log_entries.append("Ok at 4 PM")

print("Last 5 log entries are: \n")
for log in log_entries:
    print(log)
