#Selection sort algorithm
#Go through the list, pick min value.
#swap with current index
#O(n^2)

list = [17,13,2,19,23,27,5555,111,77,1,3]

print(list)

def selection_sort(list):
    #Don't forget that in range(min, max), max is not included in the forloop
    for i in range(0, len(list)):
        current_min = list[i]
        index = i
        for j in range(i+1, len(list)):
            if (current_min > list[j]):
                current_min = list[j]
                index = j
        tempVal = list[i]

        list[i] = current_min
        list[index] = tempVal

selection_sort(list)

print(list)
