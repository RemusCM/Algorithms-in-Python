#linked list data structure; composed of two classes; node and linked_list
#linked list makes use of nodes.

class Node():
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Linked_List():
    #Initialize a linked list with an empty head node that will serve
    #to know where the begining of the list is.
    def __init__(self):
        self.head = Node()

    def append(self, data):
        #Make a new node filled with data, and having next as None
        new_node = Node(data)
        #Then, we need to start at the begining and iterate through
        #all elements until we find that the node.next == None, to replace None
        #with this node.
        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next
        current_node.next = new_node

    def insert(self, data, index):
        current_node = self.head;
        if (index >= self.get_length()):
            print("ERROR: Out of bounds")
        else:
            counter = 0
            while counter != index:
                counter += 1
                current_node = current_node.next
            new_node = Node(data)
            temp_node = current_node.next
            current_node.next = new_node
            new_node.next = temp_node




    def get_length(self):
        current_node = self.head
        total = 0
        while current_node.next != None:
            total += 1
            current_node = current_node.next
        return total

    def get_list(self):
        current_node = self.head
        list = []
        while current_node.next != None:
            current_node = current_node.next
            list.append(current_node.data)#append only data, not the whole node.
        return list

    def get(self, index):
        if index >= self.get_length():
            return "Error: Out of bounds."
        else:
            counter = 0
            current_node = self.head.next
            while counter != index:
                counter += 1
                current_node = current_node.next
            return current_node.data

    def remove(self, index):
        if index >= self.get_length():
            print("Error: Out of Bounds")
            return None
        current_node = self.head
        counter = 0
        while counter != index:
            counter += 1
            current_node = current_node.next
        #We arrive at the point to delete.
        #we save in another variable the new connection
        current_node.next = (current_node.next).next



my_list = Linked_List()

print(my_list.get_list())

my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.insert(5,2)
my_list.insert(5,2)
my_list.append(6)

print(my_list.get_list())

print(my_list.get(0))
print(my_list.get(1))
print(my_list.get(2))
print(my_list.get(3))

my_list.remove(0)
print(my_list.get_list())
my_list.remove(1)
my_list.remove(1)


print(my_list.get_list())


print("""Here's a problem: Imagine you have a linked list. How would you be able
to know whether or not there is a loop within a linked list. (get_length wouldn't
work.) TIP: Use a next() and next2() methods <- jumps 2""")
