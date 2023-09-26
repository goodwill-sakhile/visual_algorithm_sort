def insertionSort(input_list):
    for i in range(1, len(input_list)):
        j =i - 1
        next_element = input_list[i]
        while (input_list[j] > next_element) and (j >= 0):
            input_list[j+1] = input_list[j]
            j = j - 1
        input_list[j+1] = next_element
list = [19, 2, 31, 43, 30, 11, 121, 27]
insertionSort(list)
print(list)