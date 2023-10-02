class MergeSort:
    def __init__(self, **kwrags):
        self.swap_list = []
    def mergeSort(self, unsorted_list):
        if len(unsorted_list)  <= 1:
            return unsorted_list
        middle = len(unsorted_list) // 2
        left_list = unsorted_list[:middle]
        right_list = unsorted_list[middle:]
        #print(right_list)
        left_list = self.mergeSort(left_list)
        right_list = self.mergeSort(right_list)
    
        x, y =  list(self.merge(left_list, right_list))
        #print("y", y)
        print("self.swap", self.swap_list)
        return x
    def merge(self, left_half, right_half):
        res = []
        swap_list = []
        while len(left_half) != 0 and len(right_half) != 0:
            count = 0
            if left_half[0][0] < right_half[0][0]:
                res.append(left_half[0])
                self.swap_list.append([left_half[0][1], right_half[0][1]])
                #print([left_half[0][1], right_half[0][1]])
                left_half.remove(left_half[0])
            else:
                self.swap_list.append([right_half[0][1], left_half[0][1]])
                #print([right_half[0][1], left_half[0][1]])
                res.append(right_half[0])
                right_half.remove(right_half[0])
        if len(left_half) == 0:
            res = res + right_half
        else:
            res = res + left_half
        return res, swap_list
unsorted_list = [[64, 0], [34, 1], [25, 2], [12, 3], [22, 4], [11, 5], [90, 6]]
merge = MergeSort()

print(merge.mergeSort(unsorted_list))
#print("swap_swap", merge.swap_list)