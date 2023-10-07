from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screen import MDScreen
from kivy.uix.screenmanager import SlideTransition
from kivy.lang import Builder
import _thread as thread
from touch import TouchBox
import random
import time
import bubble_sort_algorithm
from merge_0 import MergeSort
#all sorting algorithms
root = Builder.load_string("""
<BarBox>:
	md_bg_color:[0, 0, 0, 1]
	size_hint_x:None
	width:"10dp"
<MainScreen>:
	id:main_screen_object
	MDBoxLayout:
		orientation:"vertical"
		MDBoxLayout:
			size_hint_y:None
			height:"100dp"
			md_bg_color:[0, 0, 0, 1]
			radius:[0, 0, 30, 30]
			MDBoxLayout:
			MDBoxLayout:
				size_hint_x:None
				width:"200dp"
				orientation:"vertical"
				padding:"0dp", "0dp", "10dp", "0dp"
				MDBoxLayout:
				SortAlgorithmTypeBox:
					root:main_screen_object
					size_hint_y:None
					height:"40dp"
					radius:[30, 30, 30, 30]
					md_bg_color:[1, 1, 1, 1]
					MDBoxLayout:
						size_hint:None, None
						size:"40dp", "40dp"
					MDLabel:
						id:sort_type
						text:"Insertion Sort"
						text_size:self.size
						halign:"center"
						valign:"middle"
					MDIconButton:
						id:chevron_type
						size_hint:None, None
						size:"40dp", "40dp"
						icon:"chevron-down"
						pos_hint:{"center_x":.5, "center_y":.5}
						theme_text_color:"Custom"
						text_color:[0, 0, 0, 1]
				MDBoxLayout:
		MDBoxLayout:
			md_bg_color:[255/float(255), 255/float(220), 255/float(255), 1]
			padding:"10dp", "5dp"
			FloatLayout:
				pos:self.parent.pos
				size:self.parent.size
				MDBoxLayout:
					pos:self.parent.pos
					Widget:
					MDBoxLayout:
						size_hint_y:None
						size_hint_x:None
						height:"400dp"
						width:"320dp"
						md_bg_color:[0, 0, 0, 1]
						MDBoxLayout:
							padding:3, 0, 0, 3
							MDBoxLayout:
								padding:3, 3, 3, 0
								spacing:2
								id:graph_box
								md_bg_color:[255/float(255), 255/float(220), 255/float(255), 1]
					Widget:
				MDBoxLayout:
					pos:self.parent.pos
					ScreenManager:
						id:sort_type_screen_manager
						Screen:
							name:"empty_screen"
						Screen:
							name:"choose_sort_algorithm_screen"
							MDBoxLayout:
								orientation:"vertical"
								MDBoxLayout:
									root:main_screen_object
									md_bg_color:[20/float(255), 20/float(255), 20/float(255), 1]
									orientation:"vertical"
									padding:"10dp", "10dp"
									spacing:10
									Widget:
									SortAlgorithm:
										size_hint_y:None
										height:"50dp"
										radius:[40, 40, 40, 40]
										md_bg_color:[0/float(255), 150/float(255), 220/float(255), 1]
										MDLabel:
											text:"Insertion Sort"
											text_size:self.size
											halign:"center"
											valign:"middle"
											color:[1, 1, 1, 1]
									SortAlgorithm:
										size_hint_y:None
										height:"50dp"
										radius:[40, 40, 40, 40]
										md_bg_color:[220/float(255), 220/float(255), 220/float(255), 1]
										MDLabel:
											text:"Bubble Sort"
											text_size:self.size
											halign:"center"
											valign:"middle"
											color:[0, 0, 0, 1]
									SortAlgorithm:
										size_hint_y:None
										height:"50dp"
										radius:[40, 40, 40, 40]
										md_bg_color:[220/float(255), 220/float(255), 220/float(255), 1]
										MDLabel:
											text:"Merge Sort"
											text_size:self.size
											halign:"center"
											valign:"middle"
											color:[0, 0, 0, 1]
									SortAlgorithm:
										size_hint_y:None
										height:"50dp"
										radius:[40, 40, 40, 40]
										md_bg_color:[220/float(255), 220/float(255), 220/float(255), 1]
										MDLabel:
											text:"Quick Sort"
											text_size:self.size
											halign:"center"
											valign:"middle"
											color:[0, 0, 0, 1]
									SortAlgorithm:
										size_hint_y:None
										height:"50dp"
										radius:[40, 40, 40, 40]
										md_bg_color:[220/float(255), 220/float(255), 220/float(255), 1]
										MDLabel:
											text:"Selection Sort"
											text_size:self.size
											halign:"center"
											valign:"middle"
											color:[0, 0, 0, 1]
									SortAlgorithm:
										size_hint_y:None
										height:"50dp"
										radius:[40, 40, 40, 40]
										md_bg_color:[220/float(255), 220/float(255), 220/float(255), 1]
										MDLabel:
											text:"Heap Sort"
											text_size:self.size
											halign:"center"
											valign:"middle"
											color:[0, 0, 0, 1]
									MDBoxLayout:
										size_hint_y:None
										height:"50dp"
										spacing:"5dp"
										CancelButtonBox:
										    root:main_screen_object
										    radius:[40, 40, 40, 40]
										    md_bg_color:[220/float(255), 0/float(255), 0/float(255), 1]
										    MDLabel:
										    	text:" Cancel"
										    	text_size:self.size
									    		halign:"center"
											    valign:"middle"
										    	color:[1, 1, 1, 1]
										MDBoxLayout:
										    radius:[40, 40, 40, 40]
									    	md_bg_color:[220/float(255), 220/float(255), 220/float(255), 1]
										    MDLabel:
										    	text:" Apply"
										    	text_size:self.size
									    		halign:"center"
											    valign:"middle"
										    	color:[0, 0, 0, 1]
									Widget:
		MDBoxLayout:
			size_hint_y:None
			height:"60dp"
			padding:5
			MDBoxLayout:
				md_bg_color:[0, 0/float(255), 0/float(255), 1]
				radius:[40, 40, 40, 40]
				MDLabel:
					text:"Start Sort"
					text_size:self.size
					halign:"center"
					valign:"middle"
					color:[1, 1, 1, 1]
 """)
