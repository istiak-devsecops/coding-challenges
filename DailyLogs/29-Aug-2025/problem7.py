# Extract all words that start with a capital letter from:

import re
text = "DevOps Engineers use Python, Docker, and Kubernetes."

pattern = r'\b[A-Z][a-z]*\b'
search_result = re.findall(pattern,text)

print(f"All words start with capital letter: ", search_result)