from tkinter import *

class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.configure(height=75, width=75)
        # create a menu bar
        men = Menu(root)
        root.config(menu=men)
        
        filemenu = Menu(men, tearoff=False)
        men.add_cascade(label="File", menu=filemenu)
        #filemenu.add_command(label="New", command=self.callback1)
        #filemenu.add_command(label="Open...", command=self.callback2)
        #filemenu.add_separator()
        #filemenu.add_command(label="Exit", command=self.callback3)
        #self.cmenu = Menu(self)
        #self.cmenu.add_command(label="Copy", command=self.copy)
        #self.cmenu.add_command(label="Paste", command=self.paste)
        #self.bind("<Button-3>", self.popup)
        
        self.pack()
        
    def callback1(self):
        print("You selected 'File | New'")
        
        
root = Tk()
app = Application(master=root)
app.mainloop()