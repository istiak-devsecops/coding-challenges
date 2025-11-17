Create a .log File with Script Name and Timestamp

import module

assign script name to the variable (script_name sys.argv[0])
assign datetime to variable timestamp
assign logfile name to logfile variable using script name and timestamp

with open(logfile, "w")as file:
    file.write("Log created by {script name} at {timestamp}")

print(f"Log file created {log file}")

