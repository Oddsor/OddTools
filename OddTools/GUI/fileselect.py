__author__ = 'Odd'

import tkinter as tk

def fileselect(root, path, dir=True, func=None, save=False, filetypes=None):
    '''
    :param root: The root frame in which to insert the file select
    :param path: The file or directory path in a stringvar
    :param dir: Opening a directory or just files? True for directory
    :param func: Not implemented yet
    :return: The file select frame
    '''
    #TODO: add functions? not sure what to do here
    file_frame = tk.Frame(root)
    entry = tk.Entry(file_frame, textvariable=path)

    def open_file():
        if dir and not save:
            newpath = tk.filedialog.askdirectory(initialdir=path.get())
        elif not save:
            newpath = tk.filedialog.askopenfilename(initialfile=path.get())
        if save:
            if filetypes is None:
                newpath = tk.filedialog.asksaveasfilename()
            else:
                newpath = tk.filedialog.asksaveasfilename(initialdir=path.get(),defaultextension=filetypes[0], filetypes=filetypes)
        if entry.get() != newpath and newpath != '':
            path.set(newpath)

    entry.config(width=30)
    entry.pack(side="left")

    button = tk.Button(file_frame, command=open_file)
    button.config(text="Select")

    button.pack(side="left")
    return file_frame

