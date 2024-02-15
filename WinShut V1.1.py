import os
import webbrowser
from tkinter import *
from tkinter import ttk, messagebox

Shutdown_set = False


def shutdown_minutes():
    global Shutdown_set
    if Shutdown_set:
        messagebox.showwarning("Error", "Shutdown command is already set. You can give another command after restarting the system")
        return
    shutdown_command = Shutdown_text.get()
    if not shutdown_command:
        messagebox.showwarning("Error", "Please enter a value.")
        return
    try:
        shutdown_command = int(Shutdown_text.get())
    except ValueError:
        messagebox.showwarning("Error", "Only Integers are allowed")

    if shutdown_command < 1:
        exit()
    else:
        Shutdown_set = True
        shutdown_command *= 60
        os.system(f"shutdown /s /t {shutdown_command}")
        grab()


# --------------------------------------------------------------------------------------------------


def shutdown_seconds():
    global Shutdown_set
    if Shutdown_set:
        messagebox.showwarning("Error",
                               "Shutdown command is already set. You can give another command after restarting the system")
        return
    shutdown_command = Shutdown_text.get()
    if not shutdown_command:
        messagebox.showwarning("Error", "Please enter a value.")
        return
    try:
        shutdown_command = int(Shutdown_text.get())
    except ValueError:
        messagebox.showwarning("Error", "Only Integers are allowed")
    if shutdown_command < 0:
        exit()
    else:
        Shutdown_set = True
        os.system(f"shutdown /s /t {shutdown_command}")
        grab()


# --------------------------------------------------------------------------------------------------


def shutdown_hours():
    global Shutdown_set
    if Shutdown_set:
        messagebox.showwarning("Error",
                               "Shutdown command is already set. You can give another command after restarting the system")
        return
    shutdown_command = Shutdown_text.get()
    if not shutdown_command:
        messagebox.showwarning("Error", "Please enter a value.")
        return
    try:
        shutdown_command = int(Shutdown_text.get())
    except ValueError:
        messagebox.showwarning("Error", "Only Integers are allowed")
    if shutdown_command < 1:
        exit()
    else:
        Shutdown_set = True
        shutdown_command *= 3600
        os.system(f"shutdown /s /t {shutdown_command}")
        grab()


# --------------------------------------------------------------------------------------------------


def grab():
    shutdown_ok = ttk.Label(Shutdown, text="Shutdown order set!", font=("Arial", 11))
    shutdown_ok.place(x=86, y=220)


# --------------------------------------------------------------------------------------------------


def shutdown_order():
    selected_button = button_var.get()
    if selected_button == "Hours":
        shutdown_hours()

    elif selected_button == "Minutes":
        shutdown_minutes()
    elif selected_button == "Seconds":
        shutdown_seconds()


# --------------------------------------------------------------------------------------------------


def callback(url):
    webbrowser.open_new_tab(url)


# --------------------------------------------------------------------------------------------------


Shutdown = Tk()
Shutdown.title("WinShut Scheduler")
Shutdown.geometry("300x330")

# image_path = "/Shutdown.png"  # Replace this with the actual absolute path

# try:
#     icon = PhotoImage(file=image_path)
#     Shutdown.iconphoto(False, icon)
# except Exception as e:
#     print("Error:", e)
# dropImg = PhotoImage(file='Shutdown.png')
# Tk.iconbitmap(dropImg)
# # Shutdown.iconphoto(False, dropImg)
# Shutdown.resizable(FALSE, FALSE)

Shutdown_Label = ttk.Label(Shutdown, text="Choose a unit that will be used:", font="Tahoma 8 bold")
Shutdown_Label.place(x=64, y=50)

# Choose unit buttons
button_var = StringVar()

Hours_Button = ttk.Button(Shutdown, text="Hours", command=lambda: button_var.set("Hours"))
Hours_Button.place(x=20, y=80, height=35)

Minutes_Button = ttk.Button(Shutdown, text="Minutes", command=lambda: button_var.set("Minutes"))
Minutes_Button.place(x=115, y=80, height=35)

Seconds_Button = ttk.Button(Shutdown, text="Seconds", command=lambda: button_var.set("Seconds"))
Seconds_Button.place(x=209, y=80, height=35)

input_label = ttk.Label(Shutdown, text="")
input_label.place(x=83, y=120)


def enter_the_number_off(*args):
    selected_button = button_var.get()
    if selected_button == "Hours":
        input_label.config(text="Enter the number of hours:")
    elif selected_button == "Minutes":
        input_label.config(text="Enter the number of minutes:")
        input_label.place_configure(x=78, y=120)
    elif selected_button == "Seconds":
        input_label.config(text="Enter the number of seconds:")
        input_label.place_configure(x=77, y=120)


button_var.trace("w", enter_the_number_off)

Shutdown_text = ttk.Entry(Shutdown, width=30)
Shutdown_text.place(x=59, y=140, height=25)

Shutdown_button = ttk.Button(Shutdown, text="Shutdown", command=shutdown_order)
Shutdown_button.place(x=114, y=180)

created_by = ttk.Label(Shutdown, text="Created by Abdullah-Dev115", font=("Arial", 9))
created_by.place(x=75, y=260)

github_link = Label(Shutdown, text="Abdullah-Dev115 Github", font=('Helveticabold', 10), fg="blue", cursor="hand2")
github_link.place(x=81, y=280)
github_link.bind("<Button-1>", lambda e: callback("https://github.com/Abdullah-Dev115"))

Shutdown.mainloop()
