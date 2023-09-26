class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def pairSumhead(head: ListNode | None) -> int:
    def linked_to_list(head: ListNode | None) -> list:
        res = []
        while head:
            res.append(head.val)
            head = head.next
        return res

    nums = linked_to_list(head)
    return max(nums[i] + nums[len(nums) - 1 - i] for i in range(len(nums) // 2))


print(pairSumhead(head=ListNode(10, ListNode(20, ListNode(30, ListNode(40))))))
