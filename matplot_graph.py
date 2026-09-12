from tkinter import *
import numpy as np
import matplotlib.pyplot as plt


root = Tk()
root.title("Plot A Graph")
root.geometry("400x400")
root.resizable(width=False, height=False)

#200000, 25000, 5000
def graph():
  house_prices = np.random.normal(200000,25000,5000)#location,scale,size. np provides array of numbers, normal draws a random samples from normal (Gaussian)distribution.
  plt.bar(house_prices, 50)#x-axis,bins. hist is histogram
  #plt.pie(house_prices, 50)
  plt.show()#to show the graph. It replaces label here.

my_button = Button(root, text="Graphic",command=graph)
my_button.pack()



root.mainloop()