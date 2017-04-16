from Tkinter import *

class App(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()
        

    def createWidgets(self):
        self.entrythingy = Entry()
        self.entrythingy.pack(side="bottom")
        self.contents = StringVar()
        self.contents.set("this is a variable")
        #watch
        self.entrythingy["textvariable"] = self.contents
        #callback when hit Enter
        self.entrythingy.bind('<Key-Return>', self.print_contents)

        
        self.QUIT = Button(self)
        self.QUIT["text"] = "QUIT"
        self.QUIT["fg"]   = "red"
        self.QUIT["command"] =  self.quit
        self.QUIT.pack({"side": "left"})

        self.hi_there = Button(self)
        self.hi_there["text"] = "Hello",
        self.hi_there["command"] = self.say_hi

        self.hi_there.pack({"side": "left"})
        
    def say_hi(self):
        print "hi there, everyone!"

    def print_contents(self,fevent):
        print "hi. contents of entry is now ---->", \
              self.contents.get()
              
root = Tk()
app = App(master=root)
app.mainloop()
root.destroy()