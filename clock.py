import tkinter as tk
from time import strftime

def update_time():
    current_time = strftime('%H:%M:%S')
    time_label.config(text=current_time)
    time_label.after(1000, update_time)

root = tk.Tk()
root.title("Digital Clock")
root.geometry("200x100")

time_label = tk.Label(root, font=('Helvetica', 48))
time_label.pack(pady=20)

update_time()

root.mainloop()
