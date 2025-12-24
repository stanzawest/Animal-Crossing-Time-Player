import pygame as py
import tkinter as tk
from tkinter import *
import datetime as dt
from datetime import *

py.mixer.init()

music_is_paused = False

music_ac = [
  "music/ac/12AM.mp3",
  "music/ac/1AM.mp3",
  "music/ac/2AM.mp3",
  "music/ac/3AM.mp3",
  "music/ac/4AM.mp3",
  "music/ac/5AM.mp3",
  "music/ac/6AM.mp3",
  "music/ac/7AM.mp3",
  "music/ac/8AM.mp3",
  "music/ac/9AM.mp3",
  "music/ac/10AM.mp3",
  "music/ac/11AM.mp3",
  "music/ac/12PM.mp3",
  "music/ac/1PM.mp3",
  "music/ac/2PM.mp3",
  "music/ac/3PM.mp3",
  "music/ac/4PM.mp3",
  "music/ac/5PM.mp3",
  "music/ac/6PM.mp3",
  "music/ac/7PM.mp3",
  "music/ac/8PM.mp3",
  "music/ac/9PM.mp3",
  "music/ac/10PM.mp3",
  "music/ac/11PM.mp3"
]

music_nl = [
  "music/nl/12 AM.mp3",
  "music/nl/1 AM.mp3",
  "music/nl/2 AM.mp3",
  "music/nl/3 AM.mp3",
  "music/nl/4 AM.mp3",
  "music/nl/5 AM.mp3",
  "music/nl/6 AM.mp3",
  "music/nl/7 AM.mp3",
  "music/nl/8 AM.mp3",
  "music/nl/9 AM.mp3",
  "music/nl/10 AM.mp3",
  "music/nl/11 AM.mp3",
  "music/nl/12 PM.mp3",
  "music/nl/1 PM.mp3",
  "music/nl/2 PM.mp3",
  "music/nl/3 PM.mp3",
  "music/nl/4 PM.mp3",
  "music/nl/5 PM.mp3",
  "music/nl/6 PM.mp3",
  "music/nl/7 PM.mp3",
  "music/nl/8 PM.mp3",
  "music/nl/9 PM.mp3",
  "music/nl/10 PM.mp3",
  "music/nl/11 PM.mp3"
]


def play_sound():
    global music_is_paused
    py.mixer.music.unpause()
    music_is_paused = False

def stop_sound():
    global music_is_paused
    py.mixer.music.pause()
    music_is_paused = True

def reset_music():
    py.mixer.music.stop()

def load_music(file):
    py.mixer.music.load(file)
    print("Loaded: " + str(file))

def update_volume():
    py.mixer.music.set_volume(slider.get()/100)
    root.after(1,update_volume)

def update_current_track():
    nowtime = datetime.now()

    if not py.mixer.music.get_busy() and music_is_paused == False:
        print("Music is not playing or the track has ended, loading track for current hour")
        if game_selected.get() == 0:
            load_music(music_ac[nowtime.hour])
        elif game_selected.get() == 1:
            load_music(music_nl[nowtime.hour])
        py.mixer.music.play()

    root.after(1000,update_current_track)

root = tk.Tk()
root.iconbitmap("images/icon.ico")
root.title("AC Music Player")
root.resizable(False, False)
root.geometry("300x150")

game_selected = tk.IntVar()
game_selected.set(0)

Radiobutton(root, text='Play \"Animal Crossing\" Sound Track', variable=game_selected, value=0).grid(row=0,column=0,sticky='w')
Radiobutton(root, text='Play \"Animal Crossing New Leaf\" Sound Track', variable=game_selected, value=1).grid(row=1,column=0,sticky='w')

button_frame = tk.Frame(root)
button_frame.grid(row=2, column=0, pady=5)

button_play = tk.Button(button_frame, text="Unpause", command=play_sound)
button_stop = tk.Button(button_frame, text="Pause", command=stop_sound)
button_reset = tk.Button(button_frame, text="Reset", command=reset_music)

button_play.pack(side='left', padx=(0,5))
button_stop.pack(side='left')
button_reset.pack(side='left')

slider = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL, length=275)
slider.grid(row=3, column=0, columnspan=2, pady=10, padx=10, sticky='w')
slider.set(50)

update_current_track()
update_volume()
root.mainloop()
