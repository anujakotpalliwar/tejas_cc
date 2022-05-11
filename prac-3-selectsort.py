def findLocalMinimum(start, end, array):
    #print(1, start, end)
    minimum = array[start]
    index = start
    # print(start,end)
    for i in range(start+1, end):
        if(array[i] < array[start]):
            minimum = array[i]
            index = i
            break

    return (minimum, index)


def selectionSortG(array):
    for i in range(len(array)):
        minimum, index = findLocalMinimum(i, len(array), array)
        temp = array[i]
        array[i] = minimum
        array[index] = temp
        print(array)


print('Enter elements of array: ')
array = [int(i) for i in input().split()]
print("-------INPUT ARRAY----------")
print(array)
print("------SORTED ARRAY AFTER GREEDY SELECTION SORT------")
selectionSortG(array)
