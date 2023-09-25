class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        # return f'({self.val},{self.next})'
        return f'{self.val} -> {self.next}'


def linked_list_size(head: ListNode | None) -> int:
    size = 0
    while head:
        size += 1
        head = head.next
    return size


def linked_list_get(head: ListNode | None, ind: int) -> ListNode | None:
    while head:
        if ind == 0:
            break
        head = head.next
        ind -= 1

    return head


def linked_list_remove(prev_node: ListNode | None) -> None:
    prev_node.next = prev_node.next.next


def deleteMiddle(head: ListNode|None) -> ListNode|None:
    '''
    - count nodes
    - ind_to_del = n//2
    - find a node to delete using this index
    - deletion this node
    '''
    size = linked_list_size(head)
    if size <= 1:
        return None
    ind = size // 2 - 1
    middle = linked_list_get(head, ind)
    linked_list_remove(middle)
    return head


node1 = ListNode(10)
node2 = ListNode(20)
node3 = ListNode(30)
node1.next = node2
node2.next = node3

assert linked_list_size(None) == 0
assert linked_list_size(node3) == 1
assert linked_list_size(node2) == 2
assert linked_list_size(node1) == 3


assert linked_list_get(None, 0) == None
assert linked_list_get(node1, 0) == node1
assert linked_list_get(node1, 1) == node2
assert linked_list_get(node1, 2) == node3
assert linked_list_get(node1, 3) == None
print(node1)
print(deleteMiddle(node1))
