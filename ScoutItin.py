from Dkinter import *
from SIFrames import *

def main():
	#set up the window
	app = MainFrame(title="Scout Itinerary Generator")

	#attach all frames to it in the order they are needed, the Navbuttons frame lets you track back and forth between each later frame
	Navbuttons(app, fixed=True) #fixed means that the frame does not close when navigating
	OpenFileScreen(app)
	ListLocationsScreen(app)

	#begin the mainloop
	app.start()

if __name__ == "__main__":
	main()