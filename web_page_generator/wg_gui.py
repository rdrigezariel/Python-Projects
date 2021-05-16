from tkinter import *
import tkinter as tk

import wg_func

def load_gui(self):

    # Labels:
    self.lbl_title = tk.Label(self.master, text='Title: ')
    self.lbl_title.grid(row=0, column=0, padx=25, pady=10)
    self.lbl_body = tk.Label(self.master, text='Body: ')
    self.lbl_body.grid(row=2, column=0, padx=25, pady=10)

    # Texts:
    self.txt_title = tk.Entry(self.master, text='', width=30)
    self.txt_title.grid(row=0, column=1, pady=10)
    self.txt_body = tk.Entry(self.master, text='', width=30)
    self.txt_body.grid(row=2, column=1, pady=10)

    # Button:
    self.generate_page_btn = tk.Button(self.master, text='Generate Page', height=1, bg='grey', command=lambda: wg_func.generate_page(self))
    self.generate_page_btn.grid(row=3, column=1, padx=0, pady=0, sticky=E)


if __name__ == '__main__':
    pass
