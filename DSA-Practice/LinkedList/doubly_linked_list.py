class Node:
    def __init__(self, value) -> None:
        """constructor for the node class"""
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self, value) -> None:
        """constructor for LinkedList class"""
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def __str__(self) -> str:
        """Printing the Doubly Linked List"""
        temp = self.head
        text = ''
        while temp is not None:
            text += f"{temp.value} <=> "
            temp = temp.next
        
        return text[:-5]
    
    def append(self, value) -> bool:
        """Appending node to Doubly Linked List"""
        new_node = Node(value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
    
    def pop(self) -> Node:
        """Pop the node from teh trailing end of the Doubly Linked List"""
        if self.length == 0:
            return False
        
        temp = self.tail        
        self.tail = self.tail.prev
        self.tail.next = None
        temp.prev = None
        self.length -= 1

        if self.length == 0:
            self.head = None
            self.tail = None

        return temp
    
    def prepend(self, value) -> bool:
        """Append the node at the beginning of the Doubly Linked List"""
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True
    
    def pop_first(self) -> Node:
        """Remove the item from the beginning of the Doubly Linked List"""
        if self.length == 0:
            return None
        
        temp = self.head

        self.head = self.head.next
        self.head.prev = None
        temp.next = None
        self.length -= 1

        if self.length == 0:
            self.head = None
            self.tail = None
        return temp
    
    def get(self, index) -> Node:
        """Fetch the node from the Doubly Linked List"""
        if index < 0 or index >= self.length:
            return None
        
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
    
    def set_value(self, index, value) -> bool:
        """Setting up the intermediate value in the Doubly Linked List"""
        if index < 0 or index >= self.length:
            return False
        
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    def insert(self, index, value) -> bool:
        """Inserting the value in between the Doubly Linked List"""
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        before = self.get(index-1)
        after = before.next
        
        new_node.next = after
        new_node.prev = before
        after.prev = new_node
        before.next = new_node
        self.length += 1
        return True
    
    def remove(self, index) -> Node:
        """Remove the node from the Doubly Linked List"""
        if index < 0 or index >= self.length:
            return False
        
        if index == 0:
            return self.pop_first()
        if index == self.length-1:
            return self.pop()
        
        temp = self.get(index)

        temp.prev.next = temp.next
        temp.next.prev = temp.prev
        temp.prev = None
        temp.next = None
        self.length -= 1
        return temp
        


if __name__ == '__main__':
    dll = DoublyLinkedList(2)
    dll.append(3)
    dll.append(4)
    dll.append(5)
    dll.prepend(1)
    dll.remove(1)
    print(dll)