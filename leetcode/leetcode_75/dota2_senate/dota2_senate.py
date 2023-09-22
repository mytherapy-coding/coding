from collections import deque
from collections import Counter


def predictPartyVictory(senate: str) -> str:
    senators = deque(senate)
    buns = 0
    i = 0
    size = len(senators)
    while senators:
        s = senators.popleft()
        if s == 'R':
            if buns >= 0:
                senators.append(s)
            buns += 1
        if s == 'D':
            if buns <= 0:
                senators.append(s)
            buns -= 1
        i += 1
        if i % len(senate) == 0:
            if size == len(senators):
                break
            size = len(senators)
    if buns < 0:
        return 'Dire'
    elif buns > 0:
        return 'Radiant'
    else:
        return ''


def predictPartyVictory1(senate: str) -> str:
    senators = deque(senate)
    buns = 0
    count = Counter(senate)
    while senators:
        s = senators.popleft()
        count[s] -= 1
        if s == 'R':
            if buns >= 0:
                senators.append(s)
                count[s] += 1
            buns += 1
        if s == 'D':
            if buns <= 0:
                senators.append(s)
                count[s] += 1
            buns -= 1
        if count['R'] == 0 or count['D'] == 0:
            break
        print(count, senators)
    if count['D'] == 0:
        return "Radiant"
    elif count["R"] == 0:
        return "Dire"


senate = "DRD"
print(predictPartyVictory1(senate))
