import tkinter as tk
from tkinter import ttk

import psutils as psu

class analyzerApp(tk.Tk):
    """docstring for analyzerApp ."""
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.button = ttk.Button(text="Start", command=self.start)
        self.button.pack()
        self.progress = ttk.Progressbar(self, orient="horizontal",length=200, mode="determinate")
        self.progress.pack()
        self.cpu_load = 0
        self.maxbytes = 0

    def start(self):
        self.progress['value'] = 0
        self.progress['maximum'] = 100
        self.read_bytes()
    def read_bytes(self):
        '''get cpu load'''
        self.cpu_load = psu.cpu_percent(interval=1);
        self.progress['value'] = self.cpu_load

app = analyzerApp()
app.mainloop()
