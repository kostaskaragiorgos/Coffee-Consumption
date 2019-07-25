from tkinter import *
from tkinter import messagebox as msg
from tkinter import simpledialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

import datetime
import csv
import os
import numpy

class Medical():
    def __init__(self,master):
        self.master = master
        self.master.title("MEICAL")
        self.master.geometry("200x100")
        self.master.resizable(False,False)
        self.now = datetime.datetime.today().strftime('%d-%m-%Y')
        if os.path.exists('coffee.csv') == False:
            with open('coffee.csv', 'a+') as f:
                thewriter = csv.writer(f)
                thewriter.writerow(['DAY','CAPS_OF_COFFEE'])
                f.close()
                
        if os.path.exists('water.csv') == False:
            with open('water.csv', 'a+') as w:
                thewriter = csv.writer(w)
                thewriter.writerow(['DAY','BOTTELS_OF_WATER(500ml)'])
                w.close()
        
        self.menumain = Menu(self.master)
        self.file_menumain = Menu(self.menumain,tearoff = 0)
        self.file_menumain.add_command(label = "COFFEE CONSUMPTION",accelerator = 'Ctrl+C',command = self.cof)
        self.file_menumain.add_command(label = "WATTER CONSUMPTION",accelerator = 'Ctrl+W',command = self.wat)
        self.file_menumain.add_command(label="Exit",accelerator = 'Alt+F4',command = self.exitmenu)
        self.menumain.add_cascade(label = "File",menu=self.file_menumain)
        
        self.showmenu = Menu(self.menumain,tearoff = 0)
        self.showmenu.add_command(label = "Show Comparison",command = self.comp)
        self.showmenu.add_command(label = "Show Water",command = self.watg)
        self.showmenu.add_command(label = "Show Coffee",command = self.cofg)
        self.menumain.add_cascade(label = "Show",menu = self.showmenu)
        
        self.about_menumain = Menu(self.menumain,tearoff = 0)
        self.about_menumain.add_command(label = "About",accelerator='Ctrl+I',command=self.aboutmenu)
        self.menumain.add_cascade(label="About",menu=self.about_menumain)
        
        self.help_menumain = Menu(self.menumain,tearoff = 0)
        self.help_menumain.add_command(label = "Help",accelerator = 'Ctrl+F1',command=self.helpmenu)
        self.menumain.add_cascade(label="Help",menu=self.help_menumain)
        
        self.master.config(menu=self.menumain)
        
        self.master.bind('<Control-c>',lambda event:self.cof())
        self.master.bind('<Control-w>',lambda event:self.wat())
        self.master.bind('<Alt-F4>',lambda event: self.exitmenu())
        self.master.bind('<Control-F1>',lambda event: self.helpmenu())
        self.master.bind('<Control-i>',lambda event:self.aboutmenu())
        
        self.coffee = Button(self.master,text = "COFFEE CONSUMPTION",command = self.cof)
        self.coffee.pack()
        
        self.water = Button(self.master,text = "WATER CONSUMPTION",command = self.wat)
        self.water.pack()

    def helpmenu(self):
        pass
    
    
    def exitmenu(self):
        if msg.askokcancel("Quit?", "Really quit?"):
            self.master.destroy()
            
    def aboutmenu(self):
        pass
    
    def wat(self):
        watcon = simpledialog.askinteger("BOTTLES OF WATER","Enter the number of bottles of the water you consume",parent = self.master,minvalue  = 1, maxvalue = 20)
        if watcon != None:
            with open('water.csv','a+') as u:
                thewriter = csv.writer(u)
                thewriter.writerow([self.now,str(watcon)])
                u.close()
    
    def cof(self):
        cofcon = simpledialog.askinteger("CUPS OF COFFEE","Enter the number of cups of the coffee you consume",parent = self.master,minvalue  = 1, maxvalue = 10)
        if cofcon != None:
            with open('coffee.csv','a+') as d:
                thewriter = csv.writer(d)
                thewriter.writerow([self.now,str(cofcon)])
                d.close()
    
    def cofg(self):
        dates = []
        values = []
        with open('coffee.csv','r') as dot:
            reader = csv.reader(dot)
            next(reader)
            for row in reader:
                dates.append(row[0])
                values.append(int(row[1]))
            dot.close()
        f = Figure(figsize=(4,5), dpi=100)
        ax = f.add_subplot(111)
        rects1 = ax.bar(dates,values)
        canvas = FigureCanvasTkAgg(f,Tk())
        canvas.get_tk_widget().pack()
                
    def watg(self):
        dates = []
        values = []
        with open('water.csv','r') as dot:
            reader = csv.reader(dot)
            next(reader)
            for row in reader:
                dates.append(row[0])
                values.append(int(row[1]))
            dot.close()
        f = Figure(figsize=(4,5), dpi=100)
        ax = f.add_subplot(111)
        rects1 = ax.bar(dates,values)
        canvas = FigureCanvasTkAgg(f,Tk())
        canvas.get_tk_widget().pack()
        
        
        
    def comp(self):
        cofsum,watsum = 0,0
        with open('coffee.csv','r') as o:
            reader = csv.reader(o)
            next(reader)
            for row in reader:
                cofsum += int(row[1])
            o.close()
        with open('water.csv','r') as wa:
            reader = csv.reader(wa)
            next(reader)
            for row in reader:
                watsum += int(row[1])
            wa.close()
        f = Figure(figsize=(4,5), dpi=100)
        ax = f.add_subplot(111)
        data = (cofsum,watsum)
        da = ("Coffee", "Water")
        ax.bar(da,data,color = ('r','b'))
        canvas = FigureCanvasTkAgg(f,Tk())
        canvas.get_tk_widget().pack()
def main():
    root=Tk()
    M= Medical(root)
    root.mainloop()
    
if __name__=='__main__':
    main()
    

        