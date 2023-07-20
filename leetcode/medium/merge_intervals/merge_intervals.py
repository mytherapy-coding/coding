def merge(intervals: list[list[int]]) -> list[list[int]]:
    if not intervals:
        return []
    ordered = sorted(intervals)
    res = []
    candidate_start, candidate_end = ordered[0]
    for start, end in ordered:
        if start <= candidate_end:
            candidate_end = max(candidate_end, end)
        else:
            res.append([candidate_start, candidate_end])
            candidate_start = start
            candidate_end = end
    res.append([candidate_start, candidate_end])
    return res


intervals = [[1,3],[2,6],[8,10],[15,18]]
print(merge(intervals))
intervals = [[1,4],[4,5]]
print(merge(intervals))
intervals = []
print(merge(intervals))
intervals = [[1,3],[1,6]]
print(merge(intervals))
intervals = [[1, 6], [2, 3]]
print(merge(intervals))


