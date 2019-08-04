#Merge sort, divde and conquer method.
#if length 0 or 1, already sorted.
#if more than two, divde into two lists and sort each
#merge sorted sublists.
#We need to make a merge helper function, along with a merge_sort function.
#This algortihm uses recursion.
#O(nlogn)

#helper function to merge sorted arrays.
def merge(left, right, array):
    i, j, k = 0, 0, 0
    while(i < len(left) and j < len(right)):
        if(left[i] <= right[j]):
            array[k] = left[i]
            i += 1
            k += 1
        else:
            array[k] = right[j]
            j += 1
            k += 1


    while(i < len(left)):
        array[k] = left[i]
        i += 1
        k += 1

    while(j < len(right)):
        array[k] = right[j]
        j += 1
        k += 1

def merge_sort(array):
    if(len(array) < 2):
        return array
    else:
        midpoint = len(array)//2 # // is floor division
        left = array[:midpoint] #way to splice array, doesn't include last element if specified
        right = array[midpoint:]

    merge_sort(left)
    merge_sort(right)
    merge(left, right, array)


list = [9,6,5,3,10,17,11,2,1,2]

print(list)

merge_sort(list)

print(list)
