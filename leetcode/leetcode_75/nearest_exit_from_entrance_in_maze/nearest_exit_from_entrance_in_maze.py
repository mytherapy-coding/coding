import collections


def nearestExit(maze: list[list[str]], entrance: list[int]) -> int:
    neighbors = collections.defaultdict(set)
    exits = set()

    for y in range(len(maze)):
        for x in range(len(maze[y])):
            if maze[y][x] == ".":
                key = (y, x)
                if y == 0 or y == len(maze) - 1 or x == 0 or x == len(maze[y]) - 1:
                    exits.add(key)
                for y1, x1 in (y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1):
                    if (
                        0 <= y1 < len(maze)
                        and 0 <= x1 < len(maze[y])
                        and maze[y1][x1] == "."
                    ):
                        key1 = (y1, x1)
                        neighbors[key].add(key1)
    print(neighbors)
    print(exits)
    start = (entrance[0], entrance[1])
    exits.discard(start)

    def bfs(start: tuple[int, int]) -> int:
        visited = {start}
        nodes_to_visit = collections.deque()
        nodes_to_visit.append((start, 0))
        while nodes_to_visit:
            node, distance = nodes_to_visit.popleft()
            print(node, distance)
            if node in exits:
                return distance
            for neighbor in neighbors[node]:
                if neighbor not in visited:
                    nodes_to_visit.append((neighbor, distance + 1))
                    visited.add(neighbor)
        return -1

    return bfs(start)


maze = [["+", "+", ".", "+"], [".", ".", ".", "+"], ["+", "+", "+", "."]]
entrance = [1, 2]
print(nearestExit(maze, entrance))


maze = [["+", "+", ".", "+"], [".", ".", ".", "+"], ["+", "+", "+", "."]]
entrance = [2, 3]
nearestExit(maze, entrance)
"""
[["+", "+", ".", "+"],
[".", ".", ".", "+"],
["+", "+", "+", "."]]
"""
