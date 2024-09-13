# class Node:
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
# class LinkedList:
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def make_empty(self):
        self.head = None
        self.tail = None
        self.length = 0
      
    def print_list(self):
        temp = self.head
        for _ in range(self.length):
            print(temp.value)
            temp = temp.next
          
    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def pop(self):
        if self.length == 0:
            return None
        if self.length == 1:
            node = self.head
            node.next = None
            self.head = None
            self.tail = None
            self.length = 0
        else:   
            temp = self.head
            while temp.next.next:
                temp = temp.next
            temp.next = None
            node = self.tail
            self.length -=1
            self.tail = temp
            if self.length == 0:
              self.head = None
              self.tail = None
        return node

    def prepend(self, value):
        
        new_node = Node(value)
        if self.length == 0: 
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length +=1
        return True

    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        self.head = temp.next
        temp.next = None
        self.length -=1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp
        

    

'''LL: Constructor
You are tasked with implementing a basic data structure: a singly linked list.  
To accomplish this, you will create two classes, Node and LinkedList.  
The Node class will represent an individual node within the linked list, while the LinkedList class will manage the overall list structure.  
Your implementation should satisfy the following requirements:
Create a Node class with the following features:
A constructor that takes a value as an argument and initializes the value attribute of the node.
A next attribute, initialized to None, which will store a reference to the next node in the list.
Create a LinkedList class with the following features:
A constructor that takes a value as an argument, creates a new Node with that value, and initializes the head and tail attributes of the linked list to point to the new node.
A length attribute, initialized to 1, which represents the current number of nodes in the list.'''

'''LL: Print List
Implement a method print_list(self) that prints the linked list's elements, one per line.'''

my_linked_list = LinkedList(4)

print('Head:', my_linked_list.head.value)
print('Tail:', my_linked_list.tail.value)
print('Length:', my_linked_list.length)

'''
LL: Append
Implement the append method for the LinkedList class.
The append method should add a new node with a given value to the end of the linked list, updating the tail attribute and the length attribute accordingly.
Keep in mind the following requirements:
The method should handle the cases where the list is empty and where the list already has one or more nodes.
The method should create a new node with the given value and add it to the end of the list.
The method should update the tail attribute of the LinkedList correctly.
The method should update the length attribute of the LinkedList to reflect the addition of the new node.'''


"""
    EXPECTED OUTPUT:
    ----------------
    Head: 4
    Tail: 4
    Length: 1
    
"""

my_linked_list = LinkedList(1)
my_linked_list.make_empty()

my_linked_list.append(1)
my_linked_list.append(2)

print('Head:', my_linked_list.head.value)
print('Tail:', my_linked_list.tail.value)
print('Length:', my_linked_list.length, '\n')

print('Linked List:')
my_linked_list.print_list()



"""
    EXPECTED OUTPUT:
    ----------------
    Head: 1
    Tail: 2
    Length: 2 

    Linked List:
    1
    2
    
"""
'''
LL: Pop
Your task is to implement the pop method for the LinkedList class.
The pop method should remove the last node (tail) from the linked list and return the removed node. If the list is empty, the method should return None.
After the last node is removed, the second-to-last node should become the new tail of the list.
Additionally, if the list becomes empty after the pop operation, both the head and tail attributes should be set to None.
Keep in mind the following requirements:
The method should handle the cases where the list is empty, has only one node, or has multiple nodes.
The method should update the tail attribute of the LinkedList correctly.
The method should update the length attribute of the LinkedList to reflect the removal of the node.
The method should either return the removed node or None if the list is empty.'''
##########################################################   
##   Test code below will print output to "User logs"   ##
##########################################################

def check(expect, actual, message):
    print(message)
    print("EXPECTED:", expect)
    print("RETURNED:", actual)
    print("PASS" if expect == actual else "FAIL", "\n")

print("\n----- Test: Pop on linked list with one node -----\n")
linked_list = LinkedList(1)
linked_list.print_list()
popped_node = linked_list.pop()
check(1, popped_node.value, "Value of popped node:")
check(None, linked_list.head, "Head of linked list:")
check(None, linked_list.tail, "Tail of linked list:")
check(0, linked_list.length, "Length of linked list:")

