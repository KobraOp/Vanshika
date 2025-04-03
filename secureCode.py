import tkinter as tk
from tkinter import messagebox
import simpleaudio as sa

class Secure:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("420x50")
        self.root.title("Unlocker")

        tk.Label(self.root, 
                 text="To Unlock the code make window full screen",
                 font=(30),).pack(anchor='n')
        
        tk.Label(self.root,
                 text="A Cup Noodles will be charged 😋",
                 font=(30)).pack(anchor='s',pady=200)
        
        self.audio_call()
        
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.root.mainloop()

    def on_closing(self):
        if messagebox.askokcancel("Exit", "Dekh le Bhai ko nahi khilayegi"):
            self.root.destroy()
            Secure()

    def audio_call(self):
        wave_obj = sa.WaveObject.from_wave_file("vanshika\\assests\\audio.wav")
        play_obj = wave_obj.play()
        play_obj.wait_done()

if __name__ == "__main__":
    Secure()