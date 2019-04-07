from tkinter import Tk, Frame, Menu, Entry, Label, Button


class window(Frame):
    """
    Sub-Class: Frame;
    window object
    """
    def __init__(self, master):
        super().__init__(master)

    def drawMainGui(self):
        """
        draw the main window to the chat
        """
        self.menu = Menu(self.master)
        self.menu.add_command(label="Connect", command=self.connWindow)
        self.menu.add_command(label="Quit", command=self.master.quit)
        self.master.config(menu=self.menu)
        self.mainloop()

    def drawConnGui(self):
        """
        draw the connect window bring by "connection"
        """
        self.label = Label(self.master, text="Connection: ")
        self.label.grid()
        self.entry = Entry(self.master)
        self.entry.grid()
        self.cbutton = Button(self.master, text="GO!", command=self.connect)
        self.cbutton.grid()
        self.qbutton = Button(self.master, text="Quit", command=self.destroy)
        self.qbutton.grid()
        self.mainloop()

    def connWindow(self):
        """
        bring when press connecting
        """
        self.childWinConn = Tk()
        self.ConnWin = window(self.childWinConn)
        self.ConnWin.drawConnGui()

    def connect(self):
        """to connect to the chat server"""
        pass


def main():
    root = Tk()
    win = window(root)
    win.drawMainGui()


if __name__ == "__main__":
    main()
