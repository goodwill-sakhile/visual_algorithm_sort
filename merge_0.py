import random
class MergeSort:
    def __init__(self, **kwrags):
        self.swap_list = []
    def putIndexes(self, pool):
	    #print("pool", pool)
	    _pool = []
	    for i in range(len(pool)):
	        _pool.append([pool[i], i])
	    #print("POOL", _pool)
	    return _pool
    def generateValues(self, _pool):
        new_pool = []
        #generate values randomly that will be sorted
        for i in range(len(_pool)):
            value  = random.choice(_pool)
            _pool.remove(value)
            new_pool.append(value)
        return new_pool
    def mergeSort(self, unsorted_list, counter):
        if len(unsorted_list)  <= 1:
            return unsorted_list
        middle = len(unsorted_list) // 2
        left_list = unsorted_list[:middle]
        right_list = unsorted_list[middle:]
        counter+=1
        print("counter:", counter)
        left_list = self.mergeSort(left_list, counter)
        right_list = self.mergeSort(right_list, middle)
        x =  list(self.merge(left_list, right_list))
        return x
    def merge(self, left_half, right_half):
        res = []
        swap_list = []
        counter = 0
        while len(left_half) != 0 and len(right_half) != 0:
            
            if left_half[0][0] < right_half[0][0]:
                res.append(left_half[0])
                left_half.remove(left_half[0])
            else:
                #self.swap_list.append([left_half[0][1], right_half[0][1]])
                res.append(right_half[0])
                right_half.remove(right_half[0])
            
        if len(left_half) == 0:
            res = res + right_half
        else:
            res = res + left_half
        return res
#unsorted_list = [[64, 0], [34, 1], [25, 2], [12, 3], [22, 4], [11, 5], [90, 6]]
merge = MergeSort()
pool = merge.generateValues(list(range(100)))
#print(pool)
_list = merge.putIndexes(pool)
#print("index_included:", _list)
#print("")
#print("Sorted:", merge.mergeSort(_list))
#print("")
#print("Swap:", merge.swap_list)
#print("swap_swap", merge.swap_list)