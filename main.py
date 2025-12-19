import pygame as py
import tkinter as tk
from tkinter import *
import datetime as dt
from datetime import *

py.mixer.init()

def play_sound():
    py.mixer.music.play()
def stop_sound():
    py.mixer.music.stop()

def load_music(file):
    py.mixer.music.load(file)
    print("Loaded: " + str(file))

def update_time():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    date_label.config(text=current_time)
    root.after(1000, update_time)  # update every 1 second

load_music("test_audio.mp3")

#Screen Setup
root = tk.Tk()
root.title("Test Audio Player")
root.resizable(False, False)
root.geometry("300x200")


button_play = tk.Button(root,text="Play",command=play_sound)
button_play.grid(row=0,column=0)

button_stop = tk.Button(root,text="Stop",command=stop_sound)
button_stop.grid(row=0,column=1)

date_label = tk.Label(root, text="")
date_label.grid(row=1, column=0, columnspan=2, pady=10)

update_time()
root.mainloop()