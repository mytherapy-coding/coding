def longest_interval1(tickets: list[int]):
    tickets = sorted(tickets)
    tickets.append(tickets[-1] + 2)
    start = 0
    candidate = []
    # [1, 2, 3, 4, 4, 5, 8, 9, 15]
    for end in range(1, len(tickets)):
        if tickets[end] == tickets[end - 1] + 1 or tickets[end] == tickets[end - 1]:
            pass
        else:
            candidate.append(end - start)
            start = end

    return max(candidate)


def longest_interval2(tickets: list[int]):
    tickets = sorted(tickets)
    tickets.append(tickets[-1] + 2)
    start = 0
    iv_longest = 0
    # [1, 2, 3, 4, 4, 5, 8, 9, 15]
    for end in range(1, len(tickets)):
        if tickets[end] - tickets[end - 1] > 1:
            iv_len = end - start
            iv_longest = max(iv_longest, iv_len)
            start = end

    return iv_longest


def longest_interval3(tickets: list[int]):
    tickets = sorted(tickets)
    tickets.append(tickets[-1] + 2)
    start = 0
    end = 0
    iv_longest = 0
    # [1, 2, 3, 4, 4, 5, 8, 9, 15]
    while end < len(tickets):
        iv_longest = max(iv_longest, end - start)
        if tickets[end] - tickets[end - 1] > 1:
            start = end
        end += 1
    return iv_longest


print(longest_interval3([4, 4, 5, 3, 2, 1, 8, 9, 15]))
print(longest_interval3([1, 2, 3, 4, 5]))
