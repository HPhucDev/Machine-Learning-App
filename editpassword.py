import webbrowser
import re
import sys
import os
import tkinter as tk
from pathlib import Path
from tkinter import *
from PIL import Image, ImageTk
# Path to asset files for this GUI window.
ASSETS_PATH = Path(__file__).resolve().parent / "assets"

window = tk.Tk()
logo = tk.PhotoImage(file=ASSETS_PATH / "iconbitmap.gif")
window.call('wm', 'iconphoto', window._w, logo)
window.title("Change Password")
window.geometry("360x450")
window.configure(bg="#3A7FF6")

canvas = tk.Canvas(
    window, bg="#3A7FF6", height=400, width=360,
    bd=0, highlightthickness=0, relief="ridge")
canvas.place(x=0, y=0)

canvas.create_text(
    170.5, 38.0, text="Change password",
    fill="#FFFFFF", font=("Arial-BoldMT", int(28.0)))


text_box_bg = tk.PhotoImage(
    file=ASSETS_PATH / "TextBox_Bg.png")  # Textbox background

CMND_entry_img = canvas.create_image(
    180.0, 126.5, image=text_box_bg)  # background
CMND_entry = tk.Entry(bd=0, bg="#F6F7F9", highlightthickness=0)
CMND_entry.place(x=20.0, y=87+25, width=321.0, height=35)
CMND_entry.focus()
canvas.create_text(
    20.0, 106.0, text="CMND: ", fill="#515486",
    font=("Arial-BoldMT", int(13.0)), anchor="w")

password_old_entry_img = canvas.create_image(
    180.0, 206.5, image=text_box_bg)  # background
password_old_entry = tk.Entry(
    bd=0, bg="#F6F7F9", highlightthickness=0, show="*")
password_old_entry.place(x=20.0, y=168+25, width=321.0, height=35)
canvas.create_text(
    20.0, 234.5-50, text="Password old: ", fill="#515486",
    font=("Arial-BoldMT", int(13.0)), anchor="w")

password_new_entry_img = canvas.create_image(
    180.0, 336.5-50, image=text_box_bg)  # background
password_new_entry = tk.Entry(
    bd=0, bg="#F6F7F9", highlightthickness=0, show="*")
password_new_entry.place(x=20.0, y=312+10-50, width=321.0, height=35)
canvas.create_text(
    20.0, 312.5-48, text="Password new: ", fill="#515486",
    font=("Arial-BoldMT", int(13.0)), anchor="w")

generate_btn_img = tk.PhotoImage(file=ASSETS_PATH / "btn_confirm.png")
generate_btn = tk.Button(
    image=generate_btn_img, borderwidth=10, highlightthickness=0, relief="flat")
generate_btn.place(x=75, y=350, width=195, height=69)


window.resizable(False, False)
window.mainloop()
