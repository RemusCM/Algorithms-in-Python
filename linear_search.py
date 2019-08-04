#Linear search on an unsorted list.

from sys import argv

scriptName = argv[0]

print(f"""Welcome to {scriptName}; a script that implements linear search on an
unsorted list""")

#Defining the linear search function, which needs a list, and an element to
#search for
def linear_search(list, element):
    found = False
    for x in list:
        if x == element:
            found = True #This will go through the whole list, even if found.
    return print(found)

#Same thing, but stops once method finds a hit.
def linear_search2(list, element):
    for x in list:
        if x == element:
            return print(True)
    return print(False)

#Another addition on a sorted list is to stop once the value becomes bigger
#than the value that we are searching for.
def linear_sorted(list, element):
    for x in list:
        if x == element:
            return print(True)
        if x > element:
            return print("Stopped searching, didn't find.")

    return print(False)

list = [0,1,2,3,4,5,17]

linear_search(list, 14)

linear_sorted(list, 3)
