
# Required modules
from tkinter import *
import tkinter as tk
import shutil
import os
import time
from datetime import datetime, timedelta

# Custom modules
import func
import gui

# Frame is the Tkinter frame class that our own class will inherit from
class ParentWindow(Frame):
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # Define our master frame configuration
        self.master = master

        # Window Size
        self.master.minsize(675,125) #(Height, Width)
        self.master.maxsize(675,125)

        # Window Title
        self.master.title("The File Transfer Demo")

        # func.center_window method will center our app on the user's screen
        func.center_window(self,500,300)

        # load in the GUI widgets
        gui.load_gui(self)
        
if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
