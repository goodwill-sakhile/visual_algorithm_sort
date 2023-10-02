def insertionSort(input_list):
    swap_list = []
    for i in range(1, len(input_list)):
        j =i - 1
        next_element = input_list[i][0]
        while (input_list[j][0] > next_element) and (j >= 0):
            input_list[j+1][0] = input_list[j][0]
            swap_list.append([i, j])
            j = j - 1
        input_list[j+1][0] = next_element
    print(swap_list)
list = [[19, 0], [2, 1], [31, 2], [43, 3], [30, 4], [11, 5], [121, 6], [27, 7]]
insertionSort(list)
print(list)