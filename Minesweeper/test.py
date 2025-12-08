import tkinter as tk

root = tk.Tk()
root.title("Tk Example")
root.minsize(200, 200)
root.geometry("1000x500+0+50")

# Create two labels
tk.Button(root,text="██",width=2).grid(row=0,column=0)
tk.Button(root,text="██",width=2).grid(row=0,column=1)

root.mainloop()
