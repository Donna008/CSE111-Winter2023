
import tkinter as tk
# from tkinter import *
# def close_window():
#     global entry
#     entry = E.get()
#     root.destroy()

# root = Tk()
# E = tk.Entry(root)
# E.pack(anchor = CENTER)
# B = Button(root, text = "OK", command = close_window)
# B.pack(anchor = S)
# root.mainloop()

window = tk.Tk()
label = tk.Label(
    text = 'hello',
    fg='white',
    bg = 'white'
)
frame = tk.Frame(
   )
frame.pack()
label.pack()
window.mainloop()