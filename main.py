from tkinter import *
from tkinter import ttk

root = Tk()
root.title("test_tkinter")

label = ttk.Label(root, text="hello python!")
label.pack()

##ウィンドウの表示
root.mainloop()

