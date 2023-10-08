def findCircleNum(isConnected: list[list[int]]) -> int:
    def find_provice(city: int) -> set[int]:
        provice = {city}
        cities_to_visit = [city]
        while cities_to_visit:
            x = cities_to_visit.pop()
            for y in range(len(isConnected[x])):
                if isConnected[x][y] == 1 and y not in provice:
                    cities_to_visit.append(y)
                    provice.add(y)
        return provice

    count = 0
    all_provinces = set()
    for city in range(len(isConnected)):
        if city not in all_provinces:
            p = find_provice(city)
            all_provinces.update(p)
            count += 1
    return count



matrix = [
    [1, 1, 0],
    [1, 1, 0],
    [0, 0, 1]
]
# matrix[1][0] == 1 if city 1 and 0 are connected directly
print(matrix)
print()
print(findCircleNum(matrix))