class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f"{self.val} -> {self.next}"


def list_to_linked(nums: list) -> ListNode | None:
    head = None
    for num in reversed(nums):
        head = ListNode(num, head)
    return head


def linked_to_list(head: ListNode | None) -> list:
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res


def oddEvenList(head: ListNode | None) -> ListNode | None:
    nums = linked_to_list(head)
    odd_ind = [num for i, num in enumerate(nums) if i % 2 == 0]
    even_ind = [num for i, num in enumerate(nums) if i % 2 == 1]
    res = odd_ind + even_ind
    return list_to_linked(res)


def tests():
    nums = [100, 200, 300, 400, 500]
    print(list_to_linked(nums))
    print()
    head = list_to_linked(nums)
    print(linked_to_list(head))
    assert linked_to_list(head) == nums


# tests()


def oddEvenList2(head: ListNode | None) -> ListNode | None:
    if not head:
        return None
    even_last: ListNode | None = None
    odd_last: ListNode | None = None
    even_head = head
    odd_head = head.next
    while head:
        if even_last:
            even_last.next = head
        even_last = head
        head = head.next
        if not head:
            break
        if odd_last:
            odd_last.next = head
        odd_last = head
        head = head.next

    even_last.next = odd_head
    if odd_last:
        odd_last.next = None
    return even_head


head = list_to_linked([10, 20, 30, 40, 50, 60, 70])
print(oddEvenList2(head))
print(oddEvenList2(list_to_linked([])))
print(oddEvenList2(list_to_linked([100])))
print(oddEvenList2(list_to_linked([100, 200])))
print(oddEvenList2(list_to_linked([100, 200, 300])))
