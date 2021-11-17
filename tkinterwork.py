from tkinter import *
from tkinter import messagebox
from functools import partial
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

main_window = Tk()
main_window.title('My first App Window')
main_window.geometry('750x350')

def Hist_plot():
    messagebox.showinfo('Data Science','Welcome You All')
    v1=int(e1.get())
    v2=int(e2.get())
    v3=int(e3.get())
    x=np.random.normal(v1,v2,v3)

    figure=plt.figure(figsize=(5,4),dpi=100)
    figure.add_subplot(111).hist(x)
    chart=FigureCanvasTkAgg(figure,main_window)
    chart.get_tk_widget().grid(row=6,column=0)

Lab1=Label(main_window,text='Enter your value for random number')
Lab1.grid(row=0,column=0)
e1=Entry(main_window)
e1.grid(row=0,column=1)

Lab2=Label(main_window,text='Standard Deviation')
Lab2.grid(row=1,column=0)
e2=Entry(main_window)
e2.grid(row=1,column=1)

Lab3=Label(main_window,text='Number of Value required')
Lab3.grid(row=2,column=0)
e3=Entry(main_window)
e3.grid(row=2,column=1)

B=Button(main_window,text='Click Here',command=partial(Hist_plot))
B.grid(row=4,column=8)
#B.place(x=10,y=65)
main_window.mainloop()