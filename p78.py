from collections import deque

def merge_sorted_lists(lists): # O(klogn) time where k = total elems, n = number of lists
    '''takes in deque of deque''' 
    def fix_down(i, heap=lists, key=0):
        k = 2 * i + 1
        while k < len(heap):
            if k + 1 < len(heap) and heap[k + 1][key] > heap[k][key]:
                k += 1
            if heap[k][key] <= heap[i][key]:
                return
            heap[k], heap[i] = heap[i], heap[k]
            k, i = 2 * k + 1, k
        
    # heapify 
    for i in range(len(lists) // 2):
        fix_down(i)

    merged = []
    # extract top elem and fix-down
    while lists:
        merged.append(lists[0][0])
        lists[0].popleft()
        if not lists[0]:
            lists[-1], lists[0] = lists[0], lists[-1]
            lists.pop()
        if lists:
            fix_down(0)
    
    return merged 

# not tested

# or use built-in heapq