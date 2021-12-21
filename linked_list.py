import math

class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insertFirst(self, data):
        self.head = Node(data, self.head)

    def size(self):
        counter = 0
        node = self.head
        while node:
            counter += 1
            node = node.next
        print("The size is {}".format(counter))

    def getFirst(self):
        if self.head:
            print("The first node's data is: {}".format(self.head.data))
        else:
            print("Linked list is empty")

    def getLast(self):
        node = self.head
        while node:
            if not node.next:
                print("The Last is {}".format(node.data))
            node = node.next

    def removeFirst(self):
        self.head = self.head.next

    def removeLast(self):
        node = self.head
        if not self.head:
            print("Linked List is Empty!")
            return

        if not self.head.next:
            self.head = None
            return

        previous = self.head
        next_node = self.head.next

        while next_node.next:
            previous = next_node
            next_node = next_node.next
        previous.next = None
        return

    def insertLast(self, data):
        node = self.head

        previous = self.head
        next_node = self.head.next

        while next_node:
            previous = next_node
            next_node = next_node.next

        last_node = Node(data)
        previous.next = last_node

    def nodeAt(self, index):
        temp_node = self.head
        count = 0
        while temp_node:
            count += 1
            if count == index:
                return temp_node
            temp_node = temp_node.next
        return None

    def removeAt(self, index):
        if index == 0:
            self.head = self.head.next
        previous = self.nodeAt(index - 1)
        if not previous or not previous.next:
            return
        previous.next = previous.next.next

    def insertAt(self, index, data):
        if not self.head:
            new_node = Node(data)
            self.head = new_node
            return 1
        prev_node = self.nodeAt(index - 1)
        if not prev_node:
            return 0
        next_ref = prev_node.next
        new_node = Node(data, next_ref)
        prev_node.next = new_node
        return 1

    def traverse(self):
        temp_node = self.head
        linked_list = []
        while temp_node:
            linked_list.append(temp_node.data)
            temp_node = temp_node.next
        return linked_list

    def midElemet(self):
        linked_list = self.traverse()
        print(linked_list)
        l = len(linked_list)
        midpoint =  math.ceil(l//2)
        for linked in linked_list:
            yield linked_list[midpoint]


    def isLoop(self):
        slow = fast = self.head

        while fast:
            slow = slow.next
            if fast.next.next:
                return False
            else:
                fast = fast.next.next
            if slow == fast:
                return True

        return False


def fromLast(lk, index):
    if index == 0:
        lk.getLast()
        return

    slow = fast = lk.head
    i = 1
    while fast.next:
        if i <= index:
            fast = fast.next
        else:
            slow = slow.next
            fast = fast.next
        i += 1
    return slow.data


lk = LinkedList()
lk.insertFirst("Faiz ")
lk.insertFirst("Elahi ")
lk.insertFirst("is ")
lk.insertFirst("Programmer/Developer ")
lk.size()
# lk.getFirst()
# lk.getLast()
# lk.removeFirst()
# lk.getFirst()
# lk.removeLast()
# lk.getLast()
lk.insertLast("Papa Fans")
lk.size()
temp_node = lk.nodeAt(5)
print(temp_node.data)
lk.removeAt(2)
lk.size()
lk.insertAt(2, "instaholic")
lk.size()
lk.traverse()
lk.midElemet()
print("is there a loop in linked list ",lk.isLoop())
print(fromLast(lk, 1))