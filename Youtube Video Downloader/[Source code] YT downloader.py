#pip install pytube
#pip install Tkinter

from tkinter import Label,Button,Tk,StringVar,Entry
from os import getcwd
from pytube import YouTube
def down():
    url=YouTube(str(entrytext.get()))
    video=url.streams.first()
    video.download()
    l4=Label(text="Downloaded Successfully!!!",bg="#161A27",fg="maroon1",font=20)
    l4.place(x=210,y=310)
    tt="File saved in "+ getcwd()
    l6=Label(text=tt,bg="#161A27",fg="white")
    l6.place(x=10,y=370)
root=Tk()
root.title("SMS : Youtube video downloader")
root.geometry("600x400")
root.resizable(0,0)
l1=Label(bg="#161A27",width=400,height=600)
l1.place(x=0,y=0)
l2=Label(text="YOUTUBE VIDEO DOWNLOADER",fg="#42FF62",bg="#161A27",font=("NORMAL bold",22),padx=10,pady=10)
l2.place(x=70,y=50)
l3=Label(text="Paste Link Here :",fg="white",bg="#161A27",font=25)
l3.place(x=250,y=130)
entrytext=StringVar()
e1=Entry(width=45,textvariable=entrytext,border=2,relief="groove",bg="black",font="bold",fg="#29FFF4")
e1.place(x=100,y=170,height=50)
b1=Button(text="Download",command=down,bg="black",borderwidth=3,relief="ridge",font=15,fg="white")
b1.place(x=260,y=240,height=40,width=100)
root.mainloop()
