class Node:
    def __init__(self, value):
        self.value = value
        self.next = None # pointer to the next neighbour

class LinkedList:
    def __init__(self):
        self.head = None # entry point to the list

    def append(self, value):
        """Adds a node to the end of the list: O(n) time"""
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        
        # walk from heaad to the very last node
        current = self.head
        while current.next:
            current = current.next
        
        current.next = new_node
    
    def print_list(self):
        """Traverses and prints the list: O(n) time"""
        current = self.head
        elements = []
        while current:
            elements.append(str(current.value))
            current = current.next
        print(" -> ".join(elements) + " -> None")

    def reverse(self):
        """Reverses the list: O(n) time"""
        prev = None
        curr = self.head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        self.head = prev

    def has_cycle(self):
        """Detectes if the list has a cycle: O(n) time"""
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True
        return False

# Test
# ll = LinkedList()
# ll.append(1)
# ll.append(2)
# ll.append(3)
# ll.append(4)
# ll.print_list()

# To test reverse method
# ll.reverse()
# ll.print_list()

# To test has_cycle method
# ll = LinkedList()
# ll.append(1)
# ll.append(2)
# ll.append(3)
# ll.append(4)

# # Manually creating a cycle: 4 -> 2
# node4 = ll.head.next.next.next
# node2 = ll.head.next
# node4.next = node2 

# print(ll.has_cycle()) # Should return True