import argparse

# function that validate a IPv4 address
def valid_ipv4(ip):
    parts = ip.split(".")

    if len(parts) != 4:
        return False
    
    for p in parts:
        if not p.isdigit():
            return False
        
        num = int(p)

        if num < 0 or num > 255:
            return False
        
    return True

# main function that takes user input from CLI and validate the ip
def main():
    parser = argparse.ArgumentParser(description="validate an IPv4 address.")
    parser.add_argument("--ip",required=True, help="IPv4 address to validate.")

    args = parser.parse_args()
    ip = args.ip

    if valid_ipv4(ip):
        print(f"{ip} is a valid IPv4 address.")
    else:
        print(f"{ip} is NOT a valid IPv4 address.")