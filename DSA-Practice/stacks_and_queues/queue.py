class Node:
    def __init__(self, value):
        """Node class constructor"""
        self.value = value
        self.next = None

class Queue:
    def __init__(self, value):
        """Queue class constructor"""
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1
    
    def __str__(self):
        temp = self.first
        text = ''
        while temp is not None:
            text += f"{temp.value} -> "
            temp = temp.next
        
        return text[:-4]
    
    def enqueue(self, value):
        """Adding the node to Queue"""
        new_node = Node(value)
        if self.length == 0:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1
        return True
    
    def dequeue(self):
        """Removing the node from Queue"""
        if self.length == 0:
            return False
        
        temp = self.first
        self.first = self.first.next
        temp.next = None
        self.length -= 1

        if self.length == 0:
            self.first = None
            self.last = None
        return temp
    
if __name__ == '__main__':
    q = Queue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.dequeue()
    print(q)
