from tkinter import *

def colorgen():
    while True:
        yield "red"
        yield "blue"

class Application(Frame):
    
    def __init__(self, master=None):
        colors = colorgen()
        Frame.__init__(self, master)
        self.master.rowconfigure(0, weight=1)
        self.master.columnconfigure(0, weight=1)
        self.grid(sticky=W+E+N+S)
        rcount = 0
        for r in (1, 22, 333):
            self.rowconfigure(r, weight=rcount)
            rcount += 1
            ccount = 0
            for c in (1, 22, 333):
                self.columnconfigure(r, weight=ccount)
                ccount += 1
                txt = "Item {0}, {1}".format(r,c)
                l = Label(self, text=txt, bg=next(colors))
                l.grid(row=r, column=c, sticky=E+W+N+S)
        self.f = Frame(self)
        self.f.grid(row=22, column=22, rowspan=1, columnspan=1, sticky=N+S+E+W)
        self.t = Text(self.f, height=10, width=80)
        self.t.grid(row=22, column=22, rowspan=1, columnspan=1, sticky=N+S+E+W)
                
root = Tk()
app = Application(master=root)
app.mainloop()