from pytube import YouTube
from tkinter import *
from PIL import ImageTk, Image
import wget
import tkinter as tk
import userpaths
import os




root = tk.Tk()


yt = YouTube("https://youtu.be/1J0DlUz1nbk?si=GzvkyDUUbaVr93qv")
url = yt.thumbnail_url

file_name = wget.download(url)

img = ImageTk.PhotoImage(Image.open(file_name))
imgresize = Image.open(file_name)
img=imgresize.resize((round(imgresize.width / 3), round(imgresize.height / 3)))
miniaturaimg=ImageTk.PhotoImage(img)
miniatura = tk.Label(root, image=miniaturaimg)
miniatura.place(relx=0.5, rely=0.34, anchor=CENTER)

os.remove(file_name)

documentosog = userpaths.get_my_documents()
documentos = documentosog.replace("\\", "/")
destination = str(documentos + "/TackTube/Descargas")

def clicked():
    inputValue = txt.get()
    yt = YouTube(inputValue)
    titulo.configure(text = yt.title)
    url = yt.thumbnail_url
    file_name = wget.download(url)
    img = ImageTk.PhotoImage(Image.open(file_name))
    imgresize = Image.open(file_name)
    img=imgresize.resize((round(imgresize.width / 3), round(imgresize.height / 3)))
    miniaturaimg=ImageTk.PhotoImage(img)
    miniatura.configure(image=miniaturaimg)
    miniatura.image = miniaturaimg
    os.remove(file_name)

def descargaraudio():
    inputValue = txt.get()
    yt = YouTube(inputValue)
    video = yt.streams.filter(only_audio=True).first() 
    out_file = video.download(output_path=destination)
    base, ext = os.path.splitext(out_file) 
    new_file = base + '.mp3'
    os.rename(out_file, new_file) 



def descargarvideo():
    inputValue = txt.get()
    yt = YouTube(inputValue)
    video = yt.streams.get_highest_resolution() 
    out_file = video.download(output_path=destination)
    base, ext = os.path.splitext(out_file) 
    new_file = base + '.mp4'
    os.rename(out_file, new_file) 


root.title("TackTube")
root.geometry('480x720')
lbl = Label(root, text = "Introduce el link del video")
lbl.place(relx=0.5, rely=0.01, anchor=CENTER)
txt = Entry(root, width=50)
txt.place(relx=0.5, rely=0.04, anchor=CENTER)

btn = Button(root, text = "Obtener Video" ,
             command=clicked)
btn.place(relx=0.5, rely=0.08, anchor=CENTER)

btn2 = Button(root, text = "Descargar Audio" ,
             command=descargaraudio)
btn2.place(relx=0.5, rely=0.56, anchor=CENTER)

btn3 = Button(root, text = "Descargar Video" ,
             command=descargarvideo)
btn3.place(relx=0.5, rely=0.62, anchor=CENTER)

video = Label(root, text = "Video a descargar:")
video.place(relx=0.5, rely=0.12, anchor=CENTER)
titulo = Label(root, text = yt.title)
titulo.place(relx=0.5, rely=0.16, anchor=CENTER)

root.mainloop()