import tkinter as tk
from tkinter import ttk
import pyaudio
import speak as sp
import secureCode

class AudioSelectorGUI:
    def __init__(self):
        secureCode.Secure()

        root = tk.Tk()
        self.root = root
        self.root.title("Select Audio Input Source")
        self.root.geometry("400x200")
        self.mic_list = self.get_mic_list()
        
        ttk.Label(root, text="Select Microphone:").pack(pady=10)
        self.mic_var = tk.StringVar(value=self.mic_list[0] if self.mic_list else "No Mic Found")
        self.mic_dropdown = ttk.Combobox(root, textvariable=self.mic_var, values=self.mic_list)
        self.mic_dropdown.pack(pady=10)

        self.save_button = ttk.Button(root, text="Set Input Source", command=self.set_input_source)
        self.save_button.pack(pady=10)

        root.mainloop()

    def get_mic_list(self):
        mic_list = []
        for i in range(pyaudio.PyAudio().get_device_count()):
            device_info = pyaudio.PyAudio().get_device_info_by_index(i)
            if device_info['maxInputChannels'] > 0:
                mic_list.append(f"{device_info['index']}: {device_info['name']}")
        return mic_list if mic_list else ["No Mics Found"]

    def set_input_source(self):
        mic_index = int(self.mic_var.get().split(":")[0])
        global assistant
        sp.Model(mic_index=mic_index)
        print(f"Microphone set to: {self.mic_var.get()}")
        self.root.destroy()