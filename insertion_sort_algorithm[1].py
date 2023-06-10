#insertion sort algorithm
class InsertionSort:
	def insertionSort(self, input_list):
		for i in range(1, len(input_list)):
			j = i - 1
			next_element = input[i]
			while ((input_list[j]  > next_element) and (j >= 0)):
				input_list[j+1] = input_list[j]
				j = j - 1
			input_list[j +1] = next_element
		return inputed_list