import tkinter as tk

def blink():
    global is_yellow
    if is_yellow:
        color = 'pink'
    else:
        color = 'yellow'
    is_yellow = not is_yellow
    frame.config(bg=color)
    frame.after(750, blink)

is_yellow = True
window = tk.Tk()
frame = tk.Frame(window, width=400, height=300, bg='yellow')
frame.after(750, blink)
frame.pack()
window.mainloop()