from operator import itemgetter

def merge_overlap(intervals):
    intervals.sort(key=itemgetter(0))

    merged = [intervals[0]] 
    for start, end in intervals:
        prev_start, prev_end = merged[-1]
        if start < prev_end:
            merged[-1] = (prev_start, max(end, prev_end))
        else:
            merged.append((start, end))

    return merged 

print(merge_overlap([(1, 3), (5, 8), (4, 10), (20, 25)]))

def merge_overlap_golf(intervals):
    merged = []
    for start, end in sorted(intervals, key=itemgetter(0)):
        prev_start, prev_end = merged[-1]
        if merged and start < prev_end:
            merged[-1] = (prev_start, max(end, prev_end))
        else:
            merged.append((start, end))
    return merged 