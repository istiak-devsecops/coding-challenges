from typing import List

def calculate_average_confidence(scores: List[float]) -> float:
    """calculate average confidence weight in a multi-agent system"""
    if not scores:
        return 0.0
    
    valid_scores = []
    
    for score in scores:
        if score < 0.0 or score > 1.0:
            continue
        else:
            valid_scores.append(score)
    
    if not valid_scores:
        return 0.0
        
    average = sum(valid_scores)/len(valid_scores)
    return average
        

