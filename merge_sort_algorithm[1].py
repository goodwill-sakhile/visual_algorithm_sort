class MergeSort:
	
	def mergeSort(self, unsorted_list):
		if len(unsorted_list) <= 1:
			return unsorted_list
		middle = len(unsorted_list)
		left_list = unsorted_list[:middle]
		right_list = unsorted_list[middle:]
		left_list = self.mergeSort(left_list)
		right_list  = self.mergeSort(right_list)
		return list(self.merge(left_list, right_list))
	def merge(self, left_half, right_half):
		res = []
		while len(left_half) != 0 and len(right_half) != 0:
			if left_half[0] < right_half[0]:
				res.append(left_half[0])
				left_half.remove(left_half[0])
			else:
				res.append(right_half[0])
				right_half.remove(right_half[0])
		if len(left_half) == 0:
			res = res + right_half
		else:
			res = res + left_half
merge_sort = MergeSort()
merge_sort.mergeSort([10, 8, 4, 6, 5, 4, 3, 8, 9])