#Insertion sort.
#unsorted part -> sorted part, from left to right.
#O(n^2)

def insertion_sort(list):
    for i in range(1, len(list)):
        currentNumber = list[i]
        for j in range(i-1, -1, -1):
            if(currentNumber <= list[j] and j == 0):

                list[(j+1)] = list[j]
                list[j] = currentNumber
                break
            if(list[j] > currentNumber):
                list[j+1] = list[j]
            else:
                list[j+1] = currentNumber
                break

list = [3,2,1,4,7,6,5,9,17]

print(list)

insertion_sort(list)

print(list)
