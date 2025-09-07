import os
import time
import threading
import tkinter as tk
from tkinter import messagebox

QUACKS_ASCII = r"""
________                       __                 
\_____  \  __ _______    ____ |  | __ ___________ 
 /  / \  \|  |  \__  \ _/ ___\|  |/ // __ \_  __ \
/   \_/.  \  |  // __ \\  \___|    <\  ___/|  | \/
\_____\ \_/____/(____  /\___  >__|_ \\___  >__|   
       \__>          \/     \/     \/    \/       
"""

# List of fake packages for simulation
fake_packages = [
    "QuackLib", "NetworkTools", "DataCollector", 
    "AnalyticsModule", "Updater", "SecurityPatch"
]

def start_launcher_thread():
    """Run the launcher simulation in a separate thread."""
    threading.Thread(target=start_launcher).start()

def start_launcher():
    status_label.config(text="Starting installation...")
    root.update()

    for i, pkg in enumerate(fake_packages, start=1):
        status_label.config(text=f"Installing {pkg} ({i}/{len(fake_packages)})...")
        root.update()
        time.sleep(2)  # simulate installation delay

    messagebox.showerror("Error", "Ohh something went wrong!\nPlease start ATXLP process.")
    status_label.config(text="Installation failed.")

def start_atxlp():
    status_label.config(text="Launching ATXLP process...")
    root.update()
    os.system("python atxlp.py")  # assumes atxlp.py is in the same folder

root = tk.Tk()
root.title("QUACKERRR Launcher")
root.geometry("650x400")
root.resizable(False, False)

ascii_label = tk.Label(
    root,
    text=QUACKS_ASCII,
    font=("Consolas", 12, "bold"),
    fg="blue",
    justify="left"
)
ascii_label.pack(pady=10)

welcome_label = tk.Label(
    root,
    text="Welcome to QUACKERRR Launcher!\nby Emodi",
    font=("Arial", 14, "bold"),
    fg="green"
)
welcome_label.pack(pady=5)

menu_label = tk.Label(
    root,
    text="Choose an option:",
    font=("Arial", 12)
)
menu_label.pack(pady=5)

btn1 = tk.Button(root, text="Start Launcher", command=start_launcher_thread, width=25, height=2)
btn1.pack(pady=5)

btn2 = tk.Button(root, text="Start ATXLP Process", command=start_atxlp, width=25, height=2)
btn2.pack(pady=5)

status_label = tk.Label(root, text="Waiting for your choice...", font=("Arial", 10), fg="gray")
status_label.pack(pady=15)

root.mainloop()
