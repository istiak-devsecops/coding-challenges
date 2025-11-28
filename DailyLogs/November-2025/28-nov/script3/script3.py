import argparse
import subprocess

# function to check the service

def check_service(service_name):
    try:
        result = subprocess.run(["systemctl","status", service_name], capture_output=True, text=True)

        status = result.stdout.strip()

        if status == "active":
            print(f"Service {service_name} is active.")
        elif status == "inactive":
            print(f"service {service_name} is inactive.")
        elif status == "failed":
            print(f"service {service_name} has faiiled.")
        else:
            print(f"Service {service_name} status:{status}")
    except Exception as e:
        print(f"Error: checking service {e}")

        