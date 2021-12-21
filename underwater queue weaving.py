class Queue:
    def __init__(self):
        self.data = []

    def add(self, dat):
        self.data.insert(0, dat)

    def remove(self):
        return self.data.pop()

    def peak(self):
        try:
            return self.data[len(self.data) - 1]
        except IndexError:
            return 0


def weave(q1, q2):
    q3 = Queue()
    while q1.peak() or q2.peak():
        if q1.peak():
            q3.add(q1.remove())
        if q2.peak():
            q3.add(q2.remove())

    return q3


if __name__ == "__main__":
    queue1 = Queue()
    queue1.add(123)
    queue1.add(13)
    queue1.add(18)
    queue1.add(17)
    print("Queue1 Now: {}".format(queue1.data))
    queue2 = Queue()
    queue2.add(13)
    queue2.add(131)
    queue2.add(181)
    queue2.add(181)
    queue2.add(181)
    queue2.add(179)
    print("Queue2 Now: {}".format(queue2.data))
    queue2.remove()
    queue2.remove()
    print("Queue2 Now: {}".format(queue2.data))
    queue1.remove()
    # queue1.remove()
    queue1.remove()
    print("Queue1 Now: {}".format(queue1.data))
    queue3 = weave(queue1, queue2)
    print("Queue3 Now: {}".format(queue3.data))

