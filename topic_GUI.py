from Tkinter import *

def main():    
    root = Tk()
    frame = Frame(root)
    frame.pack()

    bottomframe = Frame(root)
    bottomframe.pack( side = BOTTOM )


    redbutton = Button(frame, text="Red", fg="red")
    redbutton.pack( side = LEFT)

    greenbutton = Button(frame, text="Brown", fg="brown")
    greenbutton.pack( side = LEFT )

    bluebutton = Button(frame, text="Blue", fg="blue")
    bluebutton.pack( side = LEFT )

    blackbutton = Button(bottomframe, text="Black", fg="black")
    blackbutton.pack( side = BOTTOM)

    root.mainloop()
    
def win_1():
    win1 = Tk()
    topframe = Frame(win1)
    topframe.pack()
    
    but_1 = Button(topframe, text="Button1", fg="green")
    but_1.pack(side = TOP)
    but_2 = Button(topframe, text="Button1", fg="green")
    but_2.pack(side = BOTTOM)
    
    win1.mainloop()

#main()
win_1()