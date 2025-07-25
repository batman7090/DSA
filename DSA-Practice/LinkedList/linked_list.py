class Node:
    def __init__(self, value) -> None:
        """constructor for the node class"""
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value) -> None:
        """constructor for LinkedList class"""
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def __str__(self) -> str:
        """Printing the Linked List"""
        temp = self.head
        text = ''
        while temp is not None:
            text += f"{temp.value} -> "
            temp = temp.next
        
        return text[:-4]
    
    def append(self, value) -> bool:
        """Appending node to Linked List"""
        new_node = Node(value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True
    
    def pop(self) -> Node:
        """Pop the node from teh trailing end of the Linked List"""
        if self.length == 0:
            return False
        
        temp = self.head
        pre = self.head

        while temp.next:
            pre = temp
            temp = temp.next
        
        self.tail = pre
        self.tail.next = None
        self.length -= 1

        if self.length == 0:
            self.head = None
            self.tail = None

        return temp
    
    def prepend(self, value) -> bool:
        """Append the node at the beginning of the Linked List"""
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True
    
    def pop_first(self) -> Node:
        """Remove the node from the beginning of the Linked List"""
        if self.length == 0:
            return None
        
        temp = self.head

        self.head = self.head.next
        temp.next = None
        self.length -= 1

        if self.length == 0:
            self.head = None
            self.tail = None
        return temp
    
    def get(self, index) -> Node:
        """Fetch the node from the Linked List"""
        if index < 0 or index >= self.length:
            return None
        
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
    
    def set_value(self, index, value) -> bool:
        """Setting up the intermediate node node in the Linked List"""
        if index < 0 or index >= self.length:
            return False
        
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    def insert(self, index, value) -> bool:
        """Inserting the node in between the Linked List"""
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index-1)
        if temp:
            new_node.next = temp.next
            temp.next = new_node
            self.length += 1
            return True
        return False
    
    def remove(self, index) -> Node:
        """Remove the node from the Linked List"""
        if index < 0 or index >= self.length:
            return False
        
        if index == 0:
            return self.pop_first()
        if index == self.length-1:
            return self.pop()
        
        pre = self.get(index-1)
        temp = pre.next

        pre.next = temp.next
        temp.next = None
        self.length -= 1
        return temp
        


if __name__ == '__main__':
    ll = LinkedList(2)
    ll.append(3)
    ll.append(4)
    ll.prepend(1)
    ll.insert(1,5)
    ll.remove(1)
    print(ll)