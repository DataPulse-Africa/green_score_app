# Build the scoring logic
def calculate_score(responses):
    total_possible = len(responses) * 3
    total_score = sum(responses)
    green_score = (total_score / total_possible) * 100
    return round(green_score, 2)
