from tkinter import Tk, Button, Menu
from tkinter import messagebox as msg
from tkinter import simpledialog
import datetime
import csv
import os
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
def helpmenu():
    """ help menu function """
    msg.showinfo("Help", "Use push the buttons to track your consumption")
def aboutmenu():
    """ about menu function """
    msg.showinfo("About", "Medical \nVersion 2.0")
class Medical():
    """ Medical class """
    def __init__(self, master):
        self.master = master
        self.master.title("MEICAL")
        self.master.geometry("200x100")
        self.master.resizable(False, False)
        self.now = datetime.datetime.today().strftime('%d-%m-%Y')
        if not os.path.exists('coffee.csv'):
            with open('coffee.csv', 'a+') as f:
                thewriter = csv.writer(f)
                thewriter.writerow(['DAY', 'CAPS_OF_COFFEE']) 
        if not os.path.exists('water.csv'):
            with open('water.csv', 'a+') as w:
                thewriter = csv.writer(w)
                thewriter.writerow(['DAY', 'BOTTELS_OF_WATER(500ml)'])
        #menu
        self.menumain = Menu(self.master)
        self.file_menumain = Menu(self.menumain, tearoff=0)
        self.file_menumain.add_command(label="COFFEE CONSUMPTION", accelerator='Ctrl+C', command=self.cof)
        self.file_menumain.add_command(label="WATER CONSUMPTION", accelerator='Ctrl+W', command=self.wat)
        self.file_menumain.add_command(label="Exit", accelerator='Alt+F4', command=self.exitmenu)
        self.menumain.add_cascade(label="File", menu=self.file_menumain)
        self.showmenu = Menu(self.menumain, tearoff=0)
        self.showmenu.add_command(label="Show Comparison", accelerator='Alt+S', command=self.comp)
        self.showmenu.add_command(label="Show Water", accelerator='Alt+W', command=self.watg)
        self.showmenu.add_command(label="Show Coffee", accelerator='Alt+C', command=self.cofg)
        self.menumain.add_cascade(label="Show", menu=self.showmenu)
        self.about_menumain = Menu(self.menumain, tearoff=0)
        self.about_menumain.add_command(label="About", accelerator='Ctrl+I', command=aboutmenu)
        self.menumain.add_cascade(label="About", menu=self.about_menumain)        
        self.help_menumain = Menu(self.menumain, tearoff=0)
        self.help_menumain.add_command(label="Help", accelerator='Ctrl+F1', command=helpmenu)
        self.menumain.add_cascade(label="Help", menu=self.help_menumain)
        self.master.config(menu=self.menumain)
        self.master.bind('<Alt-s>', lambda event: self.comp())
        self.master.bind('<Alt-w>', lambda event: self.watg())
        self.master.bind('<Alt-c>', lambda event: self.cofg())
        self.master.bind('<Control-c>', lambda event: self.cof())
        self.master.bind('<Control-w>', lambda event: self.wat())
        self.master.bind('<Alt-F4>', lambda event: self.exitmenu())
        self.master.bind('<Control-F1>', lambda event: helpmenu())
        self.master.bind('<Control-i>', lambda event: aboutmenu())
        self.coffee = Button(self.master, text="COFFEE CONSUMPTION", command=self.cof)
        self.coffee.pack()     
        self.water = Button(self.master, text="WATER CONSUMPTION", command=self.wat)
        self.water.pack()
    def exitmenu(self):
        """ exit menu function """
        if msg.askokcancel("Quit?", "Really quit?"):
            self.master.destroy()
    def wat(self):
        """ watter consumption button function """
        watcon = simpledialog.askinteger("BOTTLES OF WATER", "Enter the number of bottles of the water you consume", parent=self.master, minvalue=1, maxvalue=20)
        if not watcon is None:
            with open('water.csv', 'a+') as u:
                thewriter = csv.writer(u)
                thewriter.writerow([self.now, str(watcon)])
    def cof(self):
        """ coffee consumption button function """
        cofcon = simpledialog.askinteger("CUPS OF COFFEE", "Enter the number of cups of the coffee you consume", parent=self.master, minvalue=1, maxvalue=10)
        if not cofcon is None:
            with open('coffee.csv', 'a+') as d:
                thewriter = csv.writer(d)
                thewriter.writerow([self.now, str(cofcon)])
    def cofg(self):
        dates = []
        values = []
        with open('coffee.csv', 'r') as dot:
            reader = csv.reader(dot)
            next(reader)
            for row in reader:
                dates.append(row[0])
                values.append(int(row[1]))
        f = Figure(figsize=(4, 5), dpi=100)
        ax = f.add_subplot(111)
        ax.bar(dates, values)
        canvas = FigureCanvasTkAgg(f, Tk())
        canvas.get_tk_widget().pack()
    def watg(self):
        dates = []
        values = []
        with open('water.csv', 'r') as dot:
            reader = csv.reader(dot)
            next(reader)
            for row in reader:
                dates.append(row[0])
                values.append(int(row[1]))
        f = Figure(figsize=(4, 5), dpi=100)
        ax = f.add_subplot(111)
        ax.bar(dates, values)
        canvas = FigureCanvasTkAgg(f, Tk())
        canvas.get_tk_widget().pack()
    def comp(self):
        cofsum, watsum = 0, 0
        with open('coffee.csv', 'r') as o:
            reader = csv.reader(o)
            next(reader)
            for row in reader:
                cofsum += int(row[1])
            o.close()
        with open('water.csv', 'r') as wa:
            reader = csv.reader(wa)
            next(reader)
            for row in reader:
                watsum += int(row[1])
        f = Figure(figsize=(4, 5), dpi=100)
        ax = f.add_subplot(111)
        data = (cofsum, watsum)
        da = ("Coffee", "Water")
        ax.bar(da, data, color=('r', 'b'))
        canvas = FigureCanvasTkAgg(f, Tk())
        canvas.get_tk_widget().pack()
def main():
    """ main function """
    root = Tk()
    Medical(root)
    root.mainloop()
if __name__ == '__main__':
    main()
    

        
