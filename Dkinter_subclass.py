from tkinter import Tk, Frame

class ProgramWindow(Tk):

	def __init__(self, title, width, height):
		super().__init__()
		self.title(title)

		self.resize(width, height)

	def resize(self, width, height):
		# find the center point
		center_x = int(self.winfo_screenwidth()/2 - width / 2)
		center_y = int(self.winfo_screenheight()/2 - height / 2)

		self.geometry(f'{width}x{height}+{center_x}+{center_y}')

class DkFrame(Frame):

	def __init__(self, container, controller=None, fixed = False):

		self.__parent = container
		self.__frames = []
		self.__controller =None

		super().__init__(container)

	def render(self, row=1, column=1, columnspan=1, padx=0, pady=0):
		self.grid(row=row, column=column, columnspan=columnspan, padx=padx, pady=pady)

	def forget(self):
		self.grid_forget()

	def resize(self, width, height):
		self._controller.resize(width+100, height+100)

	def getValue(self, key):
		return self._controller.getValue(key)

	def storeData(self, key, value):
		self._controller.storeData(key, value)

	def getControlLayer(self):
		return self._controller

	def addFrame(self, frame):
		self._frames.append(frame)

	def getFrames(self):
		return self._frames

	def getParentLayer(self):
		return self._parent

