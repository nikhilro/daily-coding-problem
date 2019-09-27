# question in bonus.png
def min_weights_over_domain(intervals, weights): # O(nlogn) time, O(n) space
    assert len(intervals) == len(weights)

    if len(intervals) == 1:
        return [(min(intervals[0]), weights[0], max(intervals[0]))]
    
    mid = len(intervals) // 2
    left = min_weights_over_domain(intervals[:mid], weights[:mid])
    right = min_weights_over_domain(intervals[mid:], weights[mid:])

    merged, i, j = [], 0, 0
    while i < len(left) and j < len(right):
        if (left[i][2] > right[j][2]):
            right, left = left, right
            i, j = j, i

        left_lb, left_w, left_rb = left[i]
        right_lb, right_w, right_rb = right[j]

        if left_lb <= right_lb and left_rb <= right_lb:
            merged.append(left[i]) 
            i += 1
        elif left_lb <= right_lb:
            if left_lb != right_lb:
                merged.append((left_lb, left_w, right_lb))
            merged.append((right_lb, min(left_w, right_w), left_rb))
            i += 1
            if left_rb != right_rb:
                right[j] = (left_rb, right_w, right_rb)
            else:
                j += 1
        elif left_lb > right_lb:
            merged.append((right_lb, right_w, left_lb))
            merged.append((left_lb, min(left_w, right_w), left_rb))
            i += 1
            if left_rb != right_rb:
                right[j] = (left_rb, right_w, right_rb)
            else:
                j += 1
    
    if i < len(left):
        merged.extend(left[i:])
    if j < len(right):
        merged.extend(right[j:])
    
    return merged

intervals = ((1, 15), (8, 9), (3, 5), (2, 4), (11, 12))
weights = (4, 3, 3, 2, 5)
sol = min_weights_over_domain(intervals, weights)
print(sol)