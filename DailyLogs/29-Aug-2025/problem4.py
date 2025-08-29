#regex challenge: extract email address from text

text = """
Contact us at support@example.com or sales@company.org.
You can also reach out to admin@devsecops.io or hello.world@fake-email.net.
"""
import re

pattern = r'\w+@\w+\.\w+' #search pattern

email_address_list = re.findall(pattern, text)

print(email_address_list)