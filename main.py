from tkinter import *
from tkinter import filedialog
from tkinter.font import BOLD, ITALIC

class GUI :

    def __init__(self):
        

        self.gui = Tk()

        self.gui.title("Shaz")
        self.gui.geometry("500x400")
        self.text= Text(self.gui,bg="Light Green",fg="Royal Blue",wrap= WORD,font=("Ubuntu",16,BOLD,ITALIC))
        self.text.pack(padx= 10,pady=10,expand=True,fill= BOTH)

        self.mymenu=Menu()
        File = Menu()

        File.add_command(label="New",accelerator= "CTRL + N", command = self.new_file)
        File.add_command(label="Open File",accelerator="CTRL+O",command= self.Open_file)
        self.mymenu.add_cascade(label="File",menu= File )
        self.gui.config(menu=self.mymenu)


        self.gui.mainloop()

    def new_file(self):

            
            self.text.delete(1.0,END)
    
    def Open_file(self):

        f= filedialog.askopenfile(mode="r")
        data = f.read()
        self.text.delete(1.0,END)
        self.text.insert(1.0,data)

Editor= GUI()

