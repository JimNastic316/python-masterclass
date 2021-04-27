import tkinter
import os




mainWindow = tkinter.Tk()

mainWindow.title('Grid Demo')
mainWindow.geometry('640x400-8-200')

label=tkinter.Label(mainWindow, text='Tkinter Grid Demo')
label.grid(row=0, column=0, columnspan=3)
# set up columns & rows
mainWindow.grid_columnconfigure(0, weight=1)
mainWindow.grid_columnconfigure(1, weight=1)
mainWindow.grid_columnconfigure(2, weight=3)
mainWindow.grid_columnconfigure(3, weight=3)
mainWindow.grid_columnconfigure(4, weight=3)
mainWindow.rowconfigure(0, weight=1)
mainWindow.rowconfigure(1, weight=10)
mainWindow.rowconfigure(2, weight=1)
mainWindow.rowconfigure(3, weight=3)
mainWindow.rowconfigure(4, weight=3)
# Listbox
fileList = tkinter.Listbox(mainWindow)
fileList.grid(row=1, column=0, sticky='nsew', rowspan=2)
fileList.config(border=2, relief='sunken')
# Populate Listbox
for zone in os.listdir('/usr/bin'):
    fileList.insert(tkinter.END, zone)

mainWindow.mainloop()
