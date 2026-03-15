import argparse
import subprocess

# function to check the service
def check_service(service_name):
    try:
        result = subprocess.run(["systemctl","is-active", service_name], capture_output=True, text=True)

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

# main function to take CLI command"
def main():
    parser = argparse.ArgumentParser(description="check service status")
    parser.add_argument("--service", required=True, help="Service name to check.")

    args = parser.parse_args()
    check_service(args.service)

if __name__=="__main__":
    main()