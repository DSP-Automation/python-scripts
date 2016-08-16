import tkinter as tk
from tkinter import ttk

import psutil as psu



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
        while(1):
            self.start()

    def start(self):
        self.read_bytes()

    def read_bytes(self):
        '''get cpu load'''
        self.cpu_load = psu.cpu_percent(interval=1);
        self.progress['value'] = self.cpu_load
        self.cpu_label_value['text'] = self.cpu_load


app = analyzerApp()
app.mainloop()
