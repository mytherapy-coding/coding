def find_stable_mountains(height, threshold):
    result = []
    for i in range(1, len(height)):
        if height[i - 1] > threshold:
            result.append(i)
    return result


def test_find_stable_mountains():
    print(find_stable_mountains([1,2,3,4,5], 2), "== [3, 4]")
    print(find_stable_mountains([10,1,10,1,10], 3), "== [1, 3]")
    print(find_stable_mountains([10,1,10,1,10], 10), "== []")
    print(find_stable_mountains([5,5,5,5], 4), "== [1, 2, 3]")
    print(find_stable_mountains([5,5,5,5], 5), "== []")
    print(find_stable_mountains([2,100], 50), "== [1]")
    print(find_stable_mountains([1,50,1,50,1], 10), "== [1, 3]")

test_find_stable_mountains()
