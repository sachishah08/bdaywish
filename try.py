import tkinter as tk
from tkinter import *
import os
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import sys
import datetime

# if you are still working under a Python 2 version, 
# comment out the previous line and uncomment the following line
# import Tkinter as tk

root = tk.Tk()

w = tk.Label(root, text="Enter name of your friend")
e1=Entry(root)
x = tk.Label(root, text="Enter birthdate of your friend")

y=tk.Label(root,text="Month")
e2=Entry(root)
z=tk.Label(root,text="Day")
e3=Entry(root)

def receive_input():
	
	name=e1.get()
	with open('names.txt', 'a') as the_file:
    		the_file.write(name+'\n')
	month=e2.get()
	date=e3.get()
	with open('bday.txt','a') as f:
		f.write(month+' '+date+'\n')
	print(name)
	print(month+' '+date)
def call_script():
    os.system('python wa.py')
btn=Button(root,text="Save",command=lambda:receive_input())
btn1=Button(root,text="Go",command=lambda:call_script())
print("sachi shah")
w.pack()
e1.pack()
x.pack()
y.pack()
e2.pack()
z.pack()
e3.pack()
btn.pack()
btn1.pack()
root.mainloop()