import sys
import tkinter
from tkinter import *

win=None
win1=None

#initializes the object with values user, nice,system,iowait,steal,idle
class CPUUtil:
    def __init__(self, user, nice, system, iowait, steal, idle):
        self.user=user
        self.nice=nice
        self.system=system
        self.iowait=iowait
        self.steal=steal
        self.idle=idle
    """
    the below functions set the maximum value of the corresponding stages of the cpu utilization per hour of the time stamp
    """
    def set_user(self,user):
        if self.user<user:
            self.user=user
    def set_nice(self,nice):
        if self.nice<nice:
            self.nice=nice
    def set_system(self,system):
        if self.system<system:
            self.system=system
    def set_iowait(self,iowait):
        if self.iowait<iowait:
            self.iowait=iowait
    def set_steal(self,steal):
        if self.steal<steal:
            self.steal=steal
    def set_idle(self,idle):
        if self.idle<idle:
            self.idle=idle
            
                

# get_file function is used to obtain the file path that user inputs in the text box
def get_file(event):
    e1.get()

#binds te textbox in this function and 2 radio buttons are defined each corresponding to the area chart and bar chart    
def get_file_path():
       
    Label(win2,text="Enter the file path").grid(row=0)
    e1.bind('<Return>',get_file)
    e1.grid(row=0,column=1)    
    var = IntVar()
    R1 = Radiobutton(win2, text="Area Chart",variable=var, value=1,command=area)
    R1.grid(row=1)
    R2 = Radiobutton(win2, text="bar chart",variable=var, value=2,command=bar)
    R2.grid(row=2)
    

#the below function shows the area chart corresponding to the data points from the input file
#1st canvas
def area():
        global win
        win=Tk()
        win.title("Area Chart")
        win.geometry("600x120")
        canv=Canvas(win,bg='blue',width=480,height=100)
        canv.pack()
        user=[0,100]#green
        nice=[0,100]#voilet
        system=[0,100]#red
        iowait=[0,100]#sku blue
        steal=[0,100]#orange
        """
    Below I read the file from the path given in the text box.
    the file consists of data points of time stamp and the corresponding stage of the computer
    splitting the time stamp and taking minutes each time we populate the list of all the stages with the time stamp as the x-axis
    and corresponding values of all the stages as the y-axis value.
    then I draw the polygons of the stages using the values in the corresponding lists.
        """
        try:
            with open(e1.get()) as f:
                l=f.readlines()
                i=3
                t=0
                while i<len(l) - 1:
                    row = l[i].replace('\n','').split(' ')
                    row = [x for x in row if x != '']
                    timestamp = row[0]
                    timespan = timestamp.split(':')
                    t += 5 + float(timespan[2])/60
                    user.append(t)
                    user.append(100-float(row[3]))
                    nice.append(t)
                    nice.append(100-float(row[4])-float(row[3]))
                    system.append(t)
                    system.append(100-float(row[5])-float(row[4])-float(row[3]))
                    iowait.append(t)
                    iowait.append(100-float(row[6])-float(row[5])-float(row[4])-float(row[3]))
                    steal.append(t)
                    steal.append(100-float(row[7])-float(row[6])-float(row[5])-float(row[4])-float(row[3]))
                    i+=1
                user.append(480)
                user.append(100)
                system.append(480)
                system.append(100)
                nice.append(480)
                nice.append(100)
                iowait.append(480)
                iowait.append(100)
                steal.append(480)
                steal.append(100)
            canv.create_polygon(*steal,fill='orange')
            canv.create_polygon(*iowait,fill='sky blue')
            canv.create_polygon(*nice,fill='violet')
            canv.create_polygon(*system,fill='red')
            canv.create_polygon(*user,fill='green')
            
            # labelling the x-axis,y-axis and legends below
            label1=Label(win,text="100")
            label1.place(x=35,y=1)
            label1=Label(win,text="80")
            label1.place(x=35,y=20)
            label1=Label(win,text="60")
            label1.place(x=35,y=40)
            label1=Label(win,text="40")
            label1.place(x=35,y=60)
            label1=Label(win,text="20")
            label1.place(x=35,y=80)
            label1=Label(win,text="12")
            label1.place(x=60,y=100)
            label1=Label(win,text="1")
            label1.place(x=120,y=100)
            label1=Label(win,text="2")
            label1.place(x=180,y=100)
            label1=Label(win,text="3")
            label1.place(x=240,y=100)
            label1=Label(win,text="4")
            label1.place(x=300,y=100)
            label1=Label(win,text="5")
            label1.place(x=360,y=100)
            label1=Label(win,text="6")
            label1.place(x=420,y=100)
            label1=Label(win,text="7")
            label1.place(x=480,y=100)
            label1=Label(win,bg="blue")
            label1.place(x=550,y=10)
            label1=Label(win,text="idle")
            label1.place(x=560,y=10)
            label1=Label(win,bg="violet")
            label1.place(x=550,y=30)
            label1=Label(win,text="nice")
            label1.place(x=560,y=30)
            label1=Label(win,bg="green")
            label1.place(x=550,y=50)
            label1=Label(win,text="user")
            label1.place(x=560,y=50)
            label1=Label(win,bg="red")
            label1.place(x=550,y=70)
            label1=Label(win,text="system")
            label1.place(x=560,y=70)
            label1=Label(win,bg="sky blue")
            label1.place(x=550,y=90)
            label1=Label(win,text="iowait")
            label1.place(x=560,y=90)
            if win1!= None:
                win1.destroy()
        except TypeError:
            print('Invalid file path given')
        except FileNotFoundError:
            print("Please enter the file path first")

