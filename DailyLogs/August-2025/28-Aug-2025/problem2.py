# Extract Acronym Expansion
import re

text = "We use CI/CD (Continuous Integration and Continuous Deployment) in DevOps. The API (Application Programming Interface) is essential. The CEO (Chief Executive Officer) made a statement."

# find all acronym and full form pairs
matches = re.findall(r'([A-z\/]+)\s*\(([^)]+)\)',text)

valid_expansions = []

for acronym, full_form in matches:
    word_count = len(full_form.split()) #split the text to count number of word
    if word_count >= 3:
        valid_expansions.append(full_form) #if word count >= 3 then it will append to the list

print(valid_expansions)