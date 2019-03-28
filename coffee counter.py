from tkinter import *
from tkinter import messagebox as msg
import datetime
import csv
import os
class CoffeeCounter():
    def __init__(self,master):
        
        self.master = master
        self.master.title("COFFEE COUNTER")
        self.master.geometry("200x200")
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
        
        self.welleb = Label(text="Welcome to coffee counter")
        self.welleb.pack()
        self.cofslider = Scale(self.master,from_=0 , to = 10,orient= HORIZONTAL)
        self.cofslider.pack()
        self.submit = Button(text = "SUBMIT",command = self.submitc)
        self.submit.pack()
        
    def exitmenu(self):
        pass
    def aboutmenu(self):
        pass
    
    def submitc(self):
        now = datetime.datetime.today().strftime('%d-%m-%Y')
        with open('coffee.csv','a+') as d:
            thewriter = csv.writer(d)
            thewriter.writerow([now,str(self.cofslider.get())])
            d.close()
        msg.showinfo("Coffee Consumption ","DATE:"+now+"\nNumber:"+str(self.cofslider.get()))
    
def main():
    root=Tk()
    CC = CoffeeCounter(root)
    root.mainloop()
    
if __name__=='__main__':
    main()