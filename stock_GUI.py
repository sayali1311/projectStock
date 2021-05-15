import tkinter as tk
from tkinter import font  as tkfont 
import pandas as pd
import pickle
import warnings
warnings.filterwarnings("ignore")

master = tk.Tk()

tk.Label(master, text="Stock Price Predictor", font=tkfont.Font(size=35)).grid(row=0, columnspan=2)
tk.Label(master, text="Enter the Following Data", font=tkfont.Font(size=20)).grid(row=1, columnspan=2)


tk.Label(master, text="Enter Open Value").grid(row=2)
tk.Label(master, text="Enter High Value").grid(row=3)
tk.Label(master, text="Enter Close Value").grid(row=4)

e1 = tk.Entry(master)
e2 = tk.Entry(master)
e3 = tk.Entry(master)


e1.grid(row=2, column=1)
e2.grid(row=3, column=1)
e3.grid(row=4, column=1)

l1=tk.Label(master)
l1.grid(row=6, column=0)


def fun():
    
    p1 = e1.get()+","+e2.get()+","+e3.get()
    p2 = "open"+","+"high"+","+"low"+"\n"
    file = open("save_X.csv","w")
    file.write(p2)
    file.write(p1)
    file.close()

   
    df = pd.read_csv("save_X.csv")
    
  
    filename = 'pickle_model'
    loaded_model = pickle.load(open(filename, 'rb'))
    
    pred = loaded_model.predict(df)
    l1.configure(text=pred)



button = tk.Button(master, 
                   text="PREDICT", font=tkfont.Font(size=15), 
                   fg="blue", command=fun).grid(row=5, columnspan=2)

tk.mainloop()
