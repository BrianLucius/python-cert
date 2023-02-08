import tkinter
from tkinter import messagebox

def Click():
    reply = messagebox.askquestion("Quit?", "Are you sure?")
    if reply == 'yes':
        skylight.destroy()
    
skylight = tkinter.Tk()
skylight.title("Skylight")
button = tkinter.Button(skylight, text="Bye!", command=Click)
button.place(x=10, y=10)
skylight.mainloop()