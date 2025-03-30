import tkinter as tk
from tkinter import messagebox
import time
import threading
import pyautogui
import pyperclip
import random

interval = 400

def setinterval():
    global interval
    try:
        value = int(intervalamount.get())
        if value <= 0:
            raise ValueError
        interval = value
        messagebox.showinfo("set", f"set to {interval}")
    except ValueError:
        messagebox.showerror("invalid", "enter positive number")

def goofy():
    messagebox.showinfo("???", "bro i dont even know mytself how this shit works just yes and etc and so on")

def spam():
    texts = textbox.get("1.0", tk.END).strip().split('\n')
    sleeptime = waittime.get()

    if not texts or all(s.strip() == '' for s in texts):
        messagebox.showerror("errror", "vro please enter some text")
        return

    def sendmsgs():
        global interval
        interval = interval
        lasttext = None
        while True:
            for text in texts:
                text = random.choice([t for t in texts if t != lasttext])
                pyperclip.copy(text)
                pyautogui.hotkey('ctrl', 'v')
                pyautogui.press('enter')
                lasttext = text
                if sleeptime:
                    interval = max(10, interval - 10)
                time.sleep(interval / 1000.0)

    threading.Thread(target=sendmsgs, daemon=True).start()

rt = tk.Tk()
rt.title("ChatRage (bully-tool)")
rt.geometry("900x530")
rt.resizable(False, False)

header = tk.Label(
    rt,
    text="Preload with sentences here (each new line = new message). Can be used for trolling too (or hateful speech).",
    anchor="w",
    justify="left",
    wraplength=900
)
header.pack(fill=tk.X, padx=10, pady=(10, 0))

textbox = tk.Text(rt, height=8, width=75)
textbox.pack(padx=10, pady=(5, 10))

main = tk.Frame(rt)
main.pack(padx=10, pady=(5, 15), fill="x")

intervalbutton = tk.Frame(main)
intervalbutton.pack(side=tk.LEFT, padx=10)

intervalamount = tk.Entry(intervalbutton, width=15, justify="left")
intervalamount.insert(0, "400")
intervalamount.pack(pady=(0, 5))

set = tk.Button(intervalbutton, text="set interval for\neach message to\nbe sent (in ms)", width=15, height=3, command=setinterval, justify="center")
set.pack()

fire = tk.Button(main, text="Fire artillery!", width=20, height=2, command=spam)
fire.pack(side=tk.LEFT, padx=110)

howtouse = tk.Button(main, text="How to use?", width=12, height=1, command=goofy)
howtouse.pack(side=tk.RIGHT, padx=10)

checkbox = tk.Frame(rt)
checkbox.pack(fill="x", padx=10, pady=(5, 10))

waittime = tk.BooleanVar()
checkboxcheck = tk.Checkbutton(
    checkbox,
    text="accelerate sending speed after each\nmessage (makes it seem more aggressive\nto the recipient)",
    variable=waittime,
    justify="left"
)
checkboxcheck.pack(side=tk.LEFT, padx=10)

rt.mainloop()
