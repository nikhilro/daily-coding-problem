def running_median_naive(lst): # O(n^2 * logn) time, O(n) space
    for i in range(1, len(lst) + 1):
        ordered = sorted(lst[:i])
        l = len(ordered)
        if l % 2 == 0:
            print((ordered[l // 2] + ordered[l // 2 - 1]) / 2)
        else:
            print(ordered[l // 2])
        
running_median_naive([2, 1, 5, 7, 2, 0, 5]) 

def running_median_semi_naive(lst): # O(nlogn) time, O(n) space    
    from bisect import bisect

    running_sort = []
    for i, num in enumerate(lst):
        bisect(running_sort, )