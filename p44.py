def inversions_naive(lst): # O(n^2) time, O(1) space
    return sum(1 for i, elem in enumerate(lst) for after in lst[i + 1:] if elem > after)

print(inversions_naive([2, 4, 1, 3, 5]), inversions_naive([5, 4, 3, 2, 1]))

# def inversions(lst): # interesting idea but wrong
#     lst = sorted(enumerate(lst), key=lambda x: x[1])
#     print([prev_i - i for i, (prev_i, elem) in enumerate(lst)])
#     return sum(prev_i - i for i, (prev_i, _) in enumerate(lst))

# def inversions(lst): # O(nlogn) amortized time, O(n) space if you use a linked list
#     count = 0
#     def swap(a, b):
#         lst[a], lst[b] = lst[b], lst[a]
        
#     def count_swap(a, b):
#         nonlocal count
#         if lst[a] != lst[b]:
#             count += 1
#         lst[a], lst[b] = lst[b], lst[a]

#     def sort(start, stop):
#         i, j = start, start
#         while i < stop:
#             if lst[i] < lst[j]:
#                 count_swap(i, j)
#                 swap(i, j + 1)

def inversions(lst): # O(nlogn) time, O(n) space
    def inversions_between(start, mid, end):
        count, j = 0, mid 
        for i in range(start, mid):
            while j < end and lst[i] > lst[j]:
                j += 1
            else:
                count += j - mid 
        return count 
    
    def merge(start, mid, end): # sort
        left, right = lst[start:mid], lst[mid:end]
        i, j = 0, 0
        for k in range(start, end):
            if j >= len(right) or (i < len(left) and left[i] <= right[j]):
                lst[k] = left[i]
                i += 1
            else:
                lst[k] = right[j]
                j += 1
    
    def helper(start, end):
        if end - start <= 1:
            return 0

        mid = (end + start) // 2
        left, right = helper(start, mid), helper(mid, end)
        between = inversions_between(start, mid, end)
        merge(start, mid, end)

        return left + between + right

    return helper(0, len(lst))

print(inversions([2, 4, 1, 3, 5]), inversions([5, 4, 3, 2, 1]))
