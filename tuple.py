# -*- coding: utf-8 -*-
"""
Created on Sat Jul 10 20:00:14 2021

@author: USER
"""

from tkinter import *
root=Tk()
root.title("Tuple")
root.geometry("400x400")
lab1=Label(root,text="Tuple")
lab1.place(relx=0.5,rely=0.1,anchor=CENTER)
months=("January","February","March","April","May","June","July","August","September","October","November","December")
profits=(10000,20000,25000,35400,95200,42000,14000,45000,48500,10085,41000,58000)
max_value=max(profits)
max_index=profits.index(max_value)
min_value=min(profits)
min_index=profits.index(min_value)
lab_min=Label(root)
lab_max=Label(root)
lab_min['text']="Minimum profit of "+str(min_value)+" was recorded in the month of "+str(months[min_index])
lab_max['text']="Maximum profit of "+str(max_value)+" was recorded in the month of "+str(months[max_index])
lab_max.place(relx=0.5,rely=0.4,anchor=CENTER)
lab_min.place(relx=0.5,rely=0.5,anchor=CENTER)
root.mainloop()