class BarBox(MDBoxLayout):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
class SortAlgorithm(TouchBox):
	def respondToTouch(self):
		self.parent.root.turnOffAllAlgorithmBoxes(self.parent)
		self.md_bg_color = [0, 150/float(255), 220/float(255), 1]
		self.children[0].color = [1, 1, 1, 1]
class SortAlgorithmTypeBox(TouchBox):
	def respondToTouch(self):
		self.md_bg_color = [0, 150/float(255), 255/float(255), 1]
		self.root.ids.sort_type.color = [1, 1, 1, 1]
		self.root.ids.chevron_type.icon = "chevron-up"
		self.root.ids.sort_type_screen_manager.transition = SlideTransition(direction ="left")
		self.root.ids.sort_type_screen_manager.current = "choose_sort_algorithm_screen"
class CancelButtonBox(TouchBox):
    def respondToTouch(self):
        self.root.ids.sort_type_screen_manager.transition = SlideTransition(direction = "right")
        self.root.ids.sort_type_screen_manager.current = "empty_screen"
class MainScreen(MDScreen):
	#root screen of the app
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.values_list = [4, 1, 3, 2, 6, 5, 7]
		self.sort_algorithm = "insertion_algorithm"
		#self.values_list = []
		self.value_pool = [4, 1, 3, 2]
		#self.value_pool = list(range(1, 5))
		#random.shuffle(self.value_pool)
	def turnOffAllAlgorithmBoxes(self, parent):
		for child in parent.children[2:]:
			child.md_bg_color = [220/float(255), 220/float(255), 220/float(255), 1]
			child.children[0].color = [0, 0, 0, 1]
	def putIndexes(self, pool):
	    #print("pool", pool)
	    _pool = []
	    for i in range(len(pool)):
	        _pool.append([pool[i], i])
	    #print("POOL", _pool)
	    return _pool
	def generateValues(self):
		#generate values randomly that will be sorted
		for i in range(len(self.value_pool)):
			value  = random.choice(self.value_pool)
			self.value_pool.remove(value)
			self.values_list.append(value)
	def getWidthOfEachBar(self):
		length = len(self.values_list) - 1
		graph_width = (self.ids.graph_box.parent.parent.width - 6) - (length*2)
		return graph_width/float(len(self.values_list))
	def addBarOnGraph(self):
		#add bar
		for element in self.values_list:
			perc = (element/float(max(self.values_list)))*100
			bar_box = BarBox()
			bar_box.size_hint_y = None
			bar_box.height = ((self.ids.graph_box.parent.parent.height - 3)* perc)/float(100)
			bar_width = self.getWidthOfEachBar()
			bar_box.width = bar_width
			self.ids.graph_box.add_widget(bar_box)
	def swapIndex(self, swap_list, main_object):
		for i in range(len(swap_list)):
 			time.sleep(1)
 			graph_length = len(main_object.ids.graph_box.children) - 1
 			first_box = main_object.ids.graph_box.children[graph_length - swap_list[i][0]]
 			print(graph_length - swap_list[i][0])
 			second_box = main_object.ids.graph_box.children[graph_length - swap_list[i][1]]
 			main_object.ids.graph_box.children[graph_length - swap_list[i][1]] = first_box
 			main_object.ids.graph_box.children[graph_length - swap_list[i][0]] = second_box
	def sortWithBubbleSort(self):
		bubble = bubble_sort_algorithm.BubbleSort()
		_sorted_array, swap_list = bubble.bubbleSort(root.values_list)
		return swap_list
	def sortWithMergeSort(self):
	    merge = MergeSort()
	    values_list = self.putIndexes(self.values_list)
	    print("ROOT:", values_list)
	    sorted = merge.mergeSort(values_list, 0)
	    print("Sorted:", sorted)
	    return merge.swap_list
	def sortWithQuickSort(self):
		pass
	def sortWithSelectionSort(self):
		pass