print("\n----- Test: Pop on linked list with multiple nodes -----\n")
linked_list = LinkedList(1)
linked_list.append(2)
linked_list.append(3)
linked_list.print_list()
popped_node = linked_list.pop()
check(3, popped_node.value, "Value of popped node:")
check(1, linked_list.head.value, "Head of linked list:")
check(2, linked_list.tail.value, "Tail of linked list:")
check(2, linked_list.length, "Length of linked list:")

print("\n----- Test: Pop on empty linked list -----\n")
linked_list = LinkedList(1)
linked_list.head = None
linked_list.tail = None
linked_list.length = 0
popped_node = linked_list.pop()
check(None, popped_node, "Popped node from empty linked list:")
check(None, linked_list.head, "Head of linked list:")
check(None, linked_list.tail, "Tail of linked list:")
check(0, linked_list.length, "Length of linked list:")

print("\n----- Test: Pop all -----\n")
linked_list = LinkedList(1)
linked_list.append(2)
linked_list.print_list()
popped_node = linked_list.pop()
check(2, popped_node.value, "Value of popped node (first pop):")
check(1, linked_list.head.value, "Head of linked list (after first pop):")
check(1, linked_list.tail.value, "Tail of linked list (after first pop):")
check(1, linked_list.length, "Length of linked list (after first pop):")
popped_node = linked_list.pop()
check(1, popped_node.value, "Value of popped node (second pop):")
check(None, linked_list.head, "Head of linked list (after second pop):")
check(None, linked_list.tail, "Tail of linked list (after second pop):")
check(0, linked_list.length, "Length of linked list (after second pop):")
popped_node = linked_list.pop()
check(None, popped_node, "Popped node from empty linked list (third pop):")
check(None, linked_list.head, "Head of linked list (after third pop):")
check(None, linked_list.tail, "Tail of linked list (after third pop):")
check(0, linked_list.length, "Length of linked list (after third pop):")

'''
LL: Prepend
Implement the prepend method for the LinkedList class.
The prepend method should add a new node with a given value to the beginning of the linked list, updating the head attribute and the length attribute accordingly.
Keep in mind the following requirements:
The method should handle the cases where the list is empty and where the list already has one or more nodes.
The method should create a new node with the given value and add it to the beginning of the list.
The method should update the head attribute of the LinkedList correctly.
The method should update the length attribute of the LinkedList to reflect the addition of the new node.
The method should return True if the operation is successful.
'''
my_linked_list = LinkedList(2)
my_linked_list.append(3)

print('Before prepend():')
print('----------------')
print('Head:', my_linked_list.head.value)
print('Tail:', my_linked_list.tail.value)
print('Length:', my_linked_list.length, '\n')
print('Linked List:')
my_linked_list.print_list()


my_linked_list.prepend(1)


print('\n\nAfter prepend():')
print('---------------')
print('Head:', my_linked_list.head.value)
print('Tail:', my_linked_list.tail.value)
print('Length:', my_linked_list.length, '\n')
print('Linked List:')
my_linked_list.print_list()



"""
    EXPECTED OUTPUT:
    
    Before prepend():
    ----------------
    Head: 2
    Tail: 3
    Length: 2 

    Linked List:
    2
    3


    After prepend():
    ---------------
    Head: 1
    Tail: 3
    Length: 3 

    Linked List:
    1
    2
    3   

"""

'''
LL: Pop First
Implement the pop_first method for the LinkedList class.
The pop_first method should remove the first node (the head) from the linked list, update the head attribute and the length attribute accordingly, and return the removed node.
Keep in mind the following requirements:
The method should handle the cases where the list is empty and where the list has one or more nodes.
The method should save a reference to the current head node before updating the head attribute.
The method should update the head attribute to the second node in the list.
The method should disconnect the removed node from the list by setting its next attribute to None.
The method should update the length attribute of the LinkedList to reflect the removal of the node.
If the list becomes empty after removing the node, the method should set the tail attribute of the LinkedList to None.
The method should return the removed node, or None if the list is empty.'''
my_linked_list = LinkedList(2)
my_linked_list.append(1)


# (2) Items - Returns 2 Node
print(my_linked_list.pop_first().value)
# (1) Item -  Returns 1 Node
print(my_linked_list.pop_first().value)
# (0) Items - Returns None
print(my_linked_list.pop_first())



"""
    EXPECTED OUTPUT:
    ----------------
    2
    1
    None

"""
