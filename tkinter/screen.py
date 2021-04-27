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
# Scrollbar and scrollbar functionality
listScroll = tkinter.Scrollbar(mainWindow, orient=tkinter.VERTICAL, command=fileList.yview)
listScroll.grid(row=1, column=1, sticky='nsw', rowspan=2)
fileList['yscrollcommand'] = listScroll.set
# Frame for radio buttons
optionFrame = tkinter.LabelFrame(mainWindow, text='File Details')
optionFrame.grid(row=1, column=2, sticky='ne')
# Radio buttons
rbValue = tkinter.IntVar()
rbValue.set(1)  # default
radio1=tkinter.Radiobutton(optionFrame, text='Filename', value=1, variable=rbValue)
radio2=tkinter.Radiobutton(optionFrame, text='Path', value=2, variable=rbValue)
radio3=tkinter.Radiobutton(optionFrame, text='Timestamp', value=3, variable=rbValue)
radio1.grid(row=0, column=0, sticky='w')
radio2.grid(row=1, column=0, sticky='w')
radio3.grid(row=2, column=0, sticky='w')
# Widget to display result
resultLabel = tkinter.Label(mainWindow, text='Result')
resultLabel.grid(row=2, column=2, sticky='nw')
result = tkinter.Entry(mainWindow)
result.grid(row=2, column=2, sticky='sw')
# Frame for time spinners
timeFrame = tkinter.LabelFrame(mainWindow, text='Time')
timeFrame.grid(row=0, column=0, sticky='new')
#Time spinners
hourSpinner = tkinter.Spinbox(timeFrame, width=2, values=tuple(range(0,24)))
minuteSpinner = tkinter.Spinbox(timeFrame, width=2, values=tuple(range(0,59)))
secondSpinner = tkinter.Spinbox(timeFrame, width=2, values=tuple(range(0,59)))
hourSpinner.grid(row=0, column=0)
tkinter.Label(timeFrame, text=':').grid(row=0, column=1)
minuteSpinner.grid(row=0, column=2)
tkinter.Label(timeFrame, text=':').grid(row=0, column=3)
secondSpinner.grid(row=0, column=4)


mainWindow.mainloop()

print(rbValue.get())

