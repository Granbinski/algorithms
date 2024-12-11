class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def add_to_front(self, value):
        new_node = Node(value)
        new_node.next = self.head
        if self.head:
            self.head.prev = new_node
        else:
            self.tail = new_node
        self.head = new_node
    
    def add_to_end(self, value):
        new_node = Node(value)
        new_node.prev = self.tail
        if self.tail:
            self.tail.next = new_node
        else:
            self.head = new_node
        self.tail = new_node
    
    def remove_from_front(self):
        if self.head:
            removed = self.head
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            else:
                self.tail = None
            return removed.value
        return None
    
    def remove_from_end(self):
        if self.tail:
            removed = self.tail
            self.tail = self.tail.prev
            if self.tail:
                self.tail.next = None
            else:
                self.head = None
            return removed.value
        return None
    
    def display_forward(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")
    
    def display_backward(self):
        current = self.tail
        while current:
            print(current.value, end=" -> ")
            current = current.prev
        print("None")

# Teste da implementação
if __name__ == "__main__":
    dll = DoublyLinkedList()
    
    # Adiciona elementos
    dll.add_to_front(3)
    dll.add_to_front(2)
    dll.add_to_end(4)
    dll.add_to_end(5)
    
    print("Lista original:")
    dll.display_forward()
    dll.display_backward()
    
    # Remove elementos
    dll.remove_from_front()
    dll.remove_from_end()
    
    print("\nLista após remoções:")
    dll.display_forward()
    dll.display_backward()