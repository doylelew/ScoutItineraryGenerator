import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('Learn To Code at Codemy.com')
root.geometry("500x400")

# Create A Main Frame
main_frame = tk.Frame(root)
main_frame.pack(fill=tk.BOTH, expand=1)

# Create A Canvas
my_canvas = tk.Canvas(main_frame)
my_canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

# Add A Scrollbar To The Canvas
my_scrollbar = ttk.Scrollbar(main_frame, orient=tk.VERTICAL, command=my_canvas.yview)
my_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Configure The Canvas
my_canvas.configure(yscrollcommand=my_scrollbar.set)
my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))

# Create ANOTHER Frame INSIDE the Canvas
second_frame = tk.Frame(my_canvas)

# Add that New frame To a Window In The Canvas
my_canvas.create_window((0,0), window=second_frame, anchor="nw")

for thing in range(100):
	tk.Button(second_frame, text=f'Button {thing} Yo!').grid(row=thing, column=0, pady=10, padx=10)


root.mainloop()