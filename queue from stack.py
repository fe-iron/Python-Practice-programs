from stack import Stack
from queue import Queue


def queue_from_stack(stac2, stac):

    que_temp = Queue()

    while stac2.peak() or stac.peak():
        if stac.peak():
            que_temp.add(stac.pop())
        elif stac2.peak():
            que_temp.add(stac2.pop())

    que_temp.add(15)

    print("The new Queue from the two stacks are: {}".format(que_temp.data))


if __name__ == "__main__":
    sta1 = Stack()
    sta2 = Stack()

    sta1.push(12)
    sta1.push(22)
    sta1.push(32)

    sta2.push(22)
    sta2.push(32)
    sta2.push(42)

    print("Stack Now: {}".format(sta1.data))
    sta1.pop()
    print("After pop, Queue Now: {}".format(sta1.data))

    print("Stack Now: {}".format(sta2.data))
    sta2.pop()
    print("After POP, Stack Now: {}".format(sta2.data))

    queue_from_stack(sta1, sta2)

