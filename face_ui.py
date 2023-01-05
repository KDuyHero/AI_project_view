import os
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
import tkinter
import cv2
from PIL import ImageTk, Image, ImageGrab
import matplotlib.pyplot as plt


def _from_rgb(rgb):
    """translates an rgb tuple of int to a tkinter friendly color code
    """
    return "#%02x%02x%02x" % rgb


win = Tk()
win.title("Nhận diện khuôn mặt")
win.geometry("1000x700")

# CONFIG
# PATH
base_dir = os.path.dirname(__file__)

# COLOR
lightGray = _from_rgb((240, 240, 240))
white = _from_rgb((255, 255, 255))

# FONT
font_header1 = "Arial 20 bold"
font_header2 = "Arial 16 bold"
font_content = "Arial 12"

# IMAGE
default_them_nguoi = Image.open(base_dir+"//imageGUI//default_Image.png")
default_them_nguoi = default_them_nguoi.resize(
    (560, int(3*560/4)), Image.ANTIALIAS)
default_them_nguoi = ImageTk.PhotoImage(default_them_nguoi)

default_empty = Image.open(base_dir+"//imageGUI//default_empty.png")
default_empty = default_empty.resize(
    (60, 60), Image.ANTIALIAS)
default_empty = ImageTk.PhotoImage(default_empty)

button_them_nguoi = Image.open(base_dir+"//imageGUI//button_them_nguoi.png")
button_them_nguoi = button_them_nguoi.resize(
    (60, 60), Image.ANTIALIAS)
button_them_nguoi = ImageTk.PhotoImage(button_them_nguoi)

arow = Image.open(base_dir+"//imageGUI//arow.png")
arow = arow.resize(
    (160, 80), Image.ANTIALIAS)
arow = ImageTk.PhotoImage(arow)
# End config

trang_chu = tkinter.Frame(win)
nhan_dien = tkinter.Frame(win)
them_nguoi = tkinter.Frame(win)

frames = (trang_chu, nhan_dien, them_nguoi)
for f in frames:
    f.place(relx=0, rely=0, relheight=1, relwidth=1, anchor=NW)


def switch(frame):
    # for f in frames:
    #     for widget in f.winfo_children():
    #         widget.destroy()
    if (frame == trang_chu):
        trangChu()
    elif (frame == nhan_dien):
        nhanDien()
    elif (frame == them_nguoi):
        themNguoi()
    frame.tkraise()


def trangChu():
    f_trang_chu = tkinter.Frame(
        trang_chu, padx=100, pady=100, bg='lightblue')
    f_trang_chu.place(
        relx=0, rely=0, relheight=1, relwidth=1, anchor=NW)
    f_trang_chu.grid_columnconfigure(0, weight=1)
    f_trang_chu.grid_columnconfigure(1, weight=1)
    f_trang_chu.grid_rowconfigure(0, weight=1)
    f_trang_chu.grid_rowconfigure(1, weight=1)

    tkinter.Label(f_trang_chu, text="Chọn chức năng", font=font_header1).grid(
        column=0, row=0, columnspan=2)
    tkinter.Button(f_trang_chu, text="Nhận diện", font=font_header2, command=lambda: switch(
        nhan_dien)).grid(column=0, row=1, columnspan=1, sticky=N)
    tkinter.Button(f_trang_chu, text="Thêm người", font=font_header2, command=lambda: switch(
        them_nguoi)).grid(column=1, row=1, columnspan=1, sticky=N)


def nhanDien():
    f_nhan_dien = tkinter.Frame(nhan_dien)
    f_nhan_dien.place(
        relx=0, rely=0, relheight=1, relwidth=1, anchor=NW)
    f_nhan_dien.grid_columnconfigure(0, weight=1)
    # f_nhan_dien.grid_columnconfigure(1, weight=1)
    f_nhan_dien_left = tkinter.Frame(
        f_nhan_dien, bg=lightGray, padx=20, pady=5)
    f_nhan_dien_left.place(
        relx=0, rely=0, relheight=1, relwidth=0.6, anchor=NW)

    f_nhan_dien_right = tkinter.Frame(f_nhan_dien, bg=white, padx=30, pady=5)
    f_nhan_dien_right.place(
        relx=1, rely=0, relheight=1, relwidth=0.4, anchor=NE)

    f_nhan_dien_left.grid_columnconfigure(0, weight=1)
    f_nhan_dien_left.grid_columnconfigure(1, weight=1)
    f_nhan_dien_left.grid_rowconfigure(0, weight=1)
    f_nhan_dien_left.grid_rowconfigure(1, weight=1)
    f_nhan_dien_left.grid_rowconfigure(2, weight=1)
    f_nhan_dien_left.grid_rowconfigure(3, weight=9)
    # f_nhan_dien_left.grid_rowconfigure(4, weight=5)

    tkinter.Button(f_nhan_dien_left, text="Trở về", font=font_content, command=lambda: switch(
        trang_chu)).grid(column=0, row=0, columnspan=2, sticky=NW)
    tkinter.Label(f_nhan_dien_left, text="Nhận diện khuôn mặt",
                  font=font_header1, anchor=W).grid(column=0, row=1, columnspan=2, sticky=W)
    tkinter.Label(f_nhan_dien_left,
                  text="Đưa mặt vào trước camera để nhận diện",
                  font=font_content, anchor=W, wraplength=500, justify=LEFT).grid(row=2, column=0, columnspan=2, sticky=NW)
    camera = tkinter.Label(f_nhan_dien_left, text="", image=default_them_nguoi).grid(
        column=0, row=3, columnspan=2, sticky=NW)

    # captureButton = tkinter.Button(
    #     f_nhan_dien_left, text="Chụp ảnh", font=font_header2, command="")
    # captureButton.grid(column=0, row=4, columnspan=1, sticky=N)

    # finishButton = tkinter.Button(
    #     f_nhan_dien_left, text="Kết thúc", font=font_header2, command="")
    # finishButton.grid(column=1, row=4, columnspan=1, sticky=N)

    # RIGHT


def themNguoi():
    f_them_nguoi = tkinter.Frame(them_nguoi)
    f_them_nguoi.place(
        relx=0, rely=0, relheight=1, relwidth=1, anchor=NW)

    f_them_nguoi_left = tkinter.Frame(
        f_them_nguoi, bg=lightGray, padx=20, pady=5)
    f_them_nguoi_left.place(
        relx=0, rely=0, relheight=1, relwidth=0.6, anchor=NW)

    f_them_nguoi_right = tkinter.Frame(f_them_nguoi, bg=white, padx=30, pady=5)
    f_them_nguoi_right.place(
        relx=1, rely=0, relheight=1, relwidth=0.4, anchor=NE)

    f_them_nguoi_left.grid_columnconfigure(0, weight=1)
    f_them_nguoi_left.grid_columnconfigure(1, weight=1)
    f_them_nguoi_left.grid_rowconfigure(0, weight=1)
    f_them_nguoi_left.grid_rowconfigure(1, weight=1)
    f_them_nguoi_left.grid_rowconfigure(2, weight=1)
    f_them_nguoi_left.grid_rowconfigure(3, weight=9)
    f_them_nguoi_left.grid_rowconfigure(4, weight=5)

    tkinter.Button(f_them_nguoi_left, text="Trở về", font=font_content, command=lambda: switch(
        trang_chu)).grid(column=0, row=0, columnspan=2, sticky=NW)
    tkinter.Label(f_them_nguoi_left, text="Nhận diện khuôn mặt",
                  font=font_header1, anchor=W).grid(column=0, row=1, columnspan=2, sticky=W)
    tkinter.Label(f_them_nguoi_left,
                  text="Để thêm một khuôn mặt mới, nhấn vào biểu tượng dấu cộng ở màn hình bên tay phải",
                  font=font_content, anchor=W, wraplength=500, justify=LEFT).grid(row=2, column=0, columnspan=2, sticky=NW)
    camera = tkinter.Label(f_them_nguoi_left, text="", image=default_them_nguoi).grid(
        column=0, row=3, columnspan=2, sticky=NW)

    captureButton = tkinter.Button(
        f_them_nguoi_left, text="Chụp ảnh", font=font_header2, command="")
    captureButton.grid(column=0, row=4, columnspan=1, sticky=N)

    finishButton = tkinter.Button(
        f_them_nguoi_left, text="Kết thúc", font=font_header2, command="")
    finishButton.grid(column=1, row=4, columnspan=1, sticky=N)

    # RIGHT
    f_them_nguoi_right.grid_columnconfigure(0, weight=1)
    f_them_nguoi_right.grid_columnconfigure(1, weight=1)
    f_them_nguoi_right.grid_columnconfigure(2, weight=1)
    f_them_nguoi_right.grid_rowconfigure(0, weight=2)
    f_them_nguoi_right.grid_rowconfigure(1, weight=2)
    f_them_nguoi_right.grid_rowconfigure(2, weight=2)
    f_them_nguoi_right.grid_rowconfigure(3, weight=3)

    tkinter.Label(f_them_nguoi_right, text="Thêm khuôn mặt mới", bg=white,
                  font=font_header2, fg='lightblue', justify=CENTER).grid(column=0, row=0, columnspan=3, sticky=S)
    tkinter.Label(f_them_nguoi_right, image=arow, bg=white, justify=CENTER).grid(
        column=0, row=1, columnspan=3, sticky=W)

    tkinter.Button(f_them_nguoi_right, image=button_them_nguoi, relief=FLAT, command="").grid(
        column=0, row=2, columnspan=1, sticky=NW)

    listButton = []
    for i in range(5):
        listButton.append(tkinter.Button(f_them_nguoi_right,
                          image=default_empty, relief=FLAT))

    '''Set image for button'''

    listButton[0].grid(column=1, row=2, columnspan=1, sticky=N)
    listButton[1].grid(column=2, row=2, columnspan=1, sticky=NE)
    listButton[2].grid(column=0, row=2, columnspan=1, sticky=SW)
    listButton[3].grid(column=1, row=2, columnspan=1, sticky=S)
    listButton[4].grid(column=2, row=2, columnspan=1, sticky=SE)


switch(nhan_dien)
win.mainloop()
