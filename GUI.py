import tkinter as tk
import os
import shunting_yard as sy
from tkinter import *

def temp(string):
    temp = tk.Frame(string, width=20, height=50)
    temp.pack()

def isnumeric(str):
    if str != '=' or str != 'AC' or str != 'Del':
        return True
    return False

def work(string):
    if isnumeric(string):
        with open("num.txt", 'a') as f:
            f.write(string)

def delete():
    # TODO: clean the last input.
    pass

def ac():
    # TODO: clean the whole string in num.txt and show 0 on screen.
    pass

def calculate(str):
    # TODO: connect with the shunting_yard.py and calculate the input string's answer in num.txt when user clicks on '='.
    pass

def run():
    if os.path.exists("num.txt") == False:
        with open("num.txt", 'w') as f:
            f.write('')
        
    global root
    root = tk.Tk()
    root.title("Calculator")
    
    root.geometry('400x500+760+290')
    top = tk.Frame(root, width=30, height=100)
    top.pack()
    
    global top_work
    temp(top)
    top_work = tk.Label(top, text='', justify='left', relief=SUNKEN, bd=10, bg='white', width=40)
    top_work.pack(side='bottom')
    temp(root)
    
    number = tk.Frame(root)
    number.pack()
    # screen constuctor
    # TODO: show the input (translate.py to translate string in num.txt to mathemetical expression, maybe running delay increase.)
    # button constructor
    # when clicking on these buttons, it will write inputs on num.txt and show on the screen in calculator GUI.
    tk.Button(number, text="sqrt",   width=10, command=lambda:work('l(')).grid(row=0,column=0)
    tk.Button(number, text="square", width=10, command=lambda:work('i(')).grid(row=0, column=1)
    tk.Button(number, text="cube",   width=10, command=lambda:work('j(')).grid(row=0, column=2)
    tk.Button(number, text="^",      width=10, command=lambda:work('^')).grid(row=0, column=3)
    
    tk.Button(number, text="log",    width=10, command=lambda:work('n(')).grid(row=1, column=0)
    tk.Button(number, text="sin",    width=10, command=lambda:work('c(')).grid(row=1, column=1)
    tk.Button(number, text="cos",    width=10, command=lambda:work('d(')).grid(row=1, column=2)
    tk.Button(number, text="tan",    width=10, command=lambda:work('e(')).grid(row=1, column=3)
    
    tk.Button(number, text="ln",     width=10, command=lambda:work('o(')).grid(row=2, column=0)
    tk.Button(number, text="arcsin", width=10, command=lambda:work('f(')).grid(row=2, column=1)
    tk.Button(number, text="arccos", width=10, command=lambda:work('g(')).grid(row=2, column=2)
    tk.Button(number, text="arctan", width=10, command=lambda:work('h(')).grid(row=2, column=3)
    
    tk.Button(number, text="abs",    width=10, command=lambda:work('p(')).grid(row=3, column=0)
    tk.Button(number, text="(",      width=10, command=lambda:work('(')).grid(row=3, column=1)
    tk.Button(number, text=")",      width=10, command=lambda:work(')')).grid(row=3, column=2)
    tk.Button(number, text="ftr",    width=10, command=lambda:work('q(')).grid(row=3, column=3)
    
    tk.Button(number, text="e",      width=10, command=lambda:work('b')).grid(row=4, column=0)
    tk.Button(number, text="pi",     width=10, command=lambda:work('a')).grid(row=4, column=1)
    tk.Button(number, text="Del",    width=10, command=lambda:delete()).grid(row=4, column=2)
    tk.Button(number, text="Ac",     width=10, command=lambda:ac()).grid(row=4, column=3)

    tk.Button(number, text="7",      width=10, command=lambda:work('7')).grid(row=5, column=0)
    tk.Button(number, text="8",      width=10, command=lambda:work('8')).grid(row=5, column=1)
    tk.Button(number, text="9",      width=10, command=lambda:work('9')).grid(row=5, column=2)
    tk.Button(number, text="*",      width=10, command=lambda:work('*')).grid(row=5, column=3)

    tk.Button(number, text="4",      width=10, command=lambda:work('4')).grid(row=6, column=0)
    tk.Button(number, text="5",      width=10, command=lambda:work('5')).grid(row=6, column=1)
    tk.Button(number, text="6",      width=10, command=lambda:work('6')).grid(row=6, column=2)
    tk.Button(number, text="/",      width=10, command=lambda:work('/')).grid(row=6, column=3)

    tk.Button(number, text="1",      width=10, command=lambda:work('1')).grid(row=7, column=0)
    tk.Button(number, text="2",      width=10, command=lambda:work('2')).grid(row=7, column=1)
    tk.Button(number, text="3",      width=10, command=lambda:work('3')).grid(row=7, column=2)
    tk.Button(number, text="+",      width=10, command=lambda:work('+')).grid(row=7, column=3)

    tk.Button(number, text="0",      width=10, command=lambda:work('0')).grid(row=8, column=0)
    tk.Button(number, text=".",      width=10, command=lambda:work('.')).grid(row=8, column=1)
    tk.Button(number, text="=",      width=10, command=lambda:calculate()).grid(row=8, column=2)
    tk.Button(number, text="-",      width=10, command=lambda:work('-')).grid(row=8, column=3)
    
    root.mainloop()
run()