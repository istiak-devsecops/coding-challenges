# run a linux commands in with python script

import subprocess

ps = subprocess.Popen(["ps", "aux"], stdout=subprocess.PIPE, text=True)
grep = subprocess.Popen(["grep", "nginx"], stdin=ps.stdout, stdout=subprocess.PIPE, text=True)
result = grep.communicate()[0]  # This will take only the first output if there is multiple

print(result)