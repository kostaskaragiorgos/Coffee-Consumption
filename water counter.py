from tkinter import *
from tkinter import messagebox as msg
import datetime
import csv
import os
class WaterCounter():
    def __init__(self,master):
        
        self.master = master
        self.master.title("WATER COUNTER")
        self.master.geometry("200x200")
        self.master.resizable(False,False)
        if os.path.exists('water.csv') == False:
            with open('water.csv', 'a+') as f:
                thewriter = csv.writer(f)
                thewriter.writerow(['DAY','BOTTELS_OF_WATER(500ml)'])
                f.close()
        self.welleb = Label(text="Welcome to water counter")
        self.welleb.pack()
        self.watslider = Scale(self.master,from_=0 , to = 20,orient= HORIZONTAL)
        self.watslider.pack()
        self.submit = Button(text = "SUBMIT",command = self.submitc)
        self.submit.pack()
        
        
    def submitc(self):
        now = datetime.datetime.today().strftime('%d-%m-%Y')
        with open('water.csv','a+') as d:
            thewriter = csv.writer(d)
            thewriter.writerow([now,str(self.watslider.get())])
            d.close()
        msg.showinfo("Water Consumption ","DATE:"+now+"\nNumber:"+str(self.watslider.get()))
    
def main():
    root=Tk()
    WC = WaterCounter(root)
    root.mainloop()
    
if __name__=='__main__':
    main()