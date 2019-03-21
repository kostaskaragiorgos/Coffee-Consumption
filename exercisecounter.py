from tkinter import *
from tkinter import messagebox as msg
import datetime
import csv
import os
class ExerciseCounter():
    def __init__(self,master):
        
        self.master = master
        self.master.title("EXERCISE COUNTER")
        self.master.geometry("200x200")
        self.master.resizable(False,False)
        if os.path.exists('exercise.csv') == False:
            with open('exercise.csv', 'a+') as f:
                thewriter = csv.writer(f)
                thewriter.writerow(['DAY','MINUTES_OF_EXERCISE'])
                f.close()
        self.welleb = Label(text="Welcome to exercise counter")
        self.welleb.pack()
        self.exslider = Scale(self.master,from_=0 , to = 200,orient= HORIZONTAL)
        self.exslider.pack()
        self.submit = Button(text = "SUBMIT",command = self.submitc)
        self.submit.pack()
        
        
    def submitc(self):
        now = datetime.datetime.today().strftime('%d-%m-%Y')
        with open('coffee.csv','a+') as d:
            thewriter = csv.writer(d)
            thewriter.writerow([now,str(self.cofslider.get())])
            d.close()
        msg.showinfo("Exercise Counter ","DATE:"+now+"\nNumber:"+str(self.exslider.get()))
    
def main():
    root=Tk()
    EC = ExerciseCounter(root)
    root.mainloop()
    
if __name__=='__main__':
    main()