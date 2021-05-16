# Python Version: 3.9
#
# Author: Ariel Rodriguez
#
# Purpose: Web Generator
#
# OS: Windows 10

# Required modules
from tkinter import *
import tkinter as tk

# Imported custom modules
import wg_func
import wg_gui

# Frame is the Tkinter frame class that our own class will inherit from
class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)

        # Define our master frame configuration
        self.master = master
        self.master.minsize(325, 125)
        self.master.maxsize(325, 125)

        # This center_window method will center our app on the user's screen (imported from func custom module)
        wg_func.center_window(self,325,125)
        self.master.title('Web Page Generator')
        self.master.configure(bg='#F0F0F0')

        # Load in the GUI widgets from a seperate module,
        # keeping your code comparmentalized and clutter free.
        wg_gui.load_gui(self)

        

if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
