import tkinter as tk
from tkinter import ttk
from Dkinter_subclass import *

class MainFrame(tk.Frame):

	def __init__(self, title="New Window", width=400, height=400, icon = None):
		if icon == None:
			self.__parent = ProgramWindow(title, width, height)
		super().__init__(self.__parent)
		self.__width = width
		self.__height = height
		if icon:
			self.__parent.iconbitmap(icon)
		self.__data = {}
		self.__frames = []
		self.__frame_index = None
		self.__permaframes = []

		self.__parent.resize(width, height)

	def start(self):
		self.pack()

		for permaframe in self.__permaframes:
			permaframe.render()

		if len(self.__frames) > 0:
			self.renderFrame(0)

		self.__parent.mainloop()

	def resize(self, width, height):
		self.__parent.resize(width, height)
		self.width= width
		self.height= height

	def getsize(self):
		return(self.__width, self.__height)

	def getValue(self, key):
		if key in self.__data.keys():
			return self.__data[key]
		return None

	def storeData(self, key, value):
		self.__data[key]= value

	def addFrame(self, frame):
		self.__frames.append(frame)

	def addPermaframe(self, frame):
		self.__permaframes.append(frame)

	def forgetFrame(self):
		self.__frames[self.__frame_index].forget()

	def renderFrame(self, index):
		self.__frames[index].render()
		self.__frame_index = index

	def getFrameIndex(self):
		return self.__frame_index

	def getNumberFrames(self):
		return len(self.__frames)

#this is the Scroallable Window Branch
# class ScrollController(tk.Frame):
# 	def __init__(self, child, container, controller):
# 		self.__parent = container
# 		self.__controller = controller
# 		self.__child = child

# 		#attach to main frame
# 		super().__init__(self.__parent)
# 		self.__parent.addFrame(self)

# 		# Create A Canvas
# 		self.__canvas = tk.Canvas(self)

# 		# Add A Scrollbar To The Canvas
# 		self.__scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=self.__canvas.yview)

# 		# Configure The Canvas
# 		# self.__canvas.configure(yscrollcommand=self.__scrollbar.set)
# 		# self.__canvas.bind('<Configure>', lambda e: self.__canvas.configure(scrollregion = self.__canvas.bbox("all")))
		

# 	def render(self):

# 		#render all elements to the screen
# 		self.grid(row=1, column=1)
# 		print("self render")

# 		self.__canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
# 		print("Canvas render")

# 		self.__scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
# 		print("Scroll render")

# 		# self.__canvas.create_window((0,0), window=self.__child, anchor="nw")
# 		# self.__child.render()
# 		# print("Child render")

# 	def getCanvas(self):
# 		return self.__canvas

# 	def forget(self):
# 		pass


class SubFrame(DkFrame):

	def resize(self, width, height,):
		self.__controller.resize(width+100, height+100)

	def getValue(self, key):
		return self.__controller.getValue(key)

	def storeData(self, key, value):
		self.__controller.storeData(key, value)

	def getControlLayer(self):
		return self.__controller

	def addFrame(self, frame):
		self.__frames.append(frame)

	def getFrames(self):
		return self.__frames

	def getParentLayer(self):
		return self.__parent


class ScrollableSubFrame(SubFrame):
	def __init__(self, container, controller=None, v_scroll=False, h_scroll=False):
		super().__init__(container, controller)
		self.__parent = container
		self.__controller = controller

		#Create A Canvas
		self.__canvas = tk.Canvas(self)

		# Add A Scrollbar To The Canvas
		self.__scrollbar = ttk.Scrollbar(self, orient=tk.VERTICAL, command=self.__canvas.yview)
		self.__child_frame = ScrollChildFrame(self, self.__controller, self.__canvas)

	def addFrame(self, frame):
		self.__child = frame

	def render(self):
		print("noice!")
		pass








