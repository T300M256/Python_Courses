from tkinter import *

ALL = N+S+W+E

class Application(Frame):
    
    def mouseHandler(self, event):
        if event.widget == self.f1:
            print("Frame 1 clicked at", event.x, event.y)
        elif event.widget == self.f2:
            print("Frame 2 clicked at", event.x, event.y)
            
    def set_text_color(self, color):
        print("Attempting to set text color to "+color)
        self.t.config(fg=color)
        
    def get_text_from_file(self):
        try:
            fh = open(self.e.get(),"r")
        except FileNotFoundError:
            print("Could not open file \'"+self.e.get()+"\' for reading") # change to specific file name later
            #raise
        self.t.insert(END,fh.read())
        fh.close()
            
        
    def __init__(self, master=None):
        # necessary initialize stuff
        Frame.__init__(self, master)
        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=1)
        self.grid(sticky=ALL)
        
        # set up for frame 1
        self.rowconfigure(0, weight=1)
        self.f1 = Frame(self, bg="red",)
        self.f1.grid(row=0, column=0, rowspan=1, columnspan=2, sticky=ALL)
        self.f1.bind("<Button-1>", self.mouseHandler)
        #l1 = Label(self.f1, text="Frame 1")
        #l1.pack()
        
        # set up for frame 2
        self.rowconfigure(1, weight=1)
        self.f2 = Frame(self, bg="green")
        self.f2.grid(row=1, column=0, rowspan=1, columnspan=2, sticky=ALL)
        self.f2.bind("<Button-1>", self.mouseHandler)
        #l2 = Label(self.f2, text="Frame 2")
        #l2.pack() 
        
        # set up for frame 3
        self.f3 = Frame(self, bg="blue")
        self.f3.grid(row=0, column=2, rowspan=2, columnspan=3, sticky=ALL)
        # this is for frame 3's internal grid
        self.f3.rowconfigure(0, weight=0)
        self.f3.rowconfigure(1, weight=1)
        self.f3.columnconfigure(0, weight=1)
        # text & entry widgets in Frame 3
        self.text_color = "black"
        self.e = Entry(self.f3)
        self.e.grid(row=0,column=0, rowspan=1, columnspan=3, sticky=ALL)
        self.e.insert(0,"some.txt")
        self.t = Text(self.f3)
        self.t.grid(row=1, column=0, rowspan=4, columnspan=3, sticky=ALL)
        
        # setup buttons
        self.rowconfigure(2, weight=1)
        
        for c in range(5):
            # configure the columns here
            self.columnconfigure(c, weight=1)
        # add buttons individually here.
        Button(self, text="Red", command= lambda: self.set_text_color("red")).grid(row=2, column=0, sticky=N+S+E+W)
        Button(self, text="Blue", command= lambda: self.set_text_color("blue")).grid(row=2, column=1, sticky=N+S+E+W)
        Button(self, text="Green", command= lambda: self.set_text_color("green")).grid(row=2, column=2, sticky=N+S+E+W)
        Button(self, text="Black", command= lambda: self.set_text_color("black")).grid(row=2, column=3, sticky=N+S+E+W)
        
        Button(self, text="Open", command=self.get_text_from_file).grid(row=2, column=4, sticky=N+S+E+W)
                

root = Tk()
app = Application(master=root)
app.mainloop()