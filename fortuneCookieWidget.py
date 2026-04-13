import random
import pygame
import tkinter as tk
from PIL import Image, ImageTk

def loadFortunes(fileName):
    with open(fileName, "r", encoding="utf-8") as file:
        fortunes=file.readlines()
    return [fortune.strip() for fortune in fortunes]

def openCookie():
    crumbleSound.play()
    cookieLabel.config(image=openImage)
    fortune=random.choice(fortunes)
    fortuneLabel.config(text=fortune)

fortunes=loadFortunes("fortunes.txt")

pygame.mixer.init()
pygame.mixer.music.load("fortune-cookie-opened.mp3")
pygame.mixer.music.set_volume(0.4)
pygame.mixer.music.play(-1)

crumbleSound=pygame.mixer.Sound("crumple.mp3")
crumbleSound.set_volume(0.7)

root=tk.Tk()
root.title("Fortune Cookie")
root.geometry("400x300")
root.configure(bg="#f5e6c8")

def loadAndResize(path, width):
    image=Image.open(path)
    ratio=width/image.width
    newHeight=int(image.height*ratio)
    image=image.resize((width, newHeight))
    return ImageTk.PhotoImage(image)

closedImage=loadAndResize("cookieClosed.png", 200)
openImage=loadAndResize("cookieOpened.png", 200)

centerFrame=tk.Frame(root, bg="#f5e6c8")
centerFrame.pack(expand=True)

cookieLabel=tk.Label(centerFrame, image=closedImage, bg="#f5e6c8")
cookieLabel.pack(pady=10)
cookieLabel.bind("<Button-1>", lambda e: openCookie())

fortuneLabel=tk.Label(centerFrame, text="", wraplength=300, font=("Helvetica", 12), bg="#f5e6c8", fg="black")
fortuneLabel.pack()

root.mainloop()
