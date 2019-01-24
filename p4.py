def lowest_positive_int_naive(lst):
    lookup = set()
    max_number = lst[0]
    for num in lst:
        if num > 0:
            lookup.add(num)
        if num > max_number:
            max_number = num
    for i in range(1, max_number + 1):
        if i not in lookup:
            return i
    return max_number + 1

def lowest_positive_int_naive_pythonic(lst):
    lookup = set(lst)
    tracker = 1
    while tracker in lookup:
        tracker += 1
    return

lst = [3, 4, -1, 1]
print(lowest_positive_int_naive(lst))
lst = [1, 2, 0]
print(lowest_positive_int_naive(lst))


def lowest_positive_int_naive_2(lst):
    lst.sort()
    tracker = 1
    for num in lst:
        if num > tracker:
            return tracker
        if tracker == num:
            tracker += 1
    return tracker


lst = [3, 4, -1, 1]
print(lowest_positive_int_naive_2(lst))
lst = [1, 2, 0]
print(lowest_positive_int_naive_2(lst))


def lowest_positive_int(lst):
    def swap(a, b):
        temp = lst[a]
        lst[a] = lst[b]
        lst[b] = temp

    for i in range(len(lst)):
        while (lst[i] != i + 1 and lst[i] >= 1 and lst[i] <= len(lst)):
            swap(i, lst[i] - 1)

    tracker = 1
    for num in lst:
        if num > tracker:
            return tracker
        if tracker == num:
            tracker += 1
    return tracker


lst = [3, 4, -1, 1]
print(lowest_positive_int(lst))
lst = [1, 2, 0]
print(lowest_positive_int(lst))
