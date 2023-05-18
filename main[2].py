from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivy.lang import Builder
root = Builder.load_string("""
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
						md_bg_color:[0, 0, 0, 1]
						MDBoxLayout:
							padding:3, 0, 0, 3
							MDBoxLayout:
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
class MainScreen(MDScreen):
	#root screen of the app
	pass
class TestApp(MDApp):
 	def build(self):
 		root = MainScreen()
 		return root
if __name__ == "__