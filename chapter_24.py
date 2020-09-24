class Node:
    def __init__(self, cargo=None, next=None):
        self.cargo = cargo
        self.next = next

    def __str__(self):
        return str(self.cargo)


node1 = Node(1)
node2 = Node(2)
node3 = Node(3)

node1.next = node2
node2.next = node3


def print_list(node):
    print("[", end ="")
    while node is not None:
        print("{0},".format(node), end=" ")
        node = node.next
    print("]")

# pooja/lokesh's code
def print_list2(node):
    list = []
    while node is not None:
        list.append(node.cargo)
        node = node.next
    print(list)


# def print_list(node):
#     list = []
#     while node is not None:
#         list.append(node)
#         for i in list:
#             print(i)
#         print("{0},".format(node), end=" ")
#         node = node.next
#     print("]")



# print_list(node1)


def print_backward(list):
    if list is None: return
    head = list
    tail = list.next
    print_backward(tail)
    print(head, end=" ")

# print_backward(node1)
# print_list2(node1)
