class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        return f"{self.val} -> {self.next}"


def linked_to_list(head: ListNode | None) -> list:
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res


def list_to_linked(nums: list) -> ListNode | None:
    head: ListNode | None = None
    for num in nums:
        head = ListNode(num, head)
    return head


def reverseList(head: ListNode | None) -> ListNode | None:

    reversed_linked = list_to_linked(linked_to_list(head))
    return reversed_linked


def reverseList2(head: ListNode | None) -> ListNode | None:

    #         10 -> 20 -> 30 -> 40 -> None
    # None <- 10 <- 20 <- 30 <- 40
    prev_node = None
    while head:
        next_node = head.next
        head.next = prev_node
        prev_node = head
        head = next_node
    return prev_node


print(reverseList2(ListNode(10, ListNode(20, ListNode(30)))))
