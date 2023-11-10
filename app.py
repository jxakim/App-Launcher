from tkinter import *

root = Tk()

canvas = Canvas(root, width=700, height=500)
canvas.pack()
root.resizable(width=False, height=False) # Disable resizing 

root.title("zLauncher")

# Window components
title = Label(root, text="zLauncher", font=("Arial", 20, "bold"))
title.place(relx=0.5, rely=0.03, anchor="n")

root.mainloop()
