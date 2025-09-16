import functools


def canJump1(nums: list[int]) -> bool:
    # [2,3,1,1,4]
    if len(nums) == 1:
        return True

    for jump in range(1, min(nums[0] + 1, len(nums))):
        if canJump1(nums[jump:]):
            return True

    return False


def canJump2(nums: list[int]) -> bool:
    if len(nums) == 1:
        return True
    return any(canJump2(nums[jump:]) for jump in range(1, min(nums[0] + 1, len(nums))))


def canJump3(nums: list[int]) -> bool:
    def f(i):
        # [2,30,1,4, 1]
        if i == len(nums) - 1:  # fixit
            return True
        max_jump = min(nums[i], len(nums) - i - 1)  # fixit
        """
        nums = [2, 3, 5, 1, 0, 4]
        i = 2 
        range = (1, 4)
        jump = 1 
          |
          f(i + jump) 
        
        """
        for jump in range(1, max_jump + 1):
            if f(i + jump):  # ?????
                return True
        return False

    return f(0)


def canJump4(nums: list[int]) -> bool:
    cache = set()

    def f(i):
        if i == len(nums) - 1:
            return True
        if i in cache:
            return False
        max_jump = min(nums[i], len(nums) - i - 1)
        for jump in range(1, max_jump + 1):
            if f(i + jump):
                return True
        # remember for this i the answer is False
        cache.add(i)
        return False

    return f(0)


def canJump5(nums: list[int]) -> bool:
    @functools.cache
    def f(i):
        if i == len(nums) - 1:
            return True
        max_jump = min(nums[i], len(nums) - i - 1)
        for jump in range(1, max_jump + 1):
            if f(i + jump):
                return True
        return False

    return f(0)


def canJump6(nums: list[int]) -> bool:
    @functools.cache
    def f(i):
        if i == len(nums) - 1:
            return True
        max_jump = min(nums[i], len(nums) - i - 1)
        for jump in range(1, max_jump + 1):
            if f(i + jump):
                return True
        return False

    return f(0)


can_jump = canJump5
nums = [2, 3, 1, 1, 4]
print(can_jump(nums))

nums = [2, 3, 1, 1, 0, 4]
print(can_jump(nums))

nums = [2, 3, 5, 1, 0, 4]
print(can_jump(nums))

nums = [100] * 100 + [0] * 101
print(can_jump(nums))


@functools.cache
def foo(n):
    for _ in range(n):
        print("Hello", n)
    return n * 10


print(foo(2))
print(foo(3))
print(foo(2))

# create a decorator cache
