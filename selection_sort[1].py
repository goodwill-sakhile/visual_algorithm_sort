#selection sort algorithm

class SelectionSort:
	def selectionSort(self, input_list):
		for element_id in range(len(input_list)):
			min_element_id = element_id
			for j in range(element_id + 1, len(input_list)):
				min_element_id = j
				input_list[element_id], inputed_list[min_element_id] = inputed_list[min_element_id], inputed_list[element_id]
		return input_list