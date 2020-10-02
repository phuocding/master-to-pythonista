from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename
from os.path import basename
from tkinter.messagebox import askokcancel, askyesno
from tkinter import PhotoImage

# functions = Functions()


class Frontend():
    activefile = 'unactive'

    def __init__(self):

        self.window = Tk()

        p1 = PhotoImage(file = "logo2.png")

        # Setting icon of master window
        self.window.iconphoto(False, p1)

        self.window.title("Untitled - Text-Editor")

        self.window.geometry("800x680")  # 1920x1080

        textboxstr = StringVar()
        self.textbox1 = Text(self.window, width=1920, height=1080)
        self.textbox1.pack()

        menubar = Menu(self.window)

        filename = Menu(menubar, tearoff=0)

        filename.add_command(label="New", command=self.new)
        filename.add_command(label="Open", command=self._openfile)
        filename.add_command(label="Save", command=self.savefile)
        filename.add_command(label="Save as", command=self.saveasfile)

        filename.add_separator()

        filename.add_command(
            label="Exit", command=lambda: self.window.destroy())

        menubar.add_cascade(label="File", menu=filename)
        menubar.add_cascade(label="Edit")
        menubar.add_cascade(label="Format")
        menubar.add_cascade(label="view")
        menubar.add_cascade(label="help")
        # menubar.add_cascade(label="Run",command = self.Runfile)

        self.window.config(menu=menubar)


    def openfile(self):
        pass

    

    def _openfile(self):
        """
        docstring
        """
        self.filename = askopenfilename()
        # self.openfilename = self.
        # print(self.filename)
        with open(self.filename) as file:
            content = file.read()
            self.textbox1.delete(1.0, END)
            self.textbox1.insert(1.0, content)
            self.activefile = 'active'
        self.window.title(basename(self.filename) + "- Text-Editor")
        self.filepath = self.filename

    def savefile(self):
        # print(self.textbox1.get(1.0,END))
        if self.activefile == 'active':
            self.tosavefile = self.filename
            with open(self.tosavefile, 'w') as finalsave:
                finalsave.write(self.textbox1.get(1.0, END))
        else:
            self.savefiledialog = asksaveasfilename()
            with open(self.savefiledialog, 'a') as _savefile:
                _savefile.write(self.textbox1.get(1.0, END))
                self.window.title(basename(self.savefiledialog) + "- Text-Editor")

    def saveasfile(self):

        self.saveasfilename = asksaveasfilename()
        self.savefilename = basename(self.saveasfilename) + "- Text-Editor"
        print(self.saveasfilename)
        with open(self.saveasfilename, 'a') as savefile:
            savefile.write(self.textbox1.get(1.0, END))
            self.window.title(self.savefilename)
            self.filepath = self.saveasfilename

    def new(self):
        # if(self.textbox1.get(1)):
        self.ans = askyesno("Warning", "Do you want to save your changes ?")
        # print(self.ans)
        if(self.ans):
            self.saveasfile()
        else:
            self.window.title("Untitled - Text-Editor")
            self.textbox1.delete(1.0, END)

    
    def run(self):
        self.window.mainloop()    

front = Frontend()

front.run()
# functions.run()

# gui1
