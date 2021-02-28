from tkinter import *
import random
import os
import time
from PIL import Image,ImageTk
from tkinter import messagebox


root = Tk()
root.title("sudoko game bitch!")
root.geometry("500x500")

class GameButton(Button):
    def __init__(self,parent,row, column, **config):
        Button.__init__(self,parent,config)
        self.grid(row = row, column = column)
        self.bind("<Button-1>", self.change)
        self.bind("<Button-3>", self.change_back)
        self.configure(width = 4, height = 2, bg = "#272822", fg = "#ffffff")
        self.row = row
        self.column = column
        self.bg = "#272822"

    def change(self, bind_var):
        self.config(bg = "#9a9a94")
        self.bg = "#9a9a94"

    def change_back(self, bind_var):
        self.config(bg = "#272822")

class NumberButton(Button):
    def __init__(self,parent,row,column,number,**config):
        Button.__init__(self,parent,config)
        self.grid(row = row, column = column)
        self.config(text = str(number))
        self.config(width = 4,height = 2, bg = "#ccccc1", fg = "#000000")
        self.number = str(number)
        self.config(command = lambda :do_number(self.number))


button1 = GameButton(root,0,0)
button2 = GameButton(root,0,1)
button3 = GameButton(root,0,2)
button4 = GameButton(root,0,3)
button5 = GameButton(root,0,4)
button6 = GameButton(root,0,5)
button7 = GameButton(root,0,6)
button8 = GameButton(root,0,7)
button9 = GameButton(root,0,8)

button10 = GameButton(root,1,0)
button11 = GameButton(root,1,1)
button12 = GameButton(root,1,2)
button13 = GameButton(root,1,3)
button14 = GameButton(root,1,4)
button15 = GameButton(root,1,5)
button16 = GameButton(root,1,6)
button17 = GameButton(root,1,7)
button18 = GameButton(root,1,8)

button19 = GameButton(root,2,0)
button20 = GameButton(root,2,1)
button21 = GameButton(root,2,2)
button22 = GameButton(root,2,3)
button23 = GameButton(root,2,4)
button24 = GameButton(root,2,5)
button25 = GameButton(root,2,6)
button26 = GameButton(root,2,7)
button27 = GameButton(root,2,8)

button28 = GameButton(root,3,0)
button29 = GameButton(root,3,1)
button30 = GameButton(root,3,2)
button31 = GameButton(root,3,3)
button32 = GameButton(root,3,4)
button33 = GameButton(root,3,5)
button34 = GameButton(root,3,6)
button35 = GameButton(root,3,7)
button36 = GameButton(root,3,8)

button37 = GameButton(root,4,0)
button38 = GameButton(root,4,1)
button39 = GameButton(root,4,2)
button40 = GameButton(root,4,3)
button41 = GameButton(root,4,4)
button42 = GameButton(root,4,5)
button43 = GameButton(root,4,6)
button44 = GameButton(root,4,7)
button45 = GameButton(root,4,8)

button46 = GameButton(root,5,0)
button47 = GameButton(root,5,1)
button48 = GameButton(root,5,2)
button49 = GameButton(root,5,3)
button50 = GameButton(root,5,4)
button51 = GameButton(root,5,5)
button52 = GameButton(root,5,6)
button53 = GameButton(root,5,7)
button54 = GameButton(root,5,8)

button55 = GameButton(root,6,0)
button56 = GameButton(root,6,1)
button57 = GameButton(root,6,2)
button58 = GameButton(root,6,3)
button59 = GameButton(root,6,4)
button60 = GameButton(root,6,5)
button61 = GameButton(root,6,6)
button62 = GameButton(root,6,7)
button63 = GameButton(root,6,8)

button64 = GameButton(root,7,0)
button65 = GameButton(root,7,1)
button66 = GameButton(root,7,2)
button67 = GameButton(root,7,3)
button68 = GameButton(root,7,4)
button69 = GameButton(root,7,5)
button70 = GameButton(root,7,6)
button71 = GameButton(root,7,7)
button72 = GameButton(root,7,8)

button73 = GameButton(root,8,0)
button74 = GameButton(root,8,1)
button75 = GameButton(root,8,2)
button76 = GameButton(root,8,3)
button77 = GameButton(root,8,4)
button78 = GameButton(root,8,5)
button79 = GameButton(root,8,6)
button80 = GameButton(root,8,7)
button81 = GameButton(root,8,8)


buttons = [button1,button2,button3,button4,button5,button6,button7,button8,
button9,button10,button11,button12,button13,button14,button15,button16,button17,button18,
button19,button20,button21,button22,button23,button24,button25,button26,button27,button28,
button29,button30,button31,button32,button33,button34,button35,button36,button37,button38,
button39,button40,button41,button42,button43,button44,button45,button46,button47,button48,
button49,button50,button51,button52,button53,button54,button55,button56,button57,button58,
button59,button60,button61,button62,button63,button64,button65,button66,button67,button68,
button69,button70,button71,button72,button73,button74,button75,button76,button77,button78,
button79,button80,button81]


def do_number(number):
    for button in buttons:
        if button.bg == "#9a9a94":
            button.configure(text = number)
            button.configure(bg = "#272822")
            button.bg = "#272822"

button_number_1 = NumberButton(root,9,0,1)
button_number_2 = NumberButton(root,9,1,2)
button_number_3 = NumberButton(root,9,2,3)
button_number_4 = NumberButton(root,9,3,4)
button_number_5 = NumberButton(root,9,4,5)
button_number_6 = NumberButton(root,10,0,6)
button_number_7 = NumberButton(root,10,1,7)
button_number_8 = NumberButton(root,10,2,8)
button_number_9 = NumberButton(root,10,3,9)

root.mainloop()