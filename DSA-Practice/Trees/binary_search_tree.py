class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)

        if self.root is None:
            self.root = new_node
            return True
        
        temp = self.root
        while True:
            if temp.value == new_node.value:
                return False
            
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                temp = temp.right
    
    def contains(self, value):
        if self.root is None:
            return False
        
        temp = self.root
        while temp is not None:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True

        return False 

if __name__ == '__main__':
    bst = BinarySearchTree()
    bst.insert(2)
    bst.insert(1)
    bst.insert(3)
    bst.insert(2)
    bst.insert(5)

    print(bst.contains(5))

    print(bst.root.value)
    print(bst.root.left.value)
    print(bst.root.right.value)