from typing import List, Dict


def sanitize_metadata(raw_data: List[Dict]) -> List[str]:
    """sanitizes raw data based on character length, keywords to reduce token usage"""
    if not raw_data:    
        return []
    
    clean_metadata = []
    for data in raw_data:
        content = data["content"]
        content_char_list = list(content.strip())
        if content.upper() == "IGNORE":
            break
        elif content_char_list > 50:
            new_short_content = "".join(content_char_list[:47])
            clean_metadata.append(new_short_content)
            return clean_metadata