#the below function shows the bar chart corresponding to the data points from the input file
# second canvas
def bar():
        global win1
        win1=Tk()
        win1.title("Bar Chart")
        win1.geometry("600x140")
        canv1=Canvas(win1,bg='blue',width=480,height=120)
        canv1.pack()
        
        util={}
        t=0
        """
    below I am reading the file from the text box as above.
    the difference is instead of minutes we are taking hour value of time stamp and finding out the maximum value of all the stages for the particular
    time stamp by defining in the class "CPU Util". I declare a dictionary "util" with key as each hour and value as the object of the class consisting
    of the maximum values of all stages.Then I used create_rectangle to draw the staked bar chart of all the stages corresponding to each hour.
        """
        try:
            with open(e1.get()) as f:
                l=f.readlines()
                i=3 
                j=0.0
                p=0
                prev_hr=0
                while i<len(l) - 1:
                    row = l[i].replace('\n','').split(' ')
                    row = [x for x in row if x != '']
                    timestamp = row[0]
                    timespan = timestamp.split(':')
                    cur_hr=int(timespan[0])
                    if prev_hr==cur_hr:
                       util[prev_hr].set_user(float(row[3]))
                       util[prev_hr].set_nice(float(row[4]))
                       util[prev_hr].set_system(float(row[5]))
                       util[prev_hr].set_iowait(float(row[6]))
                       util[prev_hr].set_steal(float(row[7]))
                       util[prev_hr].set_idle(float(row[8]))
                    else:
                        prev_hr=cur_hr
                        j=0.0
                        util[prev_hr] = CPUUtil(float(row[3]),float(row[4]),float(row[5]),float(row[6]),float(row[7]),float(row[8]))
                    i+=1

            t=0        
            gap=20
            while t< prev_hr:
                if t==0 :
                    canv1.create_rectangle(gap + t*20,120-util[12].user,gap + t*20+20,120,fill='green')
                    canv1.create_rectangle(gap + t*20,120-util[12].user-util[12].nice,gap + t*20+20,120-util[12].user,fill='violet')
                    canv1.create_rectangle(gap + t*20,120-util[12].user-util[12].nice-util[12].system
                                          ,gap + t*20+20,120-util[12].user-util[12].nice,fill='red')
                    
                    canv1.create_rectangle(gap + t*20,120-util[12].user-util[12].nice-util[12].system-util[12].iowait
                                           ,gap + t*20+20,120-util[12].user-util[12].nice-util[12].system,fill='sky blue')
                     
                    canv1.create_rectangle(gap + t*20,120-util[12].user-util[12].nice-util[12].system-util[12].iowait-util[12].steal
                                           ,gap + t*20+20,120-util[12].user-util[12].nice-util[12].system-util[12].iowait,fill='orange')
                     
                    #canv1.create_rectangle(gap + t*20,120-util[12].user-util[12].nice-util[12].system-util[12].iowait-util[12].steal-util[12].idle
                                          # ,gap + t*20+20,120-util[12].user-util[12].nice-util[12].system-util[12].iowait-util[12].steal,fill='yellow')
                    
                else:
                    canv1.create_rectangle(gap + t*20,120-util[t].user,gap + t*20+20,120,fill='green')
                    canv1.create_rectangle(gap + t*20,120-util[t].nice-util[t].user,gap + t*20+20,120-util[t].user,fill='violet')
                    canv1.create_rectangle(gap + t*20,120-util[t].user-util[t].nice-util[t].system
                                          ,gap + t*20+20,120-util[t].user-util[t].nice,fill='red')
                    
                    canv1.create_rectangle(gap + t*20,120-util[t].user-util[t].nice-util[t].system-util[t].iowait
                                           ,gap + t*20+20,120-util[t].user-util[t].nice-util[t].system,fill='sky blue')
                     
                    canv1.create_rectangle(gap + t*20,120-util[t].user-util[t].nice-util[t].system-util[t].iowait-util[t].steal
                                           ,gap + t*20+20,120-util[t].user-util[t].nice-util[t].system-util[t].iowait,fill='orange')
                     
                    #canv1.create_rectangle(gap + t*20,200-util[t].user-util[t].nice-util[t].system-util[t].iowait-util[t].steal-util[t].idle
                                           #,gap + t*20+20,200-util[t].user-util[t].nice-util[t].system-util[t].iowait-util[t].steal,fill='yellow')
                    
                gap+=40
                t+=1
            #labelling the x-axis,y-axis and legends below  
            label1=Label(win1,text="100")
            label1.place(x=35,y=10)
            label1=Label(win1,text="80")
            label1.place(x=35,y=30)
            label1=Label(win1,text="60")
            label1.place(x=35,y=50)
            label1=Label(win1,text="40")
            label1.place(x=35,y=70)
            label1=Label(win1,text="20")
            label1.place(x=35,y=90)
            label1=Label(win1,text="0")
            label1.place(x=35,y=110)
            label1=Label(win1,text="12")
            label1.place(x=80,y=120)
            label1=Label(win1,text="1")
            label1.place(x=140,y=120)
            label1=Label(win1,text="2")
            label1.place(x=200,y=120)
            label1=Label(win1,text="3")
            label1.place(x=260,y=120)
            label1=Label(win1,text="4")
            label1.place(x=320,y=120)
            label1=Label(win1,text="5")
            label1.place(x=380,y=120)
            label1=Label(win1,text="6")
            label1.place(x=440,y=120)
            label1=Label(win1,text="7")
            label1.place(x=500,y=120)
            #label1=Label(win1,bg="yellow")
            #label1.place(x=550,y=10)
            #label1=Label(win1,text="idle")
            #label1.place(x=560,y=10)
            label1=Label(win1,bg="violet")
            label1.place(x=550,y=30)
            label1=Label(win1,text="nice")
            label1.place(x=560,y=30)
            label1=Label(win1,bg="green")
            label1.place(x=550,y=50)
            label1=Label(win1,text="user")
            label1.place(x=560,y=50)
            label1=Label(win1,bg="red")
            label1.place(x=550,y=70)
            label1=Label(win1,text="system")
            label1.place(x=560,y=70)
            label1=Label(win1,bg="sky blue")
            label1.place(x=550,y=90)
            label1=Label(win1,text="iowait")
            label1.place(x=560,y=90)
            if win!=None:
                win.destroy()
        except TypeError:
            print('Invalid file path given')
        except FileNotFoundError:
            print("Please enter the file path first")

#main window consisting of file menu.When you click on the file, you will get 2 options
#1st option Open: upon clicking it asks you to enter the file path in the text box and then click on the any of the 2 radio buttons
# to get the area chart and bar chart respectively
#2nd option Exit: upon clicking the main window closes
win2=Tk()
win2.title("CPU Utilization")
menubar=Menu(win2)
filemenu=Menu(menubar,tearoff=0)
filemenu.add_command(label="Open", command=get_file_path)
filemenu.add_command(label="Exit", command=win2.destroy)
menubar.add_cascade(label="File", menu=filemenu)
win2.config(menu=menubar)
e1=Entry(win2)
win2.mainloop()

   
