import queue


# O(nlogn) time, O(n) space <-maybe more
def min_required_rooms_naive(intervals):
    timequeue = queue.PriorityQueue()

    for interval in intervals:
        timequeue.put(interval)

    overlap = timequeue.get()
    current_overlap, max_overlap = 1, 1

    while True:
        try:
            current_interval = timequeue.get(False)
        except queue.Empty:
            del timequeue
            return max_overlap
        else:
            if current_interval[0] < overlap[1]:
                current_overlap += 1
                overlap = (current_interval[0], overlap[1])
                if current_interval[1] > overlap[1] and timequeue.queue:
                    timequeue.put((overlap[1], current_interval[1]))
                elif current_interval[1] < overlap[1] and timequeue.queue:
                    timequeue.put((current_interval[1], overlap[1]))
            else:
                if max_overlap < current_overlap:
                    max_overlap = current_overlap
                overlap = current_interval
                current_overlap = 1


print(min_required_rooms_naive([(30, 75), (0, 50), (60, 150)]))


def min_required_rooms_second_naive(intervals):  # not tested
    def overlap(a, b):
        return not (a[1] < b[0] or b[1] < a[0])

    current_overlap, max_overlap = 0, 0
    for overlap_interval in intervals:
        for interval in intervals:
            if overlap(overlap_interval, interval):
                current_overlap += 1

        if current_overlap > max_overlap:
            max_overlap = current_overlap
        current_overlap = 0

    return max_overlap


def min_required_rooms_second_naive_golf(intervals):  # O(n^2) time, O(1) space
    def overlap(a, b):
        return not (a[1] < b[0] or b[1] < a[0])

    current_max = 0
    for interval in intervals:
        overlaps = sum([overlap(interval, other_interval)
                        for other_interval in intervals])
        current_max = overlaps - 1 if overlaps > current_max else current_max

    return current_max


print(min_required_rooms_second_naive_golf([(30, 75), (0, 50), (60, 150)]))


def min_required_rooms(intervals):  # O(nlogn) time, O(n) space
    intervals = [((start_time, 1), (end_time, -1))
                    for start_time, end_time in intervals]

    times = sorted([time for times in intervals for time in times],
                    key=lambda time: time[0])

    current_overlap, max_overlap = 0, 0
    for time in times:
        current_overlap += time[1]
        max_overlap = max(current_overlap, max_overlap)

    return max_overlap


print(min_required_rooms([(30, 75), (0, 50), (60, 150)]))
