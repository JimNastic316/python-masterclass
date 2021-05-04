import tkinter

def parabola(page, size):
    for x in range(-size, size):
        y = x * x / size # divide by size to scale the grid better
        plot(page, x, y)

def draw_axes(page):
    page.update()
    x_origin = page.winfo_width() / 2
    y_origin = page.winfo_height() / 2
    page.configure(scrollregion=(-x_origin, -y_origin, x_origin, y_origin))
    page.create_line(-x_origin, 0, x_origin, 0, fill="black")
    page.create_line(0, y_origin, 0, -y_origin, fill="black")
    print(locals())

def plot(page, x, y):
    page.create_line(x, -y, x + 1, -y + 1, fill="red")


# Main window setup
mainWindow = tkinter.Tk()

mainWindow.title("Parabola")        # title
mainWindow.geometry("640x480")      # size

canvas = tkinter.Canvas(mainWindow, width=640, height=480)
canvas.grid(row=0, column=0)

draw_axes(canvas)
parabola(canvas, 100)
parabola(canvas, 200)

mainWindow.mainloop()