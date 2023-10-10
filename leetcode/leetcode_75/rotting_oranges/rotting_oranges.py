import collections


def orangesRotting(grid: list[list[int]]) -> int:
    neighbors = collections.defaultdict(set)
    starts = set()
    count = 0
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] != 0:
                key = (y, x)
                count +=1
                if grid[y][x] == 2:
                    starts.add(key)
                for y1, x1 in (y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1):
                    if 0 <= y1 < len(grid) and 0 <= x1 < len(grid[y]) and grid[y1][x1] != 0:
                        key1 = (y1, x1)
                        neighbors[key].add(key1)
    print(neighbors)
    print(starts)

    def bfs(starts: set[tuple[int, int]]) -> int:
        visited = set(starts)
        nodes_to_visit = collections.deque((start, 0) for start in starts)
        time = 0
        while nodes_to_visit:
            node, time = nodes_to_visit.popleft()
            print(node, time)
            for neighbor in neighbors[node]:
                if neighbor not in visited:
                    nodes_to_visit.append((neighbor, time + 1))
                    visited.add(neighbor)
        print(visited)
        print(list(neighbors.keys()))
        return time if count == len(visited) else -1

    return bfs(starts)


grid = [[2,1,1],[0,1,1],[1,0,1]]
print(orangesRotting(grid))
