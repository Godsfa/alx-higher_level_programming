def weight_average(my_list=[]):
    if not my_list:
        return 0

    total_score = 0
    total_weight = 0

    for score, weight in my_list:
        total_score += score * weight
        total_weight += weight

    return total_score / total_weight

# Example usage:
scores_weights = [(80, 2), (90, 3), (75, 1)]
result = weight_average(scores_weights)
print(result)  # Output: 86.25
