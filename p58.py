def find(arr, target): # O(log n) time, O(1) space
    start, end = 0, len(arr) - 1
    while abs(start - end) > 1:
        mid = (start + end) // 2
        if arr[mid] <= target <= arr[end]:
            start = mid 
        elif arr[start] <= target <= arr[mid]:
            end = mid 
        elif arr[mid] <= arr[start]:
            end = mid 
        elif arr[mid] >= arr[end]:
            start = mid
    if arr[start] == target:
        return start
    elif arr[end] == target:
        return end

print(find([13, 18, 25, 2, 8, 10], 8))