from tkinter import *
import tkinter as tk
import webbrowser
import os

# This function centers our window.
def center_window(self, w, h):
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()

    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))
    centerGeo = self.master.geometry('{}x{}+{}+{}'.format(w, h, x, y))
    return centerGeo

def generate_page(self):
    # Fetch the title and body inputs
    title = self.txt_title.get()
    body = self.txt_body.get()

    # Add the title and body input into page content
    content = '\
    <html>\
        <title>{}</title>\
        <body>\
            <h1>{}</h1>\
        </body>\
    </html>\
    '.format(title, body)
    file = open("generated_page.html", "w")
    file.write(content)
    file.close()
    webbrowser.open('file://' + os.path.realpath("generated_page.html"))

if __name__ == '__main__':
    pass
