#extract email address fromt he text

import re
text = "Contact us at help@example.com or support@company.org"

#check for email address pattern
result = re.findall(r'[\w.]+@\w+\.\w+',text) 


print(result)