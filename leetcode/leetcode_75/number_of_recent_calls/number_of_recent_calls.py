import collections


class RecentCounter0:
    def __init__(self):
        self.requests = []

    def ping(self, t: int) -> int:
        self.requests.append(t)
        return sum(t - 3000 <= r <= t for r in self.requests)


class RecentCounter:
    def __init__(self):
        self.requests = []

    def ping(self, t: int) -> int:
        self.requests.append(t)
        res = [t - 3000 <= r for r in self.requests]
        return len(res)


class RecentCounter1:
    def __init__(self):
        self.requests = collections.deque()

    def ping(self, t: int) -> int:
        self.requests.append(t)
        while self.requests[0] + 3000 < t:
            self.requests.popleft()
        return len(self.requests)


class RecentCounter2:
    def __init__(self):
        self.requests = []

    def ping(self, t: int) -> int:
        self.requests.append(t)
        while self.requests[0] + 3000 < t:
            self.requests.pop(0)
        return len(self.requests)


recentCounter = RecentCounter2()
print(recentCounter.requests)
n = recentCounter.ping(1)  # requests = [1], range is [-2999,1], return 1
print(recentCounter.requests, n)
m = recentCounter.ping(100)  # requests = [1, 100], range is [-2900,100], return 2
print(recentCounter.requests, m)
q = recentCounter.ping(3001)  # requests = [1, 100, 3001], range is [1,3001], return 3
print(recentCounter.requests, q)
s = recentCounter.ping(
    3002
)  # requests = [1, 100, 3001, 3002], range is [2,3002], return 3
print(recentCounter.requests, s)
