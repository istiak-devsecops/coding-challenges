import argparse

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


