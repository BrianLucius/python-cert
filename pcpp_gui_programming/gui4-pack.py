import tkinter as tk

window = tk.Tk()
window.title("GUI 4 - Pack")
button_1 = tk.Button(window, text="Button #1",
                    bg="MediumPurple",
                    fg="LightSalmon",
                    activeforeground="LavenderBlush",
                    activebackground="HotPink")
button_2 = tk.Button(window, text="Button #2",
                   bg="#9370DB",
                   fg="#FFA07A",
                   activeforeground="#FFF0F5",
                   activebackground="#FF69B4")
button_3 = tk.Button(window, text="Button #3", bg="blue")
button_1.pack(side=tk.RIGHT, fill=tk.Y)
button_2.pack()
button_3.pack()
window.mainloop()