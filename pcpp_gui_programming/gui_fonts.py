import tkinter as tk

window = tk.Tk()
label_1 = tk.Label(window, text="Quick brown fox jumps over the lazy dog")
label_1.grid(column=0, row=0)
label_2 = tk.Label(window, text="Quick brown fox jumps over the lazy dog", font=("Times", 18))
label_2.grid(column=0, row=1)
label_3 = tk.Label(window, text="Quick brown fox jumps over the lazy dog", font=("Times", 36, "bold", "italic"))
label_3.grid(column=0, row=3)
window.mainloop()