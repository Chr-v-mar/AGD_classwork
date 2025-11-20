import tkinter as tk
from wsgiref.util import application_uri


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
                            fg = "goldenrod")


        #  changes configuration of existing widget
        self.config(bg="cyan2")

        self.place_widgets()

    def place_widgets(self):
        self.txt.grid(row=0, column=0,padx=10, pady=10)
        self.btn.grid(row=0, column=1,padx=10, pady=10)
        self.btn.grid(row=1, column=0,padx=10, pady=10)
        self.edt.grid(row=1, column=1,padx=10, pady=10)
        self.sld.grid(row=2, column=0,padx=10, pady=10)

class BackgroundcolourFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(root)

        self.root = root


        self.colors = ['red','green','yellow']

        self.selected_color = tk.StringVar()
        self.selected_color.set(self.colors[0])

        self.radio_options = (tk.Radiobutton(self,
                                             text=color,
                                            value=color,
                                            variable=self.selected_color,
                                             command=self.change_color)
                              for color in self.colors)

        self.place_widgets2()

    def place_widgets2(self):

        for ro in self.radio_options:
            ro.pack(side=tk.LEFT, anchor='w', padx=(5,5), pady=5)

    def change_color(self):
        color = self.selected_color.get()
        self.config(bg=color)
        #self.root.config(bg=color)
        self.root.clicker_frame.config(bg=color)

if __name__ == '__main__':
    root = tk.Tk()
    root.title("Tkinter Class Examples")
    main_frame = MainFrame(root)
    background = BackgroundcolourFrame(root)
    background.pack()
    main_frame.pack()

    root.mainloop()