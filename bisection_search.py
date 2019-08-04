#This script is to demonstrate bisection search on a sorted list,
#which takes a list picks an index (say half). If l[I]> e, look left, else right.

list = [1,3,6,9,12,13,15,17,111,234,543]
print(list)

search_for = int(input("> Input a number to look for in that list."))

def bisection_search(list, element, low, high):
    midpoint = int((low+high)/2)

    if(list[midpoint] == element):
        return print(f"Found at index {midpoint}")
    if(low == midpoint and list[low] != element):
        return print("Does not exist in the sorted list.")    
    if(list[midpoint] > element): #look at left
        bisection_search(list, element, low, midpoint)
    if(list[midpoint] < element): #look at right
        if(midpoint == (high-1)):
            if(list[high] == element):
                return print(f"Found at index {high}")
            else:
                return print(f"Not found.")
        bisection_search(list, element, midpoint, high)


bisection_search(list, search_for, 0, (len(list)-1))
