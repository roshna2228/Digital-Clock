# Digital-Clock  


# This Python script uses the Tkinter library to create a simple digital clock that displays the current time and updates every second.

## Imports
import tkinter as tk
from time import strftime

- 'tkinter': This is Python's standard GUI (Graphical User Interface) library, which is used to create the application window and its components.
- 'strftime' from the 'time' module: This function is used to format the current time as a string.

## Function to Update Time
def update_time():
    current_time = strftime('%H:%M:%S')
    time_label.config(text=current_time)
    time_label.after(1000, update_time)

    - current_time = strftime('%H:%M:%S'): This line gets the current time and formats it as a string in the format HH:MM:SS.
    - time_label.config(text=current_time): This line updates the text of the time_label widget to display the current time.
    - time_label.after(1000, update_time): This line sets a timer to call the update_time function again after 1000 milliseconds (1 second). This creates a loop 
      that continuously updates the time every second
      
## Main Application
root = tk.Tk()
root.title("Digital Clock")
root.geometry("200x100")

- root = tk.Tk(): This creates the main application window.
- root.title("Digital Clock"): This sets the title of the window to "Digital Clock".
- root.geometry("200x100"): This sets the size of the window to 200 pixels wide and 100 pixels high.
  
## Time Label
time_label = tk.Label(root, font=('Helvetica', 48))
time_label.pack(pady=20)

- time_label = tk.Label(root, font=('Helvetica', 48)): This creates a label widget to display the time. It sets the font to 'Helvetica' with a size of 48.
- time_label.pack(pady=20): This adds the label to the window and centers it with a padding of 20 pixels on the vertical axis.

## Start the Clock
update_time()

- This calls the update_time function to start the clock. This initial call sets the clock in motion, updating every second.

## Main Loop
root.mainloop()

- root.mainloop(): This starts the Tkinter event loop, which waits for user interactions and updates the GUI as needed. The program will run indefinitely until the window is closed by the user.
