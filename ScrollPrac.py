from DoylesWindows import *
import tkinter as tk
from tkinter import ttk

class TestScroll(SubFrame):

	def render(self):

		for index in range(100):
			ttk.Button(self, text=f"This is button {index}").pack()

		super().render()

def main():
	#set up the window
	app = MainFrame(title="Scout Itinerary Generator")

	#attach all frames to it in the order they are needed, the Navbuttons frame lets you track back and forth between each later frame
	TestScroll(app, v_scroll=True)


	#begin the mainloop
	app.start()

if __name__ == "__main__":
	main()