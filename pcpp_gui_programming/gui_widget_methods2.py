import tkinter as tk

def destructo():
    frame.destroy()

window = tk.Tk()
frame = tk.Frame(window, width=200, height=100, bg='green')
button = tk.Button(frame, text="I'm a frame's child")
button.place(x=50, y=50)
frame.after(5000, destructo)
frame.pack()
window.mainloop()