# Run linux commands through python script
import subprocess 
import platform

def custom_command(*command):
    if platform.system() == "Linux":
        result = subprocess.run(command, capture_output=True, text=True)
        return result.stdout.strip()
    else:
        return "This function will only work on linux..."
    

health_check = custom_command("df", "-h")
print(health_check)
