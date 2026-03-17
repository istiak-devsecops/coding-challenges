from typing import List, Dict


def sanitize_metadata(raw_data: List[Dict]) -> List[str]:
    """sanitizes raw data based on character length, keywords to reduce token usage"""
    if not raw_data:    
        return []
    
    clean_metadata = []

    for data in raw_data:
        content = data["content"].strip()
        if content.upper() == "IGNORE":
            continue

        if len(content) > 50:
            new_short_content = (content[:47])
            clean_metadata.append(new_short_content+"...")
        else:
            clean_metadata.append(content)
    return clean_metadata