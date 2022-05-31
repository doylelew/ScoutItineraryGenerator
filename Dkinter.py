import tkinter as tk

class ProgramWindow(tk.Tk):

	def __init__(self, title, width, height):
		super().__init__()
		self.title(title)

		self.resize(width, height)

	def resize(self, width, height):
		# find the center point
		center_x = int(self.winfo_screenwidth()/2 - width / 2)
		center_y = int(self.winfo_screenheight()/2 - height / 2)

		self.geometry(f'{width}x{height}+{center_x}+{center_y}')

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

class SubFrame(tk.Frame):

	def __init__(self, container, fixed = False, controller= None):

		self.__parent = container
		self.__frames = []

		if controller == None:
			self.__controller = container
		else:
			self.__controller = controller

		if fixed:
			self.__parent.addPermaframe(self)
		else:
			self.__parent.addFrame(self)

		super().__init__(container)

	def render(self, row=1, column=1, columnspan=1, padx=0, pady=0):
		self.grid(row=row, column=column, columnspan=columnspan, padx=padx, pady=pady)

	def forget(self):
		self.grid_forget()

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







