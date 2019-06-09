def check_non_decreasing(arr): # O(n) time, O(1) space
    count = 0
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            if count:
                return False
            if not (i == len(arr) - 1 or i == 1
                        or arr[i - 1] <= arr[i + 1] or arr[i] >= arr[i - 2]):
                return False
            count += 1
    return True

print(check_non_decreasing([10, 5, 7]), check_non_decreasing([10, 5, 1]))