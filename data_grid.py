import kivy
import urllib2
import json
import pprint
kivy.require('1.7.1')

from kivy.app import App
from kivy.lang import Builder
from kivy.properties import  ListProperty
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.togglebutton import ToggleButton
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.listview import ListView
from functools import partial
from kivy.core.window import Window
from kivy.uix.scrollview import ScrollView

Builder.load_string('''
# define how clabel looks and behaves
<CLabel>:
  canvas.before:
    Color:
      rgb: self.bgcolor
    Rectangle:
      size: self.size
      pos: self.pos

<HeaderLabel>:
  canvas.before:
    Color:
      rgb: self.bgcolor
    Rectangle:
      size: self.size
      pos: self.pos
'''
)

class CLabel(ToggleButton):
	bgcolor = ListProperty([1,1,1])

class HeaderLabel(Label):
	bgcolor = ListProperty([0.108,0.476,0.611])


data_json = open('data.json')
data = json.load(data_json)

header = ['ID', 'Nome', 'Preco', 'IVA']
col_size = [0.1, 0.5, 0.2, 0.2]
body_alignment = ["center", "left", "right", "right"]

products_list = []


class DataGrid(GridLayout):
	def add_row():
		pass
	def remove_row():
		pass
	def update_row():
		pass
	def __init__(self, header_data, body_data, b_align, cols_size, **kwargs):
		super(DataGrid, self).__init__(**kwargs)
		self.size_hint_y=None
		self.bind(minimum_height=self.setter('height'))
		self.cols = len(header_data)
		self.rows = len(body_data) + 1
		self.spacing = [1,1]
		n = 0
		for hcell in header_data:
			header_str = "[b]" + str(hcell) + "[/b]"
			self.add_widget(HeaderLabel(text=header_str, 
																	markup=True, 
																	size_hint_y=None,
																	height=40,
																	size_hint_x=cols_size[n]))
			n+=1
		counter = 0
		for bcell in body_data:
			n = 0
			for item in bcell:
				def change_on_press(self):
					childs = self.parent.children
					for ch in childs:
						if ch.id == self.id:
							print ch.state
							print len(ch.id)
							row_n = 0
							if len(ch.id) == 11:
								row_n = ch.id[4:5]
							else:
								row_n = ch.id[4:6]
							for c in childs:
								if ('row_'+str(row_n)+'_col_0') == c.id:
									if c.state == "normal":
										c.state="down"
									else:	
										c.state="normal"
								if ('row_'+str(row_n)+'_col_1') == c.id:
									if c.state == "normal":
										c.state="down"
									else:	
										c.state="normal"
								if ('row_'+str(row_n)+'_col_2') == c.id:
									if c.state == "normal":
										c.state="down"
									else:	
										c.state="normal"
								if ('row_'+str(row_n)+'_col_3') == c.id:
									if c.state == "normal":
										c.state="down"
									else:
										c.state="normal"
				def change_on_release(self):
					if self.state == "normal":
						self.state = "down"
					else:
						self.state = "normal"
				#Cell definition
				cell = CLabel(text=('[color=000000]' + item + '[/color]'), 
											background_normal="background_normal.png",
											background_down="background_pressed.png",
											halign=b_align[n],
											markup=True,
											on_press=partial(change_on_press),
											on_release=partial(change_on_release),
											text_size=(0, None),
											size_hint_x=cols_size[n], 
											size_hint_y=None,
											height=40,
											id=("row_" + str(counter) + "_col_" + str(n)))
				cell_width = Window.size[0] * cell.size_hint_x
				cell.text_size=(cell_width - 30, None)
				cell.texture_update()
				self.add_widget(cell)
				n+=1
			counter += 1



grid = DataGrid(header, data, body_alignment, col_size)

scroll = ScrollView(size_hint=(1, 1), size=(400, 400), pos_hint={'center_x':.5, 'center_y':.5})
scroll.add_widget(grid)
scroll.do_scroll_y = True
scroll.do_scroll_x = False



add_row_btn = Button(text="Add Row")
del_row_btn = Button(text="Delete Row")
upt_row_btn = Button(text="Update Row")

btn_grid = BoxLayout(orientation="vertical")
btn_grid.add_widget(add_row_btn)
btn_grid.add_widget(del_row_btn)
btn_grid.add_widget(upt_row_btn)

root = BoxLayout(orientation="horizontal")

root.add_widget(scroll)
root.add_widget(btn_grid)




class MainApp(App):
	def build(self):
		# grid = DataGrid(header, data, body_alignment, col_size)
		# interface = Interface()
		# print Window.size
		# return grid
		return root

if __name__=='__main__':
	MainApp().run()