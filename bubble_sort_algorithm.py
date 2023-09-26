#bubble sort algorithm
import _thread as thread
import time
class BubbleSort:
	def __init__(self):
		self.index_swap_list = []
	def updateIndexSwap(self, j):
		self.index_swap = [j, j+1]
	def bubbleSort(self, _array):
		for i in range(len(_array)):
			for j in range(len(_array) - i - 1):
				if (_array[j + 1] < _array[j]):
					#thread.start_new_thread(self.updateIndexSwap, (j, ))
					#time.sleep(1)
					temp = _array[j]
					_array[j] = _array[j + 1]
					_array[j + 1] = temp
					self.index_swap_list.append([j, j+1])
				#else:
					#time.sleep(1)
		print("Sorted array: ", _array)
		return _array, self.index_swap_list
if __name__  == "__main__":
	BubbleSort().bubbleSort([5, 4, 9,  3, 15, 4, 45, 90, 62, 12, 1, 3])