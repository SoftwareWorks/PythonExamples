#!/usr/bin/env python3
# -*-coding:utf-8 -*

import tkinter
import tkinter.ttk

class Form1(tkinter.Tk):
  def __init__(self):
    super().__init__()
  
    self.panel = tkinter.ttk.Frame(self)
    self.panel.pack(fill = tkinter.BOTH, expand=1)

    self.checkBoxVar1 = tkinter.BooleanVar()
    self.checkBoxVar1.set(True)
    
    self.checkBox1 = tkinter.ttk.Checkbutton(self.panel, text="Checked", variable=self.checkBoxVar1)
    self.checkBox1.place(x = 30, y = 30) 
    
    self.checkBoxVar2 = tkinter.BooleanVar()
    self.checkBoxVar2.set(False)
    
    self.checkBox2 = tkinter.ttk.Checkbutton(self.panel, text="Unchecked", variable=self.checkBoxVar2)
    self.checkBox2.place(x = 30, y = 60) 
    
    self.checkBox3 = tkinter.ttk.Checkbutton(self.panel, text="Indeterminate", variable=None)
    self.checkBox3.place(x = 30, y = 90) 

    self.geometry("300x300+200+100")
    self.title("CheckBox Example")

  def main(self=None):    
    form = Form1()
    form.mainloop()
 
if __name__ == '__main__':
  Form1.main()
  
