# Required modules
from tkinter import *
import tkinter as tk

# Custom modules
import main
import func

def load_gui(self):

    # Labels:
    self.lbl_from = tk.Label(self.master,text='From:')
    self.lbl_from.grid(row=0,column=0,padx=(27,0),pady=(10,0))
    self.lbl_to = tk.Label(self.master,text='To:')
    self.lbl_to.grid(row=1,column=0,padx=(27,0),pady=(10,0))

    # Texts:
    self.from_folder_path = StringVar()
    self.txt_from = tk.Entry(self.master, textvariable=self.from_folder_path, width=80)
    self.txt_from.grid(row=0, column=1, padx=(27,0),pady=(10,0))

    self.to_folder_path = StringVar()
    self.txt_to = tk.Entry(self.master, textvariable=self.to_folder_path, width=80)
    self.txt_to.grid(row=1, column=1, padx=(27,0),pady=(10,0))

    # Buttons:
    self.browse_from_btn = tk.Button(self.master, text='Browse', command=lambda: func.browse_from_button(self))
    self.browse_from_btn.grid(row=0, column=3, padx=(10,0),pady=(10,0), sticky=N+W)
    self.browse_to_btn = tk.Button(self.master, text='Browse', command=lambda: func.browse_to_button(self))
    self.browse_to_btn.grid(row=1, column=3, padx=(10,0),pady=(10,0), sticky=N+W)
    self.file_check_btn = tk.Button(self.master, text='Process File(s)', height=1, width=25, bg='grey',command=lambda: func.process_files(self))
    self.file_check_btn.grid(row=3, column=1, padx=(27,0),pady=(10,0))

if __name__ == '__main__':
    pass