class TestApp(MDApp):
 	#main app loop object
 	def reverseList(self, _list):
 		new_list = []
 		counter = len(_list)
 		while counter > 0:
 			new_list.append(_list[counter - 1])
 			counter -= 1
 		return new_list
 	def swapTest(self, _object, swap_list):
 		print("Children:", _object.ids.graph_box.children)
 		children_list = _object.ids.graph_box.children
 		reversed_children_list = self.reverseList(children_list)
 		print("Reversed:", reversed_children_list)
 		counter = len(_object.ids.graph_box.children) - 1
 		#for i in range(len(swap_list)):
 		temp = _object.ids.graph_box.children[swap_list[counter][0]]
 		print("Temp:", temp)
 		#_object.ids.graph_box.children[swap_list[0][0]] = reversed_children_list[swap_list[0][1]]
 		#_object.ids.graph_box.children[swap_list[0][1]] = temp
 		#for element in swap_list:
 		#	temp = _object.ids.graph_box.children[element[0]]
 		#	_object.ids.graph_box.children[element[0]] = _object.ids.graph_box.children[element[1]]
 		#	_object.ids.graph_box.children[ element[1]] = temp	
 	def printSwapIndex(self, swap_list, main_object):
 		counter = 0
 		#time.sleep(0.1)
 		for i in range(len(swap_list)):
 			#print(bubble.index_swap)
 			time.sleep(1)
 			counter += 1
 			graph_length = len(main_object.ids.graph_box.children) - 1
 			first_box = main_object.ids.graph_box.children[graph_length - swap_list[i][0]]
 			second_box = main_object.ids.graph_box.children[graph_length - swap_list[i][1]]
 			main_object.ids.graph_box.children[graph_length - swap_list[i][1]] = first_box
 			main_object.ids.graph_box.children[graph_length - swap_list[i][0]] = second_box
 		#print("COUNTER:", counter)
 	def build(self):
 		root = MainScreen()
 		#root.generateValues()
 		root.addBarOnGraph()
 		#bubble = bubble_sort_algorithm.BubbleSort()
 		#_sorted_array, swap_list = bubble.bubbleSort(root.values_list)
 		#root.putIndexes(root.values_list)
 		ind = root.putIndexes(root.values_list)
 		#merge = MergeSort()
 		#swap = root.sortWithMergeSort()
 		#print("Swap:", swap)
 		#print("Test:", self.swapTest(root, swap))
 		#res = merge.mergeSort(ind)
 		#thread.start_new_thread(self.printSwapIndex, (swap, root, ))
 		#print("@@: ", root.ids.graph_box.children[0])
 		return root
if __name__ == "__main__":
	TestApp().run()