import requests
import tkinter as tk
from tkinter import *

ct="Hyderabad"
a=Tk()
a.title("Weather App")
a.geometry("1000x700")
my_label = Label(a)
my_label.pack()


entry =Entry(a,justify="center",width=15,font=("poppins",35,"bold"),bg="Green",border=0,fg="white")
entry.place(x=300,y=40)
entry.focus()

l1=Label(text='TEMPERATURE',font=("Helvetica",21,'bold'),fg="black").place(x=180,y=200)
l2=Label(text='HUMIDITY',font=("Helvetica",21,'bold'),fg="black").place(x=180,y=280)
l3=Label(text='WIND SPEED',font=("Helvetica",21,'bold'),fg="black").place(x=180,y=360)
l4=Label(text='CONDITION',font=("Helvetica",21,'bold'),fg="black").place(x=180,y=440)
t=Label(font=("Helvetica",20,'bold'),fg='black',bg='#1ab5ef',width='20')
t.place(x=500,y=200)
h=Label(font=("Helvetica",20,'bold'),fg='black',bg='#1ab5ef',width='20')
h.place(x=500,y=280)
w=Label(font=("Helvetica",20,'bold'),fg='black',bg='#1ab5ef',width='20')
w.place(x=500,y=360)
c=Label(font=("Helvetica",20,'bold'),fg='black',bg='#1ab5ef',width='20')
c.place(x=500,y=440)
l5=Label(text='PRESSURE',font=("Helvetica",21,'bold'),fg="black").place(x=180,y=520)
p=Label(font=("Helvetica",20,'bold'),fg='black',bg='#1ab5ef',width='20')
p.place(x=500,y=520)


def getWeather():
  ct=entry.get()
  api="https://api.openweathermap.org/data/2.5/weather?q="+ct+"&appid=f52705bfab8ec01d4cc00e6d99e096de"
  json_data=requests.get(api).json()
  condition=json_data['weather'][0]['main']
  description=json_data['weather'][0]['description']
  temp=int(json_data['main']['temp']-273.15)
  pressure=json_data['main']['pressure']
  humidity=json_data['main']['humidity']
  wind= json_data['wind']['speed']

  t.config(text=(temp,"°"))
  w.config(text=wind)
  h.config(text=humidity)
  c.config(text=condition)
  p.config(text=pressure)



s=PhotoImage(file="thun.png")
i=Label(image=s)
i.place(x=50,y=20)
st=PhotoImage(file="sun.png")
it=Label(image=st)
it.place(x=800,y=20)


icon=PhotoImage(file="s_icon.png")
ic=Button(image=icon,borderwidth=0,cursor="hand2",bg="#FF4040",command=getWeather)
ic.place(x=635,y=41)

a.mainloop()
