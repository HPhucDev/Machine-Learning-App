import webbrowser
import re
import sys
import os
import tksheet
import tkinter as tk
from pathlib import Path
from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
from time import strftime
# Path to asset files for this GUI window.
ASSETS_PATH = Path(__file__).resolve().parent / "assets"

window = tk.Tk()
logo = tk.PhotoImage(file=ASSETS_PATH / "iconbitmap.gif")
window.call('wm', 'iconphoto', window._w, logo)
window.title("Dashboard")
window.geometry("960x650")
window.configure(bg="#ECECEC")

canvas = tk.Canvas(
    window, bg="#ECECEC", height=650, width=1260,
    bd=0, highlightthickness=0, relief="ridge")
canvas.place(x=0, y=0)

camera_bg = tk.PhotoImage(
    file=ASSETS_PATH / "camerabackground.png")  # Camera background

camera_img = canvas.create_image(200, 200, image=camera_bg)
canvas.create_text(
    200, 40.0, text="Camera In",
    fill="#000000", font=("Arial-BoldMT", int(25.0)))
loadcamerain_btn_img = tk.PhotoImage(file=ASSETS_PATH / "btn_loadcamerain.png")
loadcamerain_btn = tk.Button(window,
                             image=loadcamerain_btn_img, borderwidth=10, highlightthickness=0, relief="flat")
loadcamerain_btn.place(x=110, y=350, width=195, height=73)
checkin_btn_img = tk.PhotoImage(file=ASSETS_PATH / "btn_checkin.png")
checkin_btn = tk.Button(window,
                        image=checkin_btn_img, borderwidth=10, highlightthickness=0, relief="flat")
checkin_btn.place(x=110, y=420, width=195, height=73)


camera_img = canvas.create_image(520, 200, image=camera_bg)
canvas.create_text(
    520, 40.0, text="Camera Out",
    fill="#000000", font=("Arial-BoldMT", int(25.0)))
loadcameraout_btn_img = tk.PhotoImage(
    file=ASSETS_PATH / "btn_loadcameraout.png")
loadcameraout_btn = tk.Button(window,
                              image=loadcameraout_btn_img, borderwidth=10, highlightthickness=0, relief="flat")
loadcameraout_btn.place(x=420, y=350, width=195, height=73)
checkout_btn_img = tk.PhotoImage(
    file=ASSETS_PATH / "btn_checkout.png")
checkout_btn = tk.Button(window,
                         image=checkout_btn_img, borderwidth=10, highlightthickness=0, relief="flat")
checkout_btn.place(x=420, y=420, width=195, height=73)

canvas.create_text(
    520, 40.0, text="Camera Out",
    fill="#000000", font=("Arial-BoldMT", int(25.0)))

canvas.create_text(
    70, 530.0, text="Note:",
    fill="#000000", font=("Arial-BoldMT", int(15.0)))
canvas.create_text(
    320, 560.0, text="6:00 AM to 6:30 PM: 1.000 VND /1 bike / 1 time ; 4.000 VND /1 motobike / 1 time   ",
    fill="#000000", font=("Arial-BoldMT", int(13.0)))
canvas.create_text(
    320, 590.0, text="6:31 PM to 9:30 PM: 2.000 VND /1 bike / 1 time ; 5.000 VND /1 motobike / 1 time   ",
    fill="#000000", font=("Arial-BoldMT", int(13.0)))
canvas.create_text(
    370, 620.0, text="If total time is more than 12 hours : 4.000 VND /1 bike / 1 time ; 10.000 VND /1 motobike / 1 time   ",
    fill="#000000", font=("Arial-BoldMT", int(13.0)))

space_btn_img = tk.PhotoImage(
    file=ASSETS_PATH / "btn_space.png")
space_btn = tk.Button(window,
                      image=space_btn_img, borderwidth=10, highlightthickness=0, relief="flat")
space_btn.place(x=710, y=410, width=200, height=82)

changepassword_btn_img = tk.PhotoImage(
    file=ASSETS_PATH / "btn_changepassword.png")
changepassword_btn = tk.Button(window,
                               image=changepassword_btn_img, borderwidth=10, highlightthickness=0, relief="flat")
changepassword_btn.place(x=710, y=540, width=195, height=73)


canvas.create_text(
    730, 40.0, text="Date Time:",
    fill="#000000", font=("Arial-BoldMT", int(20.0)))


def time():
    string = strftime('%H:%M:%S %p')
    lbl.config(text=string)
    lbl.after(1000, time)


lbl = Label(window, font=('Arial-BoldMT', 20),
            background='#ECECEC',
            foreground='#000000')
lbl.pack()
lbl.place(x=780, y=26)
time()

detail_bg = tk.PhotoImage(
    file=ASSETS_PATH / "detailbackground.png")
detail_img = canvas.create_image(800, 226, image=detail_bg)
canvas.create_text(
    703, 90.0, text="Detail:",
    fill="#000000", font=("Arial-BoldMT", int(13.0)))
canvas.create_text(
    714, 140.0, text="Name:",
    fill="#000000", font=("Arial-BoldMT", int(15.0)))
canvas.create_text(
    720, 140.0+35, text="ID Card:",
    fill="#000000", font=("Arial-BoldMT", int(15.0)))
canvas.create_text(
    720, 140.0+35*2, text="Time In:",
    fill="#000000", font=("Arial-BoldMT", int(15.0)))
canvas.create_text(
    725, 140.0+35*3, text="Time Out:",
    fill="#000000", font=("Arial-BoldMT", int(15.0)))
canvas.create_text(
    752, 140.0+35*4, text="License Plate In:",
    fill="#000000", font=("Arial-BoldMT", int(15.0)))
canvas.create_text(
    757, 140.0+35*5, text="License Plate Out:",
    fill="#000000", font=("Arial-BoldMT", int(15.0)))
canvas.create_text(
    740, 140.0+35*7, text="Payment Fees:",
    fill="#000000", font=("Arial-BoldMT", int(15.0)))


window.resizable(False, False)
window.mainloop()
