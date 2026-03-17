

def route_instruction(prompt: str) -> str:
    """tool orchestration by filtering user prompt"""
    prompt = prompt.strip().lower()

    if "search" in prompt or "find" in prompt:
        return "web_search_agent"
    elif "calc" in prompt or "math" in prompt:
        return "calculator_agent"
    else:
        return "general_purpose_agent"