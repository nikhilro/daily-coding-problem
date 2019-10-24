def running_median_naive(lst): # O(n^2 * logn) time, O(n) space
    for i in range(1, len(lst) + 1):
        ordered = sorted(lst[:i])
        l = len(ordered)
        if l % 2 == 0:
            print((ordered[l // 2] + ordered[l // 2 - 1]) / 2)
        else:
            print(ordered[l // 2])
        
running_median_naive([2, 1, 5, 7, 2, 0, 5]) 
print("----")

def running_median_semi_naive(lst): # O(nlogn) time, O(n) space    
    from bisect import bisect

    running_sort = []
    for _, _ in enumerate(lst):
        bisect(running_sort)
        # inserting is cost intensive, this won't work 

def running_median(lst): # O(nlogn) time, O(n) space
    import heapq 

    # maintain left side (max heap), median, right side (min heap)
    max_heap, min_heap = [], [] 
    for num in lst:
        if max_heap and max_heap[0] > num:
            max_heap.append(num)
            heapq._siftup_max(max_heap, len(max_heap) - 1)
        else:
            heapq.heappush(min_heap, num)

        lmax, lmin = len(max_heap), len(min_heap)
        if lmax > lmin + 1:
            heapq.heappush(min_heap, heapq._heappop_max(max_heap))
        elif lmin > lmax + 1: 
            max_heap.append(heapq.heappop(min_heap))
            heapq._siftup_max(max_heap, lmax - 1)

        lmax, lmin = len(max_heap), len(min_heap)
        if lmax == lmin:
            print((max_heap[0] + min_heap[0]) / 2)
        elif lmax - lmin == 1:
            print(max_heap[0])
        else: # lmin - lmax == 1
            print(min_heap[0])
            
running_median([2, 1, 5, 7, 2, 0, 5]) 