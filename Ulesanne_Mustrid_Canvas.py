from tkinter import * 
from turtle import width
import random 
from math import *

root= Tk () 
root.geometry("400x400") 
root.iconbitmap('canvas.ico') 
root.title("Canvas kasutamine") 

def ruut():
    ruut_window = Tk()
    ruut_window.title("Ruut")
    tahvel_2 = Canvas(ruut_window, width=700, height=600)
    tahvel_2.create_text(30, 500, text="Ruut", anchor=NW) 
    x0=80
    y0=80
    x1=400
    y1=400
    a=200
    r=(a**2+a**2)**(1/2) 
    p=(a-r) 
    for i in range(35):
        x0+=p 
        y0+=p 
        x1-=p 
        y1-=p
        tahvel_2.create_rectangle(x0,y0,x1,y1, fill="Blue")
        tahvel_2.create_oval(x0,y0,x1,y1, fill="Red")
        p=r-a
        r=r-p
        a=((r)*sqrt(2))/2
    tahvel_2.grid()
    
def ringi():
    ring_window = Tk()
    ring_window.title("Ring")
    tahvel_1 = Canvas(ring_window, width=500, height=400)
    tahvel_1.create_text(30, 550, text="Ring", anchor=NW) 
    colors=["red","blue","yellow"]
    x0=0
    y0=0
    x1=400
    y1=400
    p=2
    for i in range(150):
        x0+=p 
        y0+=p 
        x1-=p 
        y1-=p 
        tahvel_1.create_oval(x0,y0,x1,y1, fill=random.choice(colors))
    tahvel_1.grid()

def malelaud():
    malelaud_window = Tk()
    malelaud_window.title("Malelaud")
    tahvel_3 = Canvas(malelaud_window, width=700, height=600) 
    tahvel_3.create_text(30, 550, text="Malelaud", anchor=NW) 
    a=45
    b=a*15
    for i in range(12):
        for j in range(12):
            x1=i * a
            y1=j *  a
            if (i + j) % 2 == 0:
                color = "white"
            else:
                color = "black" 
                tahvel_3.create_rectangle(x1, y1, x1+a, y1+a, fill=color)
    tahvel_3.grid()

def Eesti():
    eesti_window = Tk()
    eesti_window.title("Eesti lipp")
    tahvel_4 = Canvas(eesti_window, width=400, height=400)
    tahvel_4.create_text(65, 300, text="Eesti lipp", anchor=NW) 
    x1=15
    y1=85
    y2=145
    y3=255
    a=250
    b=200
    tahvel_4.create_rectangle(x1,y1,a, b, fill="Blue")
    tahvel_4.create_rectangle(x1,y2,a, b, fill="Black")
    tahvel_4.create_rectangle(x1,y3,a, b,  fill="White")
    tahvel_4.grid()

def Saksa():
    saksa_window = Tk()
    saksa_window.title("Saksa lipp")
    tahvel_5 = Canvas(saksa_window, width=400, height=400)
    tahvel_5.create_text(65, 300, text="Saksa lipp", anchor=NW) 
    x1=25
    y1=105
    y2=150
    y3=250
    a=300
    b=200
    tahvel_5.create_rectangle(x1,y1,a, b, fill="Black")
    tahvel_5.create_rectangle(x1,y2,a, b, fill="Red")
    tahvel_5.create_rectangle(x1,y3,a, b,  fill="Gold")
    tahvel_5.grid()

def Bahama():
    bahama_window = Tk()
    bahama_window.title("Bahama saarte lipp")
    tahvel_6 = Canvas(bahama_window, width=400, height=400)
    tahvel_6.create_text(30, 300, text="Bahama saarte lipp", anchor=NW) 
    x1=35
    a=300
    b=200
    y1=45
    y2=95
    y3=155
    tahvel_6.create_rectangle(x1, y1, a, b, fill="Teal")
    tahvel_6.create_rectangle(x1, y2, a, b, fill="Yellow")
    tahvel_6.create_rectangle(x1, y3, a, b, fill="Teal")
    tahvel_6.create_polygon([x1,y1],[x1,b],[115,125],fill="black")
    tahvel_6.grid()
 
current_color = "Red"

def lulitage_valgust():
    global current_color
    if current_color == "Red":
        current_color = "Yellow"
        tahvel_7.itemconfig(Punane_värv, fill="White") # .itemconfig - с этой командой можно динамично менять цвет, длинну или ширину - https://www.tutorialspoint.com/how-to-reconfigure-tkinter-canvas-items#:~:text=If%20you%20need%20to%20configure,width%20using%20itemconfig()%20method.
        tahvel_7.itemconfig(Kollane_värv, fill="Yellow")
    elif current_color == "Yellow":
        current_color = "Green"
        tahvel_7.itemconfig(Kollane_värv, fill="White")
        tahvel_7.itemconfig(Roheline_värv, fill="Green")
    else:
        current_color = "Red"
        tahvel_7.itemconfig(Roheline_värv, fill="White")
        tahvel_7.itemconfig(Punane_värv, fill="Red")
    valgusfoor_window.after(2000, lulitage_valgust) # .after - так же как и в arduino после промежутка времени меняет цвет - https://www.educba.com/tkinter-after/

def valgusfoor():
    global tahvel_7
    global Punane_värv
    global Kollane_värv
    global Roheline_värv
    global valgusfoor_window
    
    valgusfoor_window = Tk()
    valgusfoor_window.title("Valgusfoor")
    tahvel_7 = Canvas(valgusfoor_window, width=300, height=350)
    tahvel_7.create_text(25, 20, text="Valgusfoor", anchor=NW)
    a = 150
    b = 160
    x1 = 30
    y1 = 60
    y2 = 105
    y3 = 225
    Punane_värv = tahvel_7.create_rectangle(x1, y1, a, b, width=3, outline="Black", fill="Red")
    Kollane_värv = tahvel_7.create_rectangle(x1, y2, a, b, width=3, outline="Black", fill="white")
    Roheline_värv = tahvel_7.create_rectangle(x1, y3, a, b, width=3, outline="Black", fill="white")
    tahvel_7.create_rectangle(100, 225, 85, 500, fill="Black")
    tahvel_7.create_rectangle(35, 275, 150, 25, fill="Black")
    tahvel_7.grid()
    
var=IntVar()
def valik():
    figure = var.get()
    if figure == 1:
        ringi()
    elif figure==2:
        ruut()
    elif figure==3:
        malelaud()
    elif figure ==4:
        Eesti()
    elif figure == 5:
        Saksa()
    elif figure==6:
        Bahama()
    elif figure==7:
        valgusfoor()
        lulitage_valgust()

rb1 = Radiobutton(root, text="Ring", variable=var, value=1, command=valik,font=("Arial", 20))
rb2 = Radiobutton(root,  text="Ruut",variable=var, value=2, command=valik,font=("Arial", 20))
rb3 = Radiobutton(root, text="Malelaud", variable=var, value=3, command=valik,font=("Arial", 20))
rb4 = Radiobutton(root, text="Eesti lipp",variable=var, value=4, command=valik,font=("Arial", 20))
rb5 = Radiobutton(root, text="Saksa lipp", variable=var, value=5, command=valik,font=("Arial", 20))
rb6 = Radiobutton(root, text="Bahama saarte lipp",variable=var, value=6, command=valik,font=("Arial", 20))
rb7 = Radiobutton(root, text="Valgusfoor",variable=var,  value=7, command=valik,font=("Arial", 20))

rb1.grid(row=1, column=0)
rb2.grid(row=2, column=0)
rb3.grid(row=3, column=0)
rb4.grid(row=4, column=0)
rb5.grid(row=5, column=0)
rb6.grid(row=6, column=0)
rb7.grid(row=7, column=0)

root.mainloop()