class Node:
    """Node class for the Binary Search Tree class"""
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        """Method to insert a node into BST"""
        new_node = Node(value)

        if self.root == None:
            self.root = new_node
        
        temp = self.root

        while True:
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right
    
    def contains(self, value):
        """Method to check the availability of the node"""
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
    bst.insert(3)
    bst.insert(1)
    bst.insert(4)

    print(bst.root.value)
    print(bst.root.left.value)
    print(bst.root.right.value)
    print(bst.root.right.right.value)

    print(bst.contains(2))

