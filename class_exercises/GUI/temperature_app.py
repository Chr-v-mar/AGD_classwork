import tkinter as tk
from tkinter import ttk

class MainWindow(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Temperature App")
        self.temp_name = tk.Label(self, text="Temperatures")



class Temp_buttons(tk.Frame):
    def __init__(self,master):
        tk.Frame.__init__(self,master)
        self.temperatures = ["Kelvin","Fahrenheit","Celsius"]
        self.selected_temperature = tk.StringVar()
        self.selected_temperature.set(self.temperatures[0])

        self.ro_btns = [tk.Radiobutton(self, text=temp,value = temp, command=self.radio_select)for temp in self.temperatures]

        self.place_widgets

    def place_widgets(self):
        for ro in self.ro_btns:
            ro.pack(side=tk.RIGHT, anchor=tk.SE)

class Background_color(tk.Frame):
    def __init__(self,master):
        tk.Frame.__init__(self,master)



if __name__ == '__main__':
    root = tk.Tk()
    root.geometry("500x500+100+100")