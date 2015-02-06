from tkinter import *

ALL = N+S+W+E

class Application(Frame):
    
    def mouseHandler(self, event):
        if event.widget == self.f1:
            print("Frame 1 clicked at", event.x, event.y)
        elif event.widget == self.f2:
            print("Frame 2 clicked at", event.x, event.y)  
        
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=1)
        self.grid(sticky=ALL)
        
        self.rowconfigure(1, weight=1)
        self.f1 = Frame(self, bg="red",)
        self.f1.grid(row=1, column=0, rowspan=1, columnspan=2, sticky=ALL)
        self.f1.bind("<Button-1>", self.mouseHandler)
        #l1 = Label(self.f1, text="Frame 1")
        #l1.pack()
        self.rowconfigure(2, weight=1)
        self.f2 = Frame(self, bg="green")
        self.f2.grid(row=2, column=0, rowspan=1, columnspan=2, sticky=ALL)
        self.f2.bind("<Button-1>", self.mouseHandler)
        #l2 = Label(self.f2, text="Frame 2")
        #l2.pack() 
        self.rowconfigure(3, weight=1)
        self.f3 = Frame(self, bg="blue")
        self.f3.grid(row=1, column=2, rowspan=2, columnspan=3, sticky=ALL)
        self.e = Entry(self.f3)
        self.e.grid(row=0,column=2, rowspan=1, columnspan=3, sticky=ALL)
        self.t = Text(self.f3)# Text box doesn't like being in a Frame it won't fill the frame
        self.t.grid(row=1, column=2, rowspan=4, columnspan=3, sticky=ALL)
        self.button_txt = {0:"red", 1:"blue", 2:"green", 3:"black", 4:"Open"}
        for c in range(5):
            self.columnconfigure(c, weight=1)
            Button(self, text=self.button_txt[c]).grid(row=3, column=c, sticky=N+S+E+W) # E+W used to keep the same width 

root = Tk()
app = Application(master=root)
app.mainloop()