class Node:
    def __init__(self, value):
        """Node class constructor"""
        self.value = value
        self.next = None

class Stack:
    def __init__(self, value):
        """Stack class constructor"""
        new_node = Node(value)
        self.top = new_node
        self.height = 1
    
    def __str__(self):
        temp = self.top
        text = ''
        while temp is not None:
            text += f"{temp.value} -> "
            temp = temp.next
        
        return text[:-4]
    
    def push(self, value):
        """Adding the node to Stack"""
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height += 1
        return True
    
    def pop(self):
        """Removing the node from stack"""
        if self.height == 0:
            return False
        
        temp = self.top
        self.top = self.top.next
        temp.next = None
        self.height -= 1

        if self.height == 0:
            self.top = None

        return temp
    
if __name__ == '__main__':
    s = Stack(1)
    s.push(2)
    s.push(3)
    s.pop()
    print(s)
