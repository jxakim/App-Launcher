from tkinter import *
import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("zLauncher")
window.resizable(width=False, height=False)

# Background color (darkmode&lightmode)
bg_dark = "#26242f"
bg_white = "White"

# Darkmode and lightmode image locations
light = tk.PhotoImage(file="Images/lightswitch.png")
dark = tk.PhotoImage(file="Images/darkswitch.png")

# Window size
window_size = "800x600"

window.geometry(window_size)
window.config(bg=bg_dark)  # Default dark mode

# Content
label1 = Label(window, text="zLauncher", font=("Helvetica", 24, "bold"), fg=bg_white, bg=bg_dark)
label1.place(relx=0.5, rely=0.1, anchor=CENTER)

# List of app names and image locations
app_data = [
    {"name": "App 1", "image": "icons/app1.png"},
    {"name": "App 2", "image": "icons/app2.png"},
    {"name": "App 3", "image": "icons/app3.png"},
]

# Function to handle button clicks
def open_app(app_name):
    print(f"Opening {app_name}")

app_buttons = []

# Function to create buttons for each app
def create_apps():
    for i, app_info in enumerate(app_data):
        app_name = app_info["name"]
        image_path = app_info["image"]

        # Load the image and set a specific size
        app_image = PhotoImage(file=image_path).subsample(3)

        # Create a button with the image
        app_button = Button(
            window, text=app_name, image=app_image, compound="top", command=lambda name=app_name: open_app(name),
            bd=0, bg=bg_dark, activebackground=bg_dark, highlightthickness=0
        )

        app_button.grid(row=1, column=i, padx=20, pady=40)
        app_button.image = app_image
        app_buttons.append(app_button)

create_apps()

# Toggle function between light and dark mode
switch_value = False

def toggle_theme():
    global switch_value
    if switch_value:
        switch.config(image=dark, bg=bg_dark, activebackground=bg_dark)
    
        # Changes window to dark mode
        window.config(bg=bg_dark)
        switch_value = False

        # Other changes to theme
        label1.config(fg=bg_white)
        label1.config(bg=bg_dark)
    
    else:
        switch.config(image=light, bg=bg_white, activebackground=bg_white)
        
        # Changes window to light mode
        window.config(bg=bg_white)
        switch_value = True

        # Other changes to theme
        label1.config(fg=bg_dark)
        label1.config(bg=bg_white)

# Creating a button to toggle between light and dark mode
switch = tk.Button(window, image=dark, bd=0, bg=bg_dark, activebackground=bg_dark, command=toggle_theme,
                   highlightthickness=0)
switch.grid(row=0, column=0, padx=10, pady=10)

# Start the Tkinter event loop
window.mainloop()
