from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
import _thread as thread
import random
import time
import bubble_sort_algorithm
#all sorting algorithms
root = Builder.load_string("""
<BarBox>:
	md_bg_color:[0, 0, 0, 1]
	size_hint_x:None
	width:"10dp"
<MainScreen>:
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
				width:"175dp"
				orientation:"vertical"
				padding:"0dp", "0dp", "10dp", "0dp"
				MDBoxLayout:
				MDBoxLayout:
					size_hint_y:None
					height:"40dp"
					radius:[30, 30, 30, 30]
					md_bg_color:[1, 1, 1, 1]
					MDBoxLayout:
						size_hint:None, None
						size:"40dp", "40dp"
					MDLabel:
						text:"Insert Sort"
						text_size:self.size
						halign:"center"
						valign:"middle"
					MDIconButton:
						size_hint:None, None
						size:"40dp", "40dp"
						icon:"chevron-down"
						pos_hint:{"center_x":.5, "center_y":.5}
						theme_text_color:"Custom"
						text_color:[0, 0, 0, 1]
				MDBoxLayout:
		MDBoxLayout:
			padding:"10dp", "5dp"
			FloatLayout:
				pos:self.parent.pos
				size:self.parent.size
				MDBoxLayout:
					pos:self.parent.pos
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
				MDBoxLayout:
					pos:self.parent.pos
		MDBoxLayout:
			size_hint_y:None
			height:"60dp"
			padding:5
			MDBoxLayout:
				md_bg_color:[0, 0, 0, 1]
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
class MainScreen(MDScreen):
	#root screen of the app
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		self.values_list = []
	def generateValues(self):
		for i in range(10):
			value  = random.choice(list(range(1, 10)))
			self.values_list.append(value)
	def getWidthOfEachBar(self):
		length = len(self.values_list) - 1
		graph_width = (self.ids.graph_box.parent.parent.width - 6) - (length*2)
		return graph_width/float(len(self.values_list))
	def addBarOnGraph(self):
		#add bar on a graph
		for element in self.values_list:
			perc = (element/float(max(self.values_list)))*100
			bar_box = BarBox()
			bar_box.size_hint_y = None
			bar_box.height = ((self.ids.graph_box.parent.parent.height - 3)* perc)/float(100)
			bar_width = self.getWidthOfEachBar()
			bar_box.width = bar_width
			self.ids.graph_box.add_widget(bar_box)
class TestApp(MDApp):
 	#main app loop object
 	def printSwapIndex(self, main_object, bubble):
 		time.sleep(0.1)
 		for i in range(len(main_object.values_list)):
 			print(bubble.index_swap)
 			time.sleep(1)
 			graph_length = len(main_object.ids.graph_box.children) - 1
 			first_box = main_object.ids.graph_box.children[graph_length - bubble.index_swap[0]]
 			second_box = main_object.ids.graph_box.children[graph_length - bubble.index_swap[1]]
 			main_object.ids.graph_box.children[graph_length - bubble.index_swap[1]] = first_box
 			main_object.ids.graph_box.children[graph_length - bubble.index_swap[0]] = second_box
 	def build(self):
 		root = MainScreen()
 		root.generateValues()
 		root.addBarOnGraph()
 		bubble = bubble_sort_algorithm.BubbleSort()
 		thread.start_new_thread(bubble.bubbleSort, (root.values_list, ))
 		thread.start_new_thread(self.printSwapIndex, (root, bubble, ))
 		return root
if __name__ == "__main__":
	TestApp().run()