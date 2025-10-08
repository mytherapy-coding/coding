def merge_sort(nums: list) -> list:

    if len(nums) <= 1:  # Base case
        return nums

    half_array = len(nums) // 2
    left_sorted = merge_sort(nums[:half_array])
    right_sorted = merge_sort(nums[half_array:])


    def merge_sorted_lists(a, b):
    # [10, 20, 30]
    # [15, 50]
        i = 0
        j = 0
        while i < len(a) and j < len(b):
            if a[i] < b[j]:
                yield a[i]
                i += 1
            else:
                yield b[j]
                j += 1
        
        assert i >= len(a) or j >= len(b)

        while i < len(a):
            yield a[i]
            i+=1
        while j < len(b):
            yield b[j]
            j+=1

    return list(merge_sorted_lists(left_sorted, right_sorted))
    
   
def test_merge_sort():
    # Test empty list
    assert merge_sort([]) == []

    # Test single element
    assert merge_sort([42]) == [42]

    # Test already sorted list
    assert merge_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

    # Test reverse sorted list
    assert merge_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

    # Test list with duplicates
    assert merge_sort([3, 1, 2, 3, 1]) == [1, 1, 2, 3, 3]

    # Test list with negative numbers
    assert merge_sort([-2, 5, 0, -1, 3]) == [-2, -1, 0, 3, 5]

    # Test list with all equal elements
    assert merge_sort([7, 7, 7, 7]) == [7, 7, 7, 7]

    print("All tests passed!")

# Run the tests
if __name__ == '__main__':
    test_merge_sort()

