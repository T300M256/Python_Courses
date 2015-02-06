from tkinter import *

class Application(Frame):
    """Application main window class."""
    def __init__(self, master=None):
        """Main frame initialization (mostly delegated)"""
        Frame.__init__(self, master)
        self.pack()
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
        
        bottom_frame = Frame(self)
        bottom_frame.pack(side=TOP)
        self.handleb = Button(bottom_frame, text="Convert", command=self.handle)
        self.handleb.pack(side=TOP)
        
    def handle(self):
        """What to do if the convert button is clicked..."""
        text1 = self.text_in1.get()
        text2 = self.text_in2.get()
        new_label = ""
        try:
            new_label = str(float(text1) + float(text2))
        except:
            new_label = "***ERROR***"
            #raise
        self.label.config(text=new_label)
        
root = Tk()
app = Application(master=root)
app.mainloop()