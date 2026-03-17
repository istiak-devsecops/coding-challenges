
from typing import List, Dict

results = [
    {"message": "negative", "score": 0.65},
    {"message": "neutral", "score": 0.75},
    {"message": "positive", "score": 0.85}
    ]

min_score = 0.70

def filter_high_confidence_results(results: List[Dict], min_score: float) -> List[str]: # type hinting for LLM Model to create JSON Schema
    """Filters LLM outputs based on a minimum confidence threshold.""" # Dockstring for AI model
    if not results:
        return []
    
    passed_results = []
    for dictionary in results:
        if dictionary["score"] >= min_score:
            passed_results.append(dictionary["message"])
    return passed_results

print(filter_high_confidence_results(results, min_score))