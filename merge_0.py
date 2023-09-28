def mergeSort(unsorted_list):
    if len(unsorted_list)  <= 1:
        return unsorted_list
    middle = len(unsorted_list) // 2
    left_list = unsorted_list[:middle]
    right_list = unsorted_list[middle:]
    #print(right_list)
    left_list = mergeSort(left_list)
    right_list = mergeSort(right_list)
    
    return list(merge(left_list, right_list)[1])
def merge(left_half, right_half):
    res = []
    swap_list = []
    while len(left_half) != 0 and len(right_half) != 0:
        count = 0
        if left_half[0][0] < right_half[0][0]:
            res.append(left_half[0])
            swap_list.append([left_half[0][0], right_half[0][0]])
            print([left_half[0][0], right_half[0][0]])
            left_half.remove(left_half[0])
        else:
            swap_list.append([right_half[0][0], left_half[0][0]])
            print([right_half[0][0], left_half[0][0]])
            res.append(right_half[0])
            right_half.remove(right_half[0])
    if len(left_half) == 0:
        res = res + right_half
    else:
        res = res + left_half
    return swap_list, res
unsorted_list = [[64, 0], [34, 1], [25, 2], [12, 3], [22, 4], [11, 5], [90, 6]]
#print(mergeSort(unsorted_list))