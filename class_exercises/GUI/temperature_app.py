import tkinter as tk
from tkinter import ttk

class MainWindow(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.data
        self.title("Temperature App")
        self.temp_name = tk.Label(self, text="Temperatures")



class Temp_buttons(tk.Frame):
    def __init__(self,master):
        tk.Frame.__init__(self,master)
        self.temperatures = ["celsius", "fahrenheit", "kelvin","rankine","romer"]
        self.selected_input_temperature = tk.StringVar()
        self.selected_input_temperature.set(self.temperatures[0])

        self.ro_btns = [tk.Radiobutton(self, text=temp,value = temp, command=self.radio_select)for temp in self.temperatures]

        for ro in self.ro_btns:
            ro.pack(side=tk.RIGHT)

    def radio_select(self):
        print(f'You selected {self.selected_input_temperature.get()}')


class Background_color(tk.Frame):
    def __init__(self,master):
        tk.Frame.__init__(self,master)




if __name__ == '__main__':
    root = tk.Tk()
    root.geometry("500x500+100+100")