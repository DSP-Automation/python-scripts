import tkinter as tk
from tkinter import ttk

import psutil as psu
import threading


class analyzerApp(tk.Tk):
    """docstring for analyzerApp ."""
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.cpu_label = tk.Label(self, text="CPU Load:")
        self.cpu_label.grid(row=0, column=0)
        self.cpu_label_value = tk.Label(self,text="")
        self.cpu_label_value.grid(row=0, column=1)
        self.progress = ttk.Progressbar(self, orient="horizontal",length=200, mode="determinate")
        self.progress.grid(row=0,column=3)

        self.cpu_load = 0
        self.progress['value'] = 0
        self.progress['maximum'] = 100

app = analyzerApp()
def readCPU():
    threading.Timer(0.50,readCPU).start()
    app.cpu_load = psu.cpu_percent()
    app.progress['value'] = app.cpu_load
    app.cpu_label_value['text'] = app.cpu_load
    app.update()

readCPU()
app.mainloop()
