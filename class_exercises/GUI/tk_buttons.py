import tkinter as tk


class ClickApp(tk.Tk):
    """ Button clicker application """

    def __init__(self):
        # Initialised the tk.Tk app superclass
        super().__init__()
        self.title('Click Counter')
        self.clicker_frame = ButtonClicker(self)
        self.background_color_frame = BackgroundColorFrame(self)

        self.clicker_frame.pack(side=tk.LEFT)
        self.background_color_frame.pack(side=tk.LEFT)


class BackgroundColorFrame(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        # Color choices
        self.colors = ['red', 'green', 'yellow']

        # Create a tk variable which will hold the value of the selcted color
        self.selected_color = tk.StringVar()
        self.selected_color.set(self.colors[0])

        # Create radio buttons (list comprehension)
        self.radio_options = [tk.Radiobutton(self, text=color,
                                             value=color,
                                             variable=self.selected_color,
                                             command=self.change_color)
                              for color in self.colors]

        self.place_widgets()

    def place_widgets(self):
        for ro in self.radio_options:
            ro.pack(side=tk.TOP, anchor='w', padx=(5, 10), pady=5)




class ButtonClicker(tk.Frame):
    """ Frame with button clicker widgets """

    def __init__(self, master):
        super().__init__(master)
        self.counter = 0

        self.txt = tk.Label(self, text='Press Here!')
        self.btn = tk.Button(self, text="Click me!", command=self.click_button())
        self.response_txt = tk.Label(self, text='No Clicks')
        self.config(bg="cyan2")

        self.place_widgets()

    def place_widgets(self):
        settings = {'padx': 10, 'pady': 10}
        self.txt.pack(side=tk.TOP, **settings)
        self.btn.pack(side=tk.TOP,**settings)
        self.response_txt.pack(side=tk.TOP, **settings)


    def click_button(self):
        self.counter += 1
        print(self.counter)
        self.response_txt.config(text=self.counter)

if __name__ == '__main__':
    app = ClickApp()
    app.mainloop()
