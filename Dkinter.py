import tkinter as tk
from tkinter import ttk
from Dkinter_subclass import *


class MainFrame(tk.Frame):

	def __init__(self, title="New Window", width=400, height=400, icon=None):
		if icon == None:
			self._parent = ProgramWindow(title, width, height)
		super().__init__(self._parent)
		self._width = width
		self._height = height
		if icon:
			self._parent.iconbitmap(icon)
		self._data = {}
		self._frames = []
		self._frame_index = None
		self._permaframes = []

		self._parent.resize(width, height)

	def start(self):
		self.pack()

		for permaframe in self._permaframes:
			permaframe.render()

		if len(self._frames) > 0:
			self.renderFrame(0)

		self._parent.mainloop()

	def resize(self, width, height):
		self._parent.resize(width, height)
		self.width = width
		self.height = height

	def getsize(self):
		return (self._width, self._height)

	def getValue(self, key):
		if key in self._data.keys():
			return self._data[key]
		return None

	def storeData(self, key, value):
		self._data[key] = value

	def addFrame(self, frame):
		self._frames.append(frame)

	def addPermaframe(self, frame):
		self._permaframes.append(frame)

	def forgetFrame(self):
		self._frames[self._frame_index].forget()

	def renderFrame(self, index):
		self._frames[index].render()
		self._frame_index = index

	def getFrameIndex(self):
		return self._frame_index

	def getNumberFrames(self):
		return len(self._frames)


class SubFrame(DkFrame):

	def __init__(self, container, controller=None, fixed=False):

		self._parent = container
		self._frames = []

		if controller == None:
			self._controller = container
		else:
			self._controller = controller

		if fixed:
			self._parent.addPermaframe(self)
		else:
			self._parent.addFrame(self)

		super().__init__(container)


class ScrollableSubFrame(DkFrame):

	def __init__(self, container, controller=None, fixed=False):

		self._parent = container
		self._frames = []

		if controller == None:
			self._controller = container
		else:
			self._controller = controller

		if fixed:
			self._parent.addPermaframe(self)
		else:
			self._parent.addFrame(self)

		self._grid_frame = DkFrame(container)
		self._canvas_layer = tk.Canvas(self._grid_frame)
		self._scrollbar = ttk.Scrollbar(self._grid_frame, orient=tk.VERTICAL, command=self._canvas_layer.yview)

		self._canvas_layer.configure(yscrollcommand=self._scrollbar.set)
		self._canvas_layer.bind('<Configure>', lambda e: self._canvas_layer.configure(scrollregion= self._canvas_layer.bbox("all")))

		super().__init__(self._canvas_layer)

	def render(self, row=1, column=1, columnspan=1, padx=0, pady=0):
		self._grid_frame.grid(row=row, column=column, columnspan=columnspan, padx=padx, pady=pady)
		self._canvas_layer.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
		self._scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
		self._canvas_layer.create_window((0, 0), window= self, anchor="nw")

	def forget(self):
		self.grid_forget()
