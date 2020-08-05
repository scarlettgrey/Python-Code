import tkinter as tk
from tkinter import ttk

def printSomething():
    print("Nama:")

win = tk.Tk()
win.title("Welcome To The Page")
win.geometry("600x400")

tabparent = ttk.Notebook(win)
home = ttk.Frame(tabparent)
tabparent.add(home, text = "Home")
group = ttk.Frame(tabparent)
tabparent.add(group, text = "Group")
tabparent.pack(expand = 1, fill = "both")

homebutton1 = tk.Button(home, text = "Edit Information", fg = "green")
homebutton1.pack(side = tk.LEFT)
homecanvas1 = tk.Canvas(home, width = 600, height = 400)
homecanvas1.pack()
homeentry1 = tk.Entry(home)
print("Nama:")
homecanvas1.create_window(100,100, window = homeentry1)

groupbutton1 = tk.Button(group, text = "Create Group", fg = "green")
groupbutton1.pack(side = tk.LEFT)

exitbutton = tk.Button(win, text = "Quit", fg = "blue", command = exit)
exitbutton.pack(side = tk.BOTTOM)



win.mainloop()