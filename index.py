from tkinter import *
import tkinter as tk
from geopy.geocoders import Nominatim, Photon
from tkinter import ttk,messagebox
from timezonefinder import TimezoneFinder
from datetime import datetime
import requests
import pytz


def getdata():
    city =textf.get()

    geolocator = Photon(user_agent ="geoapiExercises")
    location =geolocator.geocode(city)
    ob =TimezoneFinder()
    result = ob.timezone_at(lng=location.longitude,lat=location.latitude)

    home = pytz.timezone(result)
    localtime = datetime.now(home)
    currenttime =localtime.strftime("%I:%M %p")
    clock.config(text=currenttime)
    mytime.config(text="CURRENT WEATHER")

    api= "https://api.openweathermap.org/data/2.5/weather?q"+city+"&appid=87cb6297185815c884dd5e26e5a531a0"
    
    json_data = requests.get(api).json()
    condition =json_data["weather"][0]['main']
    description = json_data['weather'][0]['description']
    temp =int(json_data['main']['temp']-273.15)
    pressure = json_data['main']['pressure']
    humidity = json_data['main']['humidity']
    wind = json_data['wind']['speed']

    t.config(text=(temp,"°"))
    c.config(text=(condition,"|","FEELS","LIKE",temp,"°"))
    w.config(text=wind)
    h.config(text=humidity)
    d.config(text=description)
    p.config(text=pressure)




root =Tk()
root.title("Weather App")
root.geometry("900x500+300+200")
root.resizable(False,False)

# code for search box 
search_img = PhotoImage(file="search.png")
myimg = Label (image=search_img)
myimg.place(x=20,y= 20)

textf= tk.Entry(root,justify="center",width=17,font=("poppons",25,"bold"),bg="#404040",border=0,fg="white")
textf.place(x=50,y=40)
textf.focus()

searchicon = PhotoImage(file="search_icon.png")
mysearch = Button(image=searchicon,borderwidth=0,cursor="hand2",bg="#404040",command=getdata)
mysearch.place(x=400,y=34)

# code for logo 

mylogo = PhotoImage(file="logo.png")
logo = Label(image=mylogo)
logo.place(x=150,y=100)

# code for button box

mainbar = PhotoImage(file="box.png")
maybar = Label(image=mainbar)
maybar.pack(padx=5,pady=5,side=BOTTOM)

# code for display time 

mytime = Label(root,font=("arail",15,"bold"))
mytime.place(x=30,y=100)
clock = Label(root,font=("Helvetica",20))
clock.place(x=30,y=130)



# make label on bar 

l1 = Label(root,text="WIND",font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ef")
l1.place(x=120,y=400)

l2 = Label(root,text="HUMIDITY",font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ef")
l2.place(x=250,y=400)

l3 = Label(root,text="DESCRIPTION",font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ef")
l3.place(x=430,y=400)

l4 = Label(root,text="PRESSURE",font=("Helvetica",15,'bold'),fg="white",bg="#1ab5ef")
l4.place(x=650,y=400)

t = Label(font=("arial",70,"bold"),bg="#ee666d")
t.place(x=400,y=150)
c= Label(font=("arial",15,"bold"))
c.place(x=400,y=250)

w= Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
w.place(x=120,y=430)

h= Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
h.place(x=280,y=430)

d= Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
d.place(x=450,y=430)

p= Label(text="...",font=("arial",20,"bold"),bg="#1ab5ef")
p.place(x=670,y=430)







root.mainloop()