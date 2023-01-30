import tkinter as tk
from tkinter import  ttk

win = tk.Tk()
win.title("Menubar");

#Menu
# menubar = tk.Menu(win)
# win.config(menu=menubar)
def save():
    print("saved")
########################## simple Menu bar #########################
# menubar.add_command(label="save",command=save)
# menubar.add_command(label="menu",command=save)
# menubar.add_command(label="save as",command=save)
# menubar.add_command(label="Print",command=save)
# menubar.add_command(label="options",command=save)
#####################################################################

main_menu = tk.Menu(win)
win.config(menu=main_menu)
file_menu = tk.Menu(main_menu,tearoff=0) # cascade 
file_menu.add_command(label="NEW FILE",command=save)
file_menu.add_command(label="save",command=save)
file_menu.add_command(label="menu",command=save)
file_menu.add_command(label="save as",command=save)
file_menu.add_separator()
file_menu.add_command(label="Print",command=save)
file_menu.add_command(label="options",command=save)

# edit_menu

edit_menu = tk.Menu(main_menu,tearoff=0)
edit_menu.add_command(label="Undo",command=save)
edit_menu.add_command(label="Rndo",command=save)

main_menu.add_cascade(label="EDIT",menu=edit_menu)
main_menu.add_cascade(label="FILE",menu=file_menu)


edit_menu = tk.Menu(win)


win.mainloop()