import tkinter as tk

class MainFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.txt = tk.Label(self,
                            text="My tinker app",
                            bg= "medium spring green",
                            fg = "black")
        self.btn = tk.Button(self,
                             text="Press me",
                             bg = "light blue",
                             fg = "SlateBlue2",
                             activebackground="deep pink",)
        self.edt = tk.Entry(self,
                            bg = "light blue",
                            fg = "SlateBlue1",)

        self.sld = tk.Scale(self,
                            from_ = 0,
                            to= 100,
                            orient=tk.VERTICAL,
                            bg = "red",
                            fg = "goldenrod",
                            activebackground="black",)


        #  changes configuration of existing widget
        self.config(bg="cyan2")

        self.place_widgets()

    def place_widgets(self):
        settings = {'padx': 10, 'pady': 10, 'sticky': 'nswe'}
        self.txt.grid(row=0, column=0,**settings)
        self.btn.grid(row=0, column=1,**settings)
        self.btn.grid(row=1, column=0,**settings)
        self.edt.grid(row=1, column=1,**settings)
        self.sld.grid(row=2, column=0,**settings)

        self.columnconfigure(0, weight=2)
        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)


if __name__ == '__main__':
    root = tk.Tk()
    root.geometry("500x500+100+100")
    root.title("Tkinter Class Examples")
    main_frame = MainFrame(root)
    main_frame.pack(fill= tk.BOTH, expand=True)
    main_frame.pack()

    root.mainloop()