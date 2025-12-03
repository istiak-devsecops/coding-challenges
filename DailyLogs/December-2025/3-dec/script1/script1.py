import re
import json
import pathlib


def extract_contact(input_file, output_file="contacts.json"):
    text = pathlib.Path(input_file).read_text()

    # email pattern
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'

    # phone pattern
    phone_pattern = r'\+?\d[\d\s\-]{11,}\d'

    emails = re.findall(email_pattern, text)
    phones = re.findall(phone_pattern, text)

    data = { 
        "emails": list(set(emails)),
        "phones": list(set(phones))
    }

    pathlib.Path(output_file).write_text(json.dumps(data, indent=4))
    print(f"Saved to {output_file}")

if __name__=="__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python script.py <file.txt>")
        sys.exit(1)
    
    extract_contact(sys.argv[1])