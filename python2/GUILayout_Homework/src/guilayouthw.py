from tkinter import *

ALL = N+S+W+E

class Application(Frame):
    
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=1)
        self.grid(sticky=ALL)
        
        self.rowconfigure(0, weight=1)
        f1 = Frame(self, bg="red")
        f1.grid(row=0, column=0, rowspan=1, columnspan=2, sticky=ALL)
        l1 = Label(f1, text="Frame 1")
        l1.pack()
        
        self.rowconfigure(1, weight=1)
        f2 = Frame(self, bg="green")
        f2.grid(row=1, column=0, rowspan=1, columnspan=2, sticky=ALL)
        l2 = Label(f2, text="Frame 2")
        l2.pack() 
        
        f3 = Frame(self, bg="blue")
        f3.grid(row=0, column=2, rowspan=2, columnspan=3, sticky=ALL)
        l3 = Label(f3, text="Frame 3")
        l3.pack()
        self.rowconfigure(2, weight=1)
        for c in range(5):
            self.columnconfigure(c, weight=1)
            Button(self, text="Button {0}".format(c+1)).grid(row=2, column=c, sticky=ALL) 


root = Tk()
app = Application(master=root)
app.mainloop()