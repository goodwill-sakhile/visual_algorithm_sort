def selectionSort(input_list):
    for i in range(len(input_list)):
        min_i = i
        for j in range(i + 1, len(input_list)):
            if input_list[min_i] > input_list [j]:
                min_i = j
        input_list[i], input_list[min_i] = input_list[min_i], input_list[i]
_list = [19, 2, 31, 45, 30, 11, 121, 27]
selectionSort(_list)
print(_list)