class Node:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add(self, data):
        self.children.append(Node(data))

    def remove_child_node(self, data):
        if self.data == data:
            print("Equal to root node")
        else:
            count = 0
            for i in self.children:
                if i.data == data:
                    index = count
                count += 1
            self.children.pop(index)


    def traverse(self):
        print(self.data)
        for i in self.children:
            print(i.data)

    def traverse_bfs(self):
        childs = self.children
        my_list = []
        my_list.append(childs)
        for child in my_list:
            print(child.data)
            nodes.remove(child)




class Tree:
    def __init__(self):
        self.root = None

n = Node(200)
n.add(150)
n.add(100)
n.add(50)
n.add(00)
n.traverse()
n.remove_child_node(100)
n.traverse()
