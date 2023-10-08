def canVisitAllRooms(rooms: list[list[int]]) -> bool:
    keys = {0}
    rooms_to_visit = set(range(len(rooms)))
    print(rooms_to_visit)
    while rooms_to_visit:
        candidates = keys & rooms_to_visit
        if not candidates:
            return False
        key = candidates.pop()
        rooms_to_visit.remove(key)
        keys.update(rooms[key])
    return True


rooms = [[1], [2], [3], []]
print(canVisitAllRooms(rooms))
