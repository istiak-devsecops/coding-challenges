# Extract all the numbers from:

text = "Error codes: 404, 503, 200. Retry in 30 seconds."

import re
numbers = re.findall(r"\d+",text)

print(f"All the number from the text: {numbers}")