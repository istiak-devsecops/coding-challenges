# challenge A
available_tools = [ "web_search", "calculator", "image_gen" ]
request = {
    "action": "web_search",
    "query": "weather"
}

if request["action"] in available_tools:
    print(f"Tool Authorized")
else:
    print(f"Tool Unauthorized!")

# challenge B
scores = [0.98, 0.95, 0.42, 0.99]
all_passed = True

for score in scores:
    if score < 0.70:
        all_passed = False
        break
if all_passed:
    print("Batch approved")
else:
    print("Batch rejected")    

# challenge C
run_data = {"id": 101, "tokens": 500, "latency": 1.2}
required_keys = ["id", "tokens", "latency", "model_name"]
is_valid = True

for key in required_keys:
    if key not in run_data:
        print(f"{key} is missing!")
        is_valid = False
        break

if is_valid:
    print(f"All keys is available")
