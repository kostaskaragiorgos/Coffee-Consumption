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
        self.welleb = Label(text="Welcome to coffee counter")
        self.welleb.pack()
        self.cofslider = Scale(self.master,from_=0 , to = 10,orient= HORIZONTAL)
        self.cofslider.pack()
        self.submit = Button(text = "SUBMIT",command = self.submitc)
        self.submit.pack()
        
        
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