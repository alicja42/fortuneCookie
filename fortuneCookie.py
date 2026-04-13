import random
import time
import pygame

def loadFortunes(fileName):
    with open(fileName, "r", encoding="utf-8") as file:
        fortunes=file.readlines()
    return [fortune.strip() for fortune in fortunes]

def openCookie(fortunes):
    crumbleSound.play()
    time.sleep(crumbleSound.get_length())
    print("\nyour fortune:\n")
    print("✩₊˚.⋆☾⋆⁺₊✧✩₊˚.⋆")
    print(f'"{random.choice(fortunes)}"')
    print("✩₊˚.⋆☾⋆⁺₊✧✩₊˚.⋆")
    
    
fortunes=loadFortunes("fortunes.txt")

pygame.mixer.init()
pygame.mixer.music.load("fortune-cookie-opened.mp3")
pygame.mixer.music.set_volume(0.4)
pygame.mixer.music.play(-1)

crumbleSound=pygame.mixer.Sound("crumple.mp3")
crumbleSound.set_volume(0.7)

while True:
    print("\n🥠fortune cookie app🥠")
    print("1. open your fortune cookie")
    print("2. exit")
    
    choice=input("choose (1-2): ")
    
    if choice=="1":
        openCookie(fortunes)
    elif choice=="2":
        pygame.mixer.music.stop()
        break
    else:
        print("invalid try again\n")
