blocked_words = [ "password", "secret", "api_key" ]
llm_response = { 
    "status": "success", 
    "text": "Here is your secret token: 12345" 
    }
is_safe = True

if llm_response["status"] == "success" and is_safe: 
    for word in blocked_words:
        if word in llm_response["text"]:
            print(f"BLOCKING RESPONSE: Sensitive data detected.")
            is_safe = False
            break
else:
    print(f"BLOCKING RESPONSE: Sensitive data detected.")
    is_safe = False

if is_safe:
    print(f"Response safe.")



    
