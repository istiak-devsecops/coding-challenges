#Group tool names by the first letter of their status

tools = {"nginx": "installed", "mysql": "missing", "node": "installed", "mongo": "missing"}

grouped = {}

for tool,status in tools.items():
    first_letter = status[0]
    if first_letter not in grouped:
        grouped[first_letter] = []
    grouped[first_letter].append(tool)

print(grouped)
