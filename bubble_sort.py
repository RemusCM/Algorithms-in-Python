#Bubble sort algorithm
#Pass through the list n times. Verify every two elements to see if in
#correct order. Otherwise, need to swap.
#O()

list = [17,13,2,19,23,27,5555,111,77,1,3]

print(list)

def bubble_sort(list):
    swap = False
    for x in list:
        #need to figure out a way to use len(list), without the -1.
        for j in range(0, len(list)-1):
            if (list[j] > list[j+1]):
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp

bubble_sort(list)

print(list)
