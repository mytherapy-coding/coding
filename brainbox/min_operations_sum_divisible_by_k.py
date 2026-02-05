def min_operations(nums, k):
    total = sum(nums)
    return total % k


# -------------------------
# Test Cases
# -------------------------

tests = [
    # Provided example
    ([3, 9, 7], 5, 4),

    # Already divisible
    ([1, 2, 3], 3, 0),

    # Large numbers
    ([100, 200, 300], 7, (100+200+300) % 7),

    # Single element
    ([10], 6, 10 % 6),

    # Needs only 1 decrement
    ([4, 4], 5, (4+4) % 5),

    # All zeros
    ([0, 0, 0], 4, 0),

    # Mixed positives
    ([5, 11, 14], 6, (5+11+14) % 6),
]

for nums, k, expected in tests:
    result = min_operations(nums, k)
    print(f"nums={nums}, k={k} → {result} (expected {expected})")
