import tkinter as tk
import tkinter.font as tkFont

class App:
    def __init__(self, root):
        #setting title
        root.title("undefined")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        v1 = tk.StringVar()
        v2 = tk.StringVar()

        GLineEdit_67=tk.Entry(root)
        GLineEdit_67["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_67["font"] = ft
        GLineEdit_67["fg"] = "#333333"
        GLineEdit_67["justify"] = "center"
        GLineEdit_67["text"] = "Entry"
        GLineEdit_67.place(x=40,y=20,width=519,height=51)

        GButton_14=tk.Button(root)
        GButton_14["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_14["font"] = ft
        GButton_14["fg"] = "#000000"
        GButton_14["justify"] = "center"
        GButton_14["text"] = "Button"
        GButton_14.place(x=40,y=110,width=51,height=57)
        GButton_14["command"] = self.GButton_14_command

        GButton_508=tk.Button(root)
        GButton_508["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_508["font"] = ft
        GButton_508["fg"] = "#000000"
        GButton_508["justify"] = "center"
        GButton_508["text"] = "Button"
        GButton_508.place(x=100,y=110,width=60,height=56)
        GButton_508["command"] = self.GButton_508_command

        GRadio_112=tk.Radiobutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GRadio_112["font"] = ft
        GRadio_112["fg"] = "#333333"
        GRadio_112["justify"] = "center"
        GRadio_112["text"] = "RadioButton"
        GRadio_112.place(x=40,y=200,width=73,height=34)
        GRadio_112["value"] = "Test"
        GRadio_112["variable"] = v2
        GRadio_112["command"] = self.GRadio_112_command

        GRadio_153=tk.Radiobutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GRadio_153["font"] = ft
        GRadio_153["fg"] = "#333333"
        GRadio_153["justify"] = "center"
        GRadio_153["text"] = "RadioButton"
        GRadio_153.place(x=40,y=230,width=85,height=25)
        GRadio_153["value"] = "Test1"
        GRadio_153["variable"] = v1
        GRadio_153["command"] = self.GRadio_153_command

        GRadio_600=tk.Radiobutton(root)
        ft = tkFont.Font(family='Times',size=10)
        GRadio_600["font"] = ft
        GRadio_600["fg"] = "#333333"
        GRadio_600["justify"] = "center"
        GRadio_600["text"] = "RadioButton"
        GRadio_600.place(x=40,y=260,width=85,height=25)
        GRadio_600["value"] = "Test2"
        GRadio_600["variable"] = v1
        GRadio_600["command"] = self.GRadio_600_command

        GRadio_601 = tk.Radiobutton(root)
        ft = tkFont.Font(family='Times', size=10)
        GRadio_601["font"] = ft
        GRadio_601["fg"] = "#333333"
        GRadio_601["justify"] = "center"
        GRadio_601["text"] = "RadioButton"
        GRadio_601.place(x=40, y=300, width=85, height=25)
        GRadio_601["value"] = "Test3"
        GRadio_601["variable"] = v2
        GRadio_601["command"] = self.GRadio_600_command

    def GButton_14_command(self):
        print("command")


    def GButton_508_command(self):
        print("command")


    def GRadio_112_command(self):
        print("command")


    def GRadio_153_command(self):
        print("command")


    def GRadio_600_command(self):
        print("command")

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
