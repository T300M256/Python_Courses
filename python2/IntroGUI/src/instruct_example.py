from tkinter import *

class Application(Frame):
    """Application main window class."""
    def __init__(self, master=None):
        """Main frame initialization (mostly delegated)"""
        Frame.__init__(self, master)
        master.rowconfigure(0,weight=1)
        master.columnconfigure(0,weight=1)
        self.grid(sticky=S+W+E+N)
        self.createWidgets()

    def createWidgets(self):
        """Add all the widgets to the main frame."""
        top_frame = Frame(self)
        self.text_in1 = Entry(top_frame)
        self.text_in2 = Entry(top_frame)
        self.label = Label(top_frame, text="Waiting for Data")
        self.text_in1.pack()
        self.text_in2.pack()
        self.label.pack()
        top_frame.pack(side=TOP)

        bottom_frame = Frame(self, bg="red")
        bottom_frame.pack(side=TOP, fill=BOTH, expand=True)
        self.A = Button(bottom_frame, text="Convert")
        self.A.pack(side=TOP)
        self.B = Button(bottom_frame, text="Foo")
        self.B.pack(side=TOP)

root = Tk()
root.geometry("300x300")
app = Application(master=root)
root.mainloop()