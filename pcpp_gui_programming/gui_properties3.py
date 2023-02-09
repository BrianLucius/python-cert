import tkinter as tk
from tkmacosx import Button

window = tk.Tk()
button_1 = Button(window, text="Ordinary Button")
button_1.pack()
button_2 = Button(window, text="Extraordinary Button")
button_2.pack()
button_2["borderwidth"] = 10
button_2["highlightthickness"] = 10
button_2["padx"] = 10
button_2["pady"] = 5
button_2["underline"] = 1
button_2.config(bg="#000000")
button_2.config(fg="yellow")
button_2.config(activeforeground="#FF0000")
button_2.config(activebackground="green")
window.mainloop()