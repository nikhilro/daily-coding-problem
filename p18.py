def sliding_max_array_naive(arr, k): # O(n*k) time, O(1) space
    for i in range(k - 1, len(arr)):
        print(max(arr[i - k + 1 : i + 1]))

sliding_max_array_naive([10, 5, 2, 7, 8, 7], 3)

def sliding_max_array_naive_cleaner(arr, k):
    for i in range(len(arr) - (k - 1)):
        print(max(arr[i : i + k]))

sliding_max_array_naive_cleaner([10, 5, 2, 7, 8, 7], 3)

from collections import deque

def sliding_max_array(arr, k): # O(n) time, O(k) space
    lookback = deque()
    for i, elem in enumerate(arr):
        try:
            while lookback[0][1] < elem:
                lookback.popleft()
        except IndexError:
            pass

        lookback.appendleft((i, elem))

        if i >= k - 1:
            print(lookback[-1][1])

        try:
            while i - lookback[-1][0] >= k - 1:
                lookback.pop()
        except IndexError:
            pass

sliding_max_array([10, 5, 2, 7, 8, 7], 3)

def sliding_max_array_cleaner(arr, k): # O(n) time, O(k) space
    lookback = deque()
    for i, elem in enumerate(arr):
        while lookback and lookback[0][1] < elem:
            lookback.popleft()

        lookback.appendleft((i, elem))

        if i >= k - 1:
            print(lookback[-1][1])

        while lookback and i - lookback[-1][0] >= k - 1:
            lookback.pop()

sliding_max_array_cleaner([10, 5, 2, 7, 8, 7], 3)
