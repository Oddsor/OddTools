
__author__ = 'Odd'

import tkinter as tk
from tkinter import filedialog

class Listbox(tk.Frame):
    def __init__(self, data, master=None, multiple=False, orderable=True, height=10):
        tk.Frame.__init__(self, master)
        self.config()
        self.pack()
        self.list = data
        self.order = list()
        boxframe = tk.Frame(self)
        scrollbar = tk.Scrollbar(boxframe, orient=tk.VERTICAL)
        self.lister = tk.Listbox(boxframe, yscrollcommand=scrollbar.set)
        self.lister.config(height=height, exportselection=False)
        scrollbar.config(command=self.lister.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        if data is not None and data is not False:
            self.add_data(self.list)
        if multiple:
            self.lister.config(selectmode=tk.EXTENDED)
        self.lister.pack(side=tk.LEFT)
        boxframe.grid(row=0, rowspan=2, column=0)

        if orderable:

            def move_up():
                if len(self.lister.curselection()) == 1:
                    self.move_up(self.lister.curselection()[0])

            def move_down():
                if len(self.lister.curselection()) == 1:
                    self.move_down(self.lister.curselection()[0])

            container = tk.Frame(self)
            up_button = tk.Button(container, command=move_up)
            up_button.config(text="↑")
            up_button.pack(side="top")
            down_button = tk.Button(container, command=move_down)
            down_button.config(text="↓")
            down_button.pack(side="bottom")
            container.grid(row=1, column=1, sticky=tk.S)

    def get_items(self):
        return self.list

    def get_selected(self):
        '''
        >>> listbox = Listbox(['1: yep', '2: yep', '3: yep'])
        >>> listbox.move_up(1)
        >>> listbox.selection_set(0,2)
        >>> listbox.get_selected()
        [1, 0, 2]

        :return:
        '''
        retur = list()
        for item in self.lister.curselection():
            retur.append(self.order[item])
        return retur

    def add_data(self, listd):
        self.list = list(listd)
        self.order = list(range(0, len(listd)))
        self.lister.delete(0, tk.END)
        for item in self.list:
            self.lister.insert(tk.END, item)

    def move_up(self, index):
        if index > 0:
            self.list.insert(index - 1, self.list.pop(index))
            self.order.insert(index - 1, self.order.pop(index))
            self.refresh_list(index - 1)

    def move_down(self, index):
        if index < len(self.list) - 1:
            self.list.insert(index + 1, self.list.pop(index))
            self.order.insert(index + 1, self.order.pop(index))
            self.refresh_list(index + 1)

    def refresh_list(self, selected):
        self.lister.delete(0, tk.END)
        for item in self.list:
            self.lister.insert(tk.END, item)
        self.lister.selection_set(selected)

    def selection_set(self, indstart, indend):
        self.lister.selection_set(indstart, indend)

    def add_onclick(self, action):
        self.lister.bind('<<ListboxSelect>>', action)

if __name__ == "__main__":
    import doctest
    doctest.testmod()