class Node():
    def __init__(self, data = None):
        self.data = data
        self.next = None
        self.previous = None

class Doubly_Linked_List():
    def __init__(self):
        self.head = Node()

        #function that adds a new node at the end of a linked list
    def append(self, data):
        new_node = Node(data)
        current_node = self.head

        #iterate until current.next == None.
        while current_node.next != None:
            current_node = current_node.next

        temp_node = current_node
        current_node.next = new_node
        new_node.previous = current_node


        #function that adds at the begining of the linked list
    def prepend(self, data):
        if(self.get_length == 0):
            self.append(data)

        else:
            new_node = Node(data)
            new_node.previous = self.head
            temp_node = self.head.next
            new_node.next = temp_node
            self.head.next = new_node
            temp_node.previous = new_node


    def get_list(self):
        current_node = self.head
        list = []
        while current_node.next != None:
            list.append((current_node.next).data)
            current_node = current_node.next

        return list

    def get(self, index):
        if(index >= self.get_length()):
            print("ERROR: Out of bounds")
            return None
        else:
            counter = 0
            current_node = self.head.next
            while counter != index:
                counter += 1
                current_node = current_node.next
            return current_node.data

    def get_length(self):
        current_node = self.head
        total = 0
        while current_node.next != None:
            total += 1
            current_node = current_node.next

        return total

    def remove(self, index):
        if(index >= self.get_length()):
            print("ERROR: Out of bounds")
            return None
        else:
            current_node = self.head.next
            counter = 0
            while(counter != index):
                counter += 1
                current_node = current_node.next

            previous_node = current_node.previous
            next_node = current_node.next
            previous_node.next = next_node
            next_node.previous = previous_node


    def is_empty(self):
        return (self.head.next == None)

my_list = Doubly_Linked_List()
print(my_list.get_list())
print(my_list.get_length())
print(my_list.is_empty())
my_list.append(1)
my_list.append(2)
print(my_list.get_list())
print(my_list.get_length())
print(my_list.is_empty())
my_list.prepend(3)
my_list.prepend(5)
print(my_list.get(2))
print(my_list.get_list())
my_list.remove(2)
print(my_list.get_list())
