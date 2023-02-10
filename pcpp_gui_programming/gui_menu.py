import tkinter as tk
from tkinter import messagebox

def about_app():
    messagebox.showinfo("App", "The application\nthat does nothing")

def are_you_sure(*args):
    if messagebox.askyesno("Quit?", "Are you sure you want to quit the app?"):
        window.destroy()

def open_file():
    messagebox.showinfo("Open Document", "We'll open a file here...")

window = tk.Tk()

main_menu = tk.Menu(window)
window.config(menu=main_menu)

sub_menu_file = tk.Menu(main_menu, tearoff=0)
main_menu.add_cascade(label="File", menu=sub_menu_file, underline=0)
sub_menu_file.add_command(label="Open", underline=0, command=open_file)

sub_sub_menu_file = tk.Menu(sub_menu_file, tearoff=0)
sub_menu_file.add_cascade(label="Open Recent File...", underline=5, menu=sub_sub_menu_file)

for i in range(8):
    number = str(i + 1)
    sub_sub_menu_file.add_command(label=number + ". File_" + number + ".txt", underline=0)

sub_menu_file.add_separator()
sub_menu_file.add_command(label="Exit", underline=1, command=are_you_sure, accelerator="Command-x")

sub_menu_edit = tk.Menu(main_menu)
main_menu.add_cascade(label="Edit", menu=sub_menu_edit, underline=1)

sub_menu_help = tk.Menu(main_menu)
main_menu.add_cascade(label="Help", menu=sub_menu_help, underline=0)
sub_menu_help.add_command(label="About...", command=about_app, underline=0)

window.bind_all("<Command-x>", are_you_sure)
window.mainloop()