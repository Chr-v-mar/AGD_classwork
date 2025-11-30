import tkinter as tk
from Temperature import Temperature as Temp
from tkinter import ttk, StringVar


class MainWindow(tk.Frame):
    def __init__(self,master):
        super().__init__(master)
        self.Temp = Temp
        self.outputTemps = []
        self.temperature = tk.StringVar()
        self.temp_symbols = []
        self.temp_in_frame = Temp_buttons(self)
        self.temp_in = 'celsius'
        self.temp_in = self.temp_in_frame.selected_input_temperature.get()
        self.temperatures = ["celsius", "fahrenheit", "kelvin", "rankine", "romer"]
        self.tempVar = tk.StringVar()
        self.tempVar.set("Select temperature to convert to")

        text_labels = ["Temperature", "Value", "Conversion","Output"]

        self.labels = [tk.Label(self, text=text_label,
                                justify=tk.LEFT,
                                font=('Arial', 12))
                       for text_label in text_labels]
        self.convert_button = tk.Button(self, text="Convert Temperature",
                                        bg="green",
                                        fg="white",
                                        font=('Arial', 12),
                                        command=self.TempConverter,
                                        activebackground="medium spring green")
        self.inputTemp = tk.Entry(self,textvariable= self.temperature  ,width=20, font=('Arial', 12),)
        self.outputTempOptions = ttk.Combobox(self,
                                       textvariable=self.tempVar,
                                       values=self.temperatures, )
        self.outputTempOptions.config(width=20,font=('Arial', 12))
        self.outputTemp = tk.Label(self,text=f"{self.TempOutputGet()}")
        self.outputTempOptions.bind('<<ComboboxSelected>>', self.combo_select)
        self.conversion_labels = []

        self.place_widgets()

    def TempConverter(self):
        match self.temp_in:
            case "c":
                self.Temp.celsius = self.temperature

            case "f":
                self.Temp.fahrenheit = self.temperature

            case "k":
                self.Temp.kelvin = self.temperature

            case "ra":
                self.Temp.rankine = self.temperature

            case "ro":
                self.Temp.romer = self.temperature


    def TempOutputGet(self):
        match self.outputTempOptions.get():
            case "celsius":
                return self.Temp.celsius
            case "fahrenheit":
                return self.Temp.fahrenheit
            case "kelvin":
                return self.Temp.kelvin
            case "rankine":
                return self.Temp.rankine
            case "romer":
                return self.Temp.romer
            case _:
                return 0


    def place_widgets(self):
        self.labels[0].grid(row=0, column=0, columnspan=2, padx=10, pady=3, sticky="w")
        for i, label in enumerate(self.labels[1:], 1):
            label.grid(row=i, column=0, padx=10, pady=3, sticky="w")
        self.convert_button.grid(row=len(self.labels), column=1, padx=15, pady=(3, 10),sticky="w")
        self.inputTemp.grid(row=1, column=3, padx=(10, 25), pady=3, sticky="we")
        self.outputTempOptions.grid(row=2, column=3, padx=(10, 25), pady=3, sticky="we")
        self.temp_in_frame.grid(row=0, column=3, padx=10, pady=3, sticky="w")
        self.outputTemp.grid(row=3, column=3, padx=10, pady=3, sticky="we")

    def combo_select(self, event):
        # Call back for selecting the country combo-box item
        print(f'You selected {self.tempVar.get()}')

class Temp_buttons(tk.Frame):
    def __init__(self,master):
        tk.Frame.__init__(self,master)
        self.temperatures = [("celsius","c"), ("fahrenheit","f"), ("kelvin","k"),("rankine","ra"),("romer","ro")]
        self.selected_input_temperature = tk.StringVar()
        self.selected_input_temperature.set("c")

        self.ro_btns = [tk.Radiobutton(self, text=temp[0], value = temp[1], variable=self.selected_input_temperature, command=self.radio_select) for temp in self.temperatures]

        for ro in self.ro_btns:
            ro.pack(side=tk.RIGHT)



    def radio_select(self):
        print(f'You selected {self.selected_input_temperature.get()}')


class Background_color(tk.Frame):
    def __init__(self,master):
        tk.Frame.__init__(self,master)




if __name__ == "__main__":
    root = tk.Tk()
    root.title('Temperature App')
    root.resizable(1, 0)
    reg_frame = MainWindow(root).pack(fill=tk.BOTH, expand=True)
    root.mainloop()