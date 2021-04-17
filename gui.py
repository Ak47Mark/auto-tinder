import tkinter as tk
import functools
from PIL import Image, ImageTk

people = []

def loadData():
    f = open("log.txt", "r")
    ps = f.read().splitlines()
    for person in ps:
        person = person.split(', ')
        people.append(person)
        listbox.insert(tk.END, person[0] + ' ' + person[2])

def getPerson(event):
    list_tuple = listbox.curselection()
    id = functools.reduce(lambda sub, elem: sub * 10 + elem, list_tuple)

    profile = Image.open("Tinder photos/"+people[id][1]+"_1.jpg")
    profile = profile.resize((480, 600), Image.ANTIALIAS)
    profile = ImageTk.PhotoImage(profile)
    profile_label = tk.Label(image = profile)
    profile_label.image = profile
    profile_label.grid(column = 0, row = 0)


root = tk.Tk()
root.title("Auto Tinder")
root.geometry("800x600")
root.iconbitmap('icon.ico')

canvas = tk.Canvas(root, width=800, height=600)
canvas.grid(columnspan=6, rowspan=4)

listbox = tk.Listbox(root)
listbox.grid(column = 1, row = 0)
listbox.bind('<Double-1>', getPerson)

profile = Image.open("Tinder photos/5dc6a870c28cd9010001da7d_4.jpg")
profile = profile.resize((480, 600), Image.ANTIALIAS)
profile = ImageTk.PhotoImage(profile)
profile_label = tk.Label(image = profile)
profile_label.image = profile
profile_label.grid(column = 0, row = 0)

face = Image.open("Tinder photos/5dc6a870c28cd9010001da7d_4_0.jpg")
face = ImageTk.PhotoImage(face)
face_label = tk.Label(image = face)
face_label.image = face
#face_label.grid(column = 1, row = 0)

data = tk.Label(root, text="Name: Asdasd\nName: Asdasd")
#data.grid(column = 1, row = 0)

loadData()

root.mainloop()