import collections


def minReorder0(n: int, connections: list[list[int]]) -> int:
    def dfs(city: int, parent: int) -> int:
        count = 0
        for a, b in connections:
            if a == city and b != parent:
                count += 1
                count += dfs(b, city)
            elif b == city and a != parent:
                count += dfs(a, city)

        return count

    return dfs(0, 0)


def minReorder(n: int, connections: list[list[int]]) -> int:
    connect = set(tuple(t) for t in connections)
    neighbours: dict[int, set[int]] = collections.defaultdict(set)

    for a, b in connect:
        neighbours[a].add(b)
        neighbours[b].add(a)

    def dfs(city: int):
        for neighbor in neighbours[city]:
            neighbours[neighbor].remove(city)
            connect.discard((neighbor, city))
            dfs(neighbor)

    dfs(0)
    return len(connect)


connections = [[0, 1], [1, 3], [2, 3], [4, 0], [4, 5]]
n = 6
count = minReorder(n, connections)
print(f"{count=}")
