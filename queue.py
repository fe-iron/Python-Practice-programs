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


if __name__ == "__main__":
    queue = Queue()
    queue.add(123)
    queue.add(13)
    queue.add(18)
    queue.add(17)
    print("List Now: {}".format(queue.data))
    queue.remove()
    queue.remove()
    print("List Now: {}".format(queue.data))
