from tkinter import *
from PIL import ImageTk,Image
import requests
import json
import urllib.request
root = Tk()
root.title("Country API - Made By Ritvik Buxi")
root.geometry("500x500")
root.config(bg="#8370fe")
logo = ImageTk.PhotoImage(Image.open("india.jpg"))
root.iconphoto(False,logo)
LH = Label(root,text="Capital City Name",font=("Arial",30,"bold"),bg="#8370fe",fg="white")
LH.place(relx=0.4,rely=0.15,anchor=CENTER)
CEntry = Entry(root,relief=FLAT,width=40)
CEntry.place(relx=0.3,rely=0.25,anchor=CENTER)
lblcounty = Label(root,text="Country: ",bg="#8370fe",fg="white",font=("Arial",15,"bold"))
lblregion = Label(root,text="Region: ",bg="#8370fe",fg="white",font=("Arial",15,"bold"))
lbllang = Label(root,text="Language: ",bg="#8370fe",fg="white",font=("Arial",15,"bold"))
lblpop = Label(root,text="Population: ",bg="#8370fe",fg="white",font=("Arial",15,"bold"))
lblcare = Label(root,text="Area: ",bg="#8370fe",fg="white",font=("Arial",15,"bold"))
lblimg = Label(root,borderwidth=0,bg="#8370fe")
lblcounty.place(relx=0.05,rely=0.4,anchor=W)
lblregion.place(relx=0.05,rely=0.475,anchor=W)
lbllang.place(relx=0.05,rely=0.55,anchor=W)
lblpop.place(relx=0.05,rely=0.625,anchor=W)
lblcare.place(relx=0.05,rely=0.7,anchor=W)
lblimg.place(relx=0.05,rely=0.85,anchor=W)
def cityDetails():
    apiRequest = requests.get("https://restcountries.com/v2/capital/" + CEntry.get())
    apiOutputJson = json.loads(apiRequest.content)
    name = apiOutputJson[0]['name']
    region =  apiOutputJson[0]['region']
    language = apiOutputJson[0]['languages'][0]['name']
    population = apiOutputJson[0]['population']
    area = apiOutputJson[0]['area']
    png = apiOutputJson[0]['flags']['png']
    lblcounty['text'] = "Country: "+name
    lblregion['text'] = "Region: "+region
    lbllang['text'] = "Language: "+str(language)
    lblpop['text'] = "Population: " + str(population)
    lblcare['text'] = "Area: "+str(area)
    try:
        urllib.request.urlretrieve(png,'png.png')
    except urllib.error.HTTPError:
        print("Forbiden 403 :(")
    try:
        flagimg = (Image.open('png.png'))
    except FileNotFoundError:
        print("File Not Found! :(")
    rflagimg = flagimg.resize((160,106),Image.ANTIALIAS)
    fl = ImageTk.PhotoImage(rflagimg)
    lblimg['image']=fl
btn = Button(root,text="City Details",bg="blue",fg="white",relief="flat",padx=10,pady=1,command=cityDetails)
btn.place(relx=0.055,rely=0.3)
root.mainloop()
