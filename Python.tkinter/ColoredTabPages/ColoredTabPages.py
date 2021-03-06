#!/usr/bin/env python3
# -*-coding:utf-8 -*

import tkinter
import tkinter.ttk

class Form1(tkinter.Tk):
  def __init__(self):
    super().__init__()
    
    self.frame = tkinter.ttk.Frame(self)
    self.frame.pack(fill = tkinter.BOTH, expand=1)

    self.tabControl = tkinter.ttk.Notebook(self.frame, width=320, height=200)
    self.tabControl.place(x=10, y=10)

    self.tabPageRed = tkinter.Frame(self.tabControl, background='red')
    self.tabControl.add(self.tabPageRed, text='Red')
    
    self.tabPageGreen = tkinter.Frame(self.tabControl, background='green')
    self.tabControl.add(self.tabPageGreen, text='Green')
    
    self.tabPageBlue = tkinter.Frame(self.tabControl, background='blue')
    self.tabControl.add(self.tabPageBlue, text='Blue')
    
    self.tabPageYellow = tkinter.Frame(self.tabControl, background='yellow')
    self.tabControl.add(self.tabPageYellow, text='Yellow')
    
    self.geometry("390x270+200+100")
    self.title("Colored TabPages example")

  def main(self=None):
    form = Form1()
    form.mainloop()

if __name__ == '__main__':
  Form1.main()
