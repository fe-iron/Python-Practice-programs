class Stack:
    def __init__(self):
        this.data = []

    def push(self, dat):
        self.data.append(dat)

    def pop(self):
        return self.data.pop()

    def peak(self):
        try:
            return self.data[len(self.data) - 1]
        except IndexError:
            return 0



if __name__ == "__main__":
    stack = Stack()
    stack.push(123)
    stack.push(2234)
    stack.push(1)
    print("List Now: {}".format(stack.data))
    stack.pop()
    stack.pop()
    print("List Now: {}".format(stack.data))
    print("PEAK Now: {}".format(stack.data))
