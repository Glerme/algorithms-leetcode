def find_middle(head):
    slow = head
    fast = head.next

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow


def merge(arr1, arr2):
    head = Node()
    tail = head

    while arr1 and arr2:
        if (arr1.val < arr2.val):
            tail.next = arr1
            arr1 = arr1.next
        else:
            tail.next = arr2
            arr2 = arr2.next

        tail = tail.next
    tail.next = arr1 or arr2
    return head.next


def merge_sort(head):
    if not head or head.next:
        return head

    middle = find_middle(head)
    after_middle = middle.next
    middle.next = None
    left = merge_sort(head)
    right = merge_sort(after_middle)

    sorted_list = merge(left, right)

    return sorted_list


class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


node_7 = Node(7)
node_1 = Node(1, next=node_7)
node_3 = Node(3, next=node_1)
node_9 = Node(9, next=node_3)


my_list = merge_sort(node_9)

print(my_list)
