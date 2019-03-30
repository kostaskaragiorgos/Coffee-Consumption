from tkinter import *
from tkinter import messagebox as msg
import datetime
import csv
import os
class Medical():
    def __init__(self,master):
        self.master = master
        self.master.title("MEICAL")
        self.master.geometry("200x100")
        self.master.resizable(False,False)
        self.menumain = Menu(self.master)
        self.file_menumain = Menu(self.menumain)
        self.file_menumain.add_command(label="Exit",command = self.exitmenumain)
        self.menumain.add_cascade(label = "File",menu=self.file_menumain)
        
        self.about_menumain = Menu(self.menumain)
        self.about_menumain.add_command(label = "About",command=self.aboutmenumain)
        self.menumain.add_cascade(label="About",menu=self.about_menumain)
        self.master.config(menu=self.menumain)
        self.coffee = Button(self.master,text = "COFFEE CONSUMPTION",command = self.cof)
        self.coffee.pack()
        self.water = Button(self.master,text = "WATER CONSUMPTION",command = self.wat)
        self.water.pack()
        self.exer = Button(self.master,text = "EXERCISE COUNTER",command = self.exerc)
        self.exer.pack()
    
    def exitmenumain(self):
        if msg.askokcancel("Quit?", "Really quit?"):
            self.master.destroy()
            
    def aboutmenumain(self):
        msg.showinfo("About MY MED","Main Window")
    
    
    def exerc(self):
        root4 = Toplevel()
        makeexerc = ExerciseCounter(root4)
    
    def wat(self):
        root3 = Toplevel()
        makwat = WaterCounter(root3)
    
    def cof(self):
        root2 = Toplevel()
        makcof = CoffeeCounter(root2)
        
class CoffeeCounter():
    def __init__(self,master):
        self.master = master
        self.master.title("COFFEE COUNTER")
        self.master.geometry("200x150")
        self.master.resizable(False,False)
        if os.path.exists('coffee.csv') == False:
            with open('coffee.csv', 'a+') as f:
                thewriter = csv.writer(f)
                thewriter.writerow(['DAY','CAPS_OF_COFFEE'])
                f.close()
                
        self.menu = Menu(self.master)
        self.file_menu = Menu(self.menu)
        self.file_menu.add_command(label="Exit",command = self.exitmenu)
        self.menu.add_cascade(label = "File",menu=self.file_menu)
        
        self.about_menu = Menu(self.menu)
        self.about_menu.add_command(label = "About",command=self.aboutmenu)
        self.menu.add_cascade(label="About",menu=self.about_menu)
        self.master.config(menu=self.menu)
        
        self.welleb = Label(self.master,text="Welcome to coffee counter")
        self.welleb.pack()
        self.cofslider = Scale(self.master,from_=0 , to = 10,orient= HORIZONTAL)
        self.cofslider.pack()
        self.submit = Button(self.master,text = "SUBMIT",command = self.submitc)
        self.submit.pack()
        
    def exitmenu(self):
        if msg.askokcancel("Quit?", "Really quit?"):
            self.master.destroy()
    def aboutmenu(self):
        msg.showinfo("About Coffee counter","Coffee counter,"
                     +"counts the cups of coffee you are drinking per day ")
    
    def submitc(self):
        now = datetime.datetime.today().strftime('%d-%m-%Y')
        with open('coffee.csv','a+') as d:
            thewriter = csv.writer(d)
            thewriter.writerow([now,str(self.cofslider.get())])
            d.close()
        msg.showinfo("Coffee Consumption ","DATE:"+now+"\nNumber:"+str(self.cofslider.get()))

class WaterCounter():
    def __init__(self,master):
        
        self.master = master
        self.master.title("WATER COUNTER")
        self.master.geometry("200x200")
        self.master.resizable(False,False)
        self.menuwat = Menu(self.master)
        self.file_menuwat = Menu(self.menuwat)
        self.file_menuwat.add_command(label="Exit",command = self.exitmenuwat)
        self.menuwat.add_cascade(label = "File",menu=self.file_menuwat)
        
        self.about_menuwat = Menu(self.menuwat)
        self.about_menuwat.add_command(label = "About",command=self.aboutmenuwat)
        self.menuwat.add_cascade(label="About",menu=self.about_menuwat)
        self.master.config(menu=self.menuwat)
        if os.path.exists('water.csv') == False:
            with open('water.csv', 'a+') as f:
                thewriter = csv.writer(f)
                thewriter.writerow(['DAY','BOTTELS_OF_WATER(500ml)'])
                f.close()
        self.welleb = Label(self.master,text="Welcome to water counter")
        self.welleb.pack()
        self.watslider = Scale(self.master,from_=0 , to = 20,orient= HORIZONTAL)
        self.watslider.pack()
        self.submit = Button(self.master,text = "SUBMIT",command = self.submitc)
        self.submit.pack()
        
    def exitmenuwat(self):
        if msg.askokcancel("Quit?", "Really quit?"):
            self.master.destroy()
            
    def aboutmenuwat(self):
        msg.showinfo("About Water counter","Water counter,"
                     +"counts the bottles of water you are drinking per day ")
    
    def submitc(self):
        now = datetime.datetime.today().strftime('%d-%m-%Y')
        with open('water.csv','a+') as d:
            thewriter = csv.writer(d)
            thewriter.writerow([now,str(self.watslider.get())])
            d.close()
        msg.showinfo("Water Consumption ","DATE:"+now+"\nNumber:"+str(self.watslider.get()))


class ExerciseCounter():
    def __init__(self,master):
        
        self.master = master
        self.master.title("EXERCISE COUNTER")
        self.master.geometry("200x200")
        self.master.resizable(False,False)
        self.menuexer = Menu(self.master)
        self.file_menuexer = Menu(self.menuexer)
        self.file_menuexer.add_command(label="Exit",command = self.exitmenuexer)
        self.menuexer.add_cascade(label = "File",menu=self.file_menuexer)
        
        self.about_menuexer = Menu(self.menuexer)
        self.about_menuexer.add_command(label = "About",command=self.aboutmenuexer)
        self.menuexer.add_cascade(label="About",menu=self.about_menuexer)
        self.master.config(menu=self.menuexer)
        if os.path.exists('exercise.csv') == False:
            with open('exercise.csv', 'a+') as f:
                thewriter = csv.writer(f)
                thewriter.writerow(['DAY','MINUTES_OF_EXERCISE'])
                f.close()
        self.welleb = Label(self.master,text="Welcome to exercise counter")
        self.welleb.pack()
        self.exslider = Scale(self.master,from_=0 , to = 200,orient= HORIZONTAL)
        self.exslider.pack()
        self.submit = Button(self.master,text = "SUBMIT",command = self.submitc)
        self.submit.pack()
        
    def exitmenuexer(self):
        if msg.askokcancel("Quit?", "Really quit?"):
            self.master.destroy()
            
    def aboutmenuexer(self):
        msg.showinfo("About Exercise counter","Exercise counter,"
                     +"counts the minutes of you  exercising  per day ")
    def submitc(self):
        now = datetime.datetime.today().strftime('%d-%m-%Y')
        with open('coffee.csv','a+') as d:
            thewriter = csv.writer(d)
            thewriter.writerow([now,str(self.cofslider.get())])
            d.close()
        msg.showinfo("Exercise Counter ","DATE:"+now+"\nNumber:"+str(self.exslider.get()))
    
def main():
    root=Tk()
    M= Medical(root)
    root.mainloop()
    
if __name__=='__main__':
    main()