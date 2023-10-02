def selectionSort(input_list):
    swap_list = []
    for i in range(len(input_list)):
        min_i = i
        for j in range(i + 1, len(input_list)):
            if input_list[min_i][0] > input_list [j][0]:
                min_i = j
        input_list[i][0], input_list[min_i][0] = input_list[min_i][0], input_list[i][0]
        swap_list.append([i, min_i])
_list = [[19, 0], [2, 1], [31, 2], [45, 3], [30, 4], [11, 5], [121, 6], [27, 7]]
selectionSort(_list)
print(_list)