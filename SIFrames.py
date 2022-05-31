# tkinter imports
import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import filedialog as fd

# custom Library imports
from Dkinter import *
from SIExcelObj import ExcelObject


# permanent back and next buttons for navigating frame
class Navbuttons(SubFrame):

    def render(self):

        # create the buttons
        self.back_button = ttk.Button(self, text="Back", command=self.backFrame, state='disabled')
        self.next_button = ttk.Button(self, text="Next", command=self.nextFrame)

        # render the buttons
        self.next_button.grid(row=0, column=2, sticky=tk.E)
        self.back_button.grid(row=0, column=1, sticky=tk.E)

        # render frame on bottom of the control panel
        super().render(row=2, column=0, columnspan=3, pady=5)

    def backFrame(self):
        # get the index of the last frame
        index = self.getControlLayer().getFrameIndex() - 1
        top_index = self.getControlLayer().getNumberFrames() - 1

        # forget curent frame and render to the screen the next frame
        self.getControlLayer().forgetFrame()
        self.getControlLayer().renderFrame(index)

        # if this is the last frame in the list then disable the next button otherwise keep it active
        if index != top_index:
            self.next_button.state(['!disabled'])

        # if this is the first frame in the list then disable the next button otherwise keep it active
        if index == 0:
            self.back_button.state(['disabled'])
        else:
            self.back_button.state(['!disabled'])

    def nextFrame(self):
        # get the index of the next frame and top possible index
        index = self.getControlLayer().getFrameIndex() + 1
        top_index = self.getControlLayer().getNumberFrames() - 1

        # forget curent frame and render to the screen the next frame
        self.getControlLayer().forgetFrame()
        self.getControlLayer().renderFrame(index)

        # if this is the last frame in the list then disable the next button otherwise keep it active
        if index == top_index:
            self.next_button.state(['disabled'])
        else:
            self.next_button.state(['!disabled'])

        # if this is the first frame in the list then disable the next button otherwise keep it active
        if index != 0:
            self.back_button.state(['!disabled'])


# asks the user for an excel file that has the locatiion info
class OpenFileScreen(SubFrame):

    def render(self):

        self.resize(300, 0)

        # user instructions
        self.instruct = ttk.Label(self, text="Please choose a template file with all Locations")
        self.instruct.grid(column=0, row=0, sticky=tk.E)

        # allows them to see the string they selected before confirming, or type it in if they want
        self.DataFile_Loc = tk.StringVar()
        self.keyword = ttk.Entry(self, textvariable=self.DataFile_Loc, width=30)
        self.keyword.focus()
        self.keyword.grid(column=0, row=1, sticky=tk.E)

        self.filestr = tk.StringVar()

        # button that allows them to browse file and save the location string
        self.openFileButton = ttk.Button(self, text="Browse", command=self.select_file)
        self.openFileButton.grid(column=1, row=1, sticky=tk.W)

        # render frame center of the control frame
        super().render()

    def forget(self):
        self.storeData('excel file', self.DataFile_Loc.get())
        super().forget()

    def select_file(self):
        filetypes = (
            ('text files', '*.xlsx'),
            ('All files', '*.*')
        )

        filename = fd.askopenfilename(
            title='Open a file',
            initialdir='.',
            filetypes=filetypes
        )
        self.filestr = filename
        self.keyword.delete(0, tk.END)
        self.keyword.insert(0, self.filestr)


# Each block of location data in list locations screen
class LocationUnit(SubFrame):

    def __init__(self, container, index, row_index, controller):
        self.index = index
        self.row_index = row_index
        super().__init__(container, controller=controller)

    def render(self):
        self.full_time_frame = ttk.LabelFrame(self, text="Start and End Times")
        self.full_time_frame.grid(row=0, column=0)

        self.Checkbox_label = ttk.Label(self.full_time_frame, text="check the box\nto override times")
        self.Checkbox_label.grid(row=0, column=0)

        self.checkbox_value = tk.StringVar()
        self.overide_checkbox = ttk.Checkbutton(self.full_time_frame, variable=self.checkbox_value, onvalue='disabled',
                                                offvalue='!disabled')
        self.overide_checkbox.grid(row=0, column=1)

        self.sub_time_frame = ttk.LabelFrame(self.full_time_frame)
        self.sub_time_frame.grid(row=0, column=2)

        self.start_time = tk.StringVar()
        self.start_time_entry = ttk.Entry(self.sub_time_frame, textvariable=self.start_time, width=10)
        self.start_time_entry.grid(row=0, column=0)

        self.end_time = tk.StringVar()
        self.end_time_entry = ttk.Entry(self.sub_time_frame, textvariable=self.end_time, width=10)
        self.end_time_entry.grid(row=1, column=0)

        self.location_choices = self.getControlLayer().getValue('column choice')
        self.location_choice = tk.StringVar()
        self.choose_location = tk.OptionMenu(self, self.location_choice, *self.location_choices)
        self.choose_location.grid(row=0, column=1)

        self.horizontal_seperator = ttk.Separator(self, orient='horizontal')
        self.horizontal_seperator.grid(row=1, column=0, columnspan=2, sticky="ew", pady=5, )

        # place under the last row the parent screen has saved sequentially
        super().render(row=self.index + self.row_index)


# allows user to pick the locations they will want to write to a file, including order, times and so forth
class ListLocationsScreen(SubFrame):

    def render(self):

        # import the selected excel file and turn it into a pandas database through a custom object and methods
        self.excel_file = ExcelObject(self.getControlLayer().getValue('excel file'))
        self.cleaner = []
        self.rows = 4
        self.location_index = 0

        # frame renders information only id the file successfully opens in pandas
        if self.excel_file.dataframeIsValid():

            self.resize(500, 200)

            # remind the user what file they chose
            self.file_name_label = ttk.Label(self, text=f"Looking at File:{str(self.excel_file)}")
            self.file_name_label.grid(row=0, column=0, columnspan=4)

            # seprate the Label from the options
            self.horizontal_seperator1 = ttk.Separator(self, orient='horizontal')
            self.horizontal_seperator1.grid(row=1, column=0, columnspan=4, sticky="ew", pady=5)

            # allows the user to choose a Column to read from
            self.column_label = ttk.LabelFrame(self, text="Choose column to display")
            self.column_label.grid(row=2, column=0)

            self.column_choices = self.excel_file.getColumns()
            self.column_choice = tk.StringVar()
            self.choose_column = tk.OptionMenu(self.column_label, self.column_choice, *self.column_choices)
            self.choose_column.pack()

            # allows the user to choose number of locations to visit
            self.number_label = ttk.LabelFrame(self, text="How many locations to visit?")
            self.number_label.grid(row=2, column=1)
            self.number_of_locations = ttk.Entry(self.number_label, width=10)
            self.number_of_locations.pack()

            # allows the user to choose standard amount of time at a location
            self.time_label = ttk.LabelFrame(self, text="How many minutes per visit?")
            self.time_label.grid(row=2, column=2)
            self.minutes_per = ttk.Entry(self.time_label, width=10)
            self.minutes_per.pack()

            # button that sumbits the choices
            self.sumbit_options = ttk.Button(self, text="Submit", command=self.submitOptions)
            self.sumbit_options.grid(row=2, column=3)

            # seprate the options from what follows
            self.horizontal_seperator2 = ttk.Separator(self, orient='horizontal')
            self.horizontal_seperator2.grid(row=3, column=0, columnspan=4, sticky="ew", pady=5)

            # add all to cleaner
            self.cleaner = [self.file_name_label, self.column_label, self.choose_column, self.sumbit_options,
                            self.horizontal_seperator1, self.horizontal_seperator2, self.number_label, self.time_label,
                            self.number_of_locations, self.minutes_per]


        else:
            self.file_name_label = ttk.Label(self,
                                             text=f"'{str(self.excel_file)}' is not a file,\nplease hit 'back' and try again")
            self.file_name_label.pack(pady=15)

            # add all to cleaner
            self.cleaner = [self.file_name_label]

        # render frame center of the control frame
        super().render()

    def forget(self):
        # delete the object that was stored to keep memory low
        del self.excel_file

        # destroys the items so only one print per render of the frame
        for item in self.cleaner:
            item.destroy()

        self.destroyLocationBoxs()

        # clears attached frames
        self.__frames = []

        super().forget()

    def submitOptions(self):
        # data validation
        if self.column_choice.get() == '':
            messagebox.showerror("Invalid Value for 'Column choice'", "Column choice may not be left blank")
            return

        if not self.number_of_locations.get().isnumeric():
            messagebox.showerror("Invalid Value for 'Number of Locations'",
                                 "You entered a non-number value for'Number of Locations'\nPlease enter a number value for the feild\ne.g '5', '10', '37', etc.")
            return

        if not self.minutes_per.get().isnumeric():
            messagebox.showerror("Invalid Value for 'Minutes per location'",
                                 "You entered a non-number value for'Minutes per loation'\nPlease enter a number value for the feild\ne.g '5', '10', '37', etc.")
            return

        # submit data to control frame
        self.destroyLocationBoxs()
        self.getControlLayer().storeData("column choice", self.excel_file.getEachForColumn(self.column_choice.get()))
        self.getControlLayer().storeData("number of locations", int(self.number_of_locations.get()))
        self.getControlLayer().storeData("minutes per", int(self.minutes_per.get()))
        print(
            f"{self.getControlLayer().getValue('column choice')}, {int(self.number_of_locations.get())}, {int(self.minutes_per.get())}")

        # sumbit draw the new frames
        i = 0
        while i < self.getControlLayer().getValue("number of locations"):
            self.createLocationBox(self.location_index, self.rows)
            i += 1

        self.resize(800, 600)

    def createLocationBox(self, index, row_index):
        frame = LocationUnit(self, self.location_index, self.rows, self.getControlLayer())
        frame.render()
        self.location_index += 1

    def destroyLocationBoxs(self):
        for frame in self.getFrames():
            frame.forget()


# frame used for testing that a value was stored
class LabelScreen(SubFrame):

    def render(self):
        key = 'excel file'
        message = f"You chose file located @ {self.getValue(key)}"

        self.resize(450, 0)

        self.label = ttk.Label(self, text=message)

        self.label.pack(pady=15)

        self.grid(row=1, column=1)

    def forget(self):
        self.label.destroy()
        super().forget()
