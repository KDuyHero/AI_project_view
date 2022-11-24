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
# config window
win.title("Nhận diện khuôn mặt")
win_w = 1000
win_h = int(0.72*win_w)

frame1_w = win_w*0.6
frame1_h = win_h
bgFrame1 = _from_rgb((240, 240, 240))

frame2_w = win_w - frame1_w
frame2_h = win_h
bgFrame2 = _from_rgb((255, 255, 255))

pixel = tkinter.PhotoImage(width=1, height=1)
# If camera = false => dừng video
camera = True
# If capture = True => chụp ảnh
capture = False


def startVideo():
    global camera
    camera = True
    show_frames()


def endVideo():
    global camera, labelVideo
    labelVideo['image'] = defaultImage
    camera = False


def takeAPhoto():
    global capture
    capture = True


win.geometry(f"{win_w}x{win_h}")

# Frame1
frame1 = tkinter.Frame(win, width=frame1_w, height=frame1_h,
                       bg=bgFrame1)
# neo góc NW của đối tượng (góc trên bên trái) vào tọa độ đã cài đặt
frame1.place(relx=0, rely=0, anchor=NW)

label1In1 = tkinter.Label(frame1, text="Nhận diện khuôn mặt", font="Helvetica " + str(int(0.036*win_h)),
                          fg="black", bg=bgFrame1, justify=LEFT)
label1In1.place(relx=0.04, rely=0.09, anchor=NW)

label2In1 = tkinter.Label(
    frame1, text="Để thêm một gương mặt mới, nhấn vào dấu cộng\nở màn hình bên phải", font="Helvetica " + str(int(0.023*win_h)), fg=_from_rgb((80, 80, 80)), bg=bgFrame1, justify=LEFT)
label2In1.place(relx=0.04, rely=0.16, anchor=NW)

# START Video in Frame 1
# image without camera
load_img = (Image.open(
    r"D:\K65-Computer Science-BKHN\2022-1\Nhap_mon_tri_tue_nhan_tao\Project\default_Image.png"))
load_img = load_img.resize((int(0.49*win_w), int(0.53*win_h)), Image.ANTIALIAS)
defaultImage = ImageTk.PhotoImage(load_img)

labelVideo = tkinter.Label(frame1, text="", bg=bgFrame1, image=defaultImage)
labelVideo.place(relx=0.04, rely=0.26, anchor=NW)

# Create a camera
cap = cv2.VideoCapture(0)
# Define function to show frame


def show_frames():
    global capture
    # Dừng video
    if camera == False:
        return
    # Get the latest frame and convert into Image
    frame = cap.read()[1]
    cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(cv2image)
    img = img.resize((int(0.49*win_w), int(0.53*win_h)), Image.ANTIALIAS)
    # Convert image to PhotoImage
    imgtk = ImageTk.PhotoImage(image=img)
    if capture:
        print("Captured!")
        photoSave = img
        photoSave = cv2.resize(src=photoSave, dsize=(640, 480))
        print(photoSave)
        cv2.imwrite("saved.png", photoSave)
        # plt.imshow(photoSave, cmap='gray')
        # get img capture
        # end capture
        capture = False
    labelVideo.imgtk = imgtk
    labelVideo.configure(image=imgtk)

    # Repeat after an interval to capture continiously
    labelVideo.after(15, show_frames)


# End video

# chụp và dừng video button
# tạo frame chứa 2 button
frame1In1 = tkinter.Frame(
    frame1, height=int(0.1*win_h), width=int(0.4*win_w))
frame1In1.place(relx=0.45, rely=0.83, anchor=N)
# button chụp ảnh
buttonCapture = tkinter.Button(
    frame1In1, text="Chụp", font="Helvetica " + str(int(0.025*win_h)), command=takeAPhoto)
buttonCapture.place(relx=0, rely=0, anchor=NW)
# button dừng chụp

buttonCapture = tkinter.Button(
    frame1In1, text="Kết thúc", font="Helvetica " + str(int(0.025*win_h)), command=endVideo)
buttonCapture.place(relx=1, rely=0, anchor=NE)
# END Frame1
# ----------------------------------------------------------------------------------------------
# START Frame2
frame2 = tkinter.Frame(win, width=frame2_w,
                       height=frame2_h, bg="white", pady=0)
# neo góc NE (góc trên bên phải) vào tọa độ được cài
frame2.place(relx=1, rely=0, anchor=NE)

label1In2 = tkinter.Label(frame2, text="Thêm một khuôn mặt mới",
                          font="Helvetica " + str(int(0.025*win_h)), bg=bgFrame2, fg="blue")
label1In2.place(relx=0.5, rely=0.22, anchor=N)

# ảnh mũi tên
load_img = (Image.open(
    r"D:\K65-Computer Science-BKHN\2022-1\Nhap_mon_tri_tue_nhan_tao\Project\arow.png"))
load_img = load_img.resize(
    (int(0.085*win_h), int(0.085*win_h)), Image.ANTIALIAS)
arowImage = ImageTk.PhotoImage(load_img)

label2In2 = tkinter.Label(frame2, text="", bg=bgFrame2, image=arowImage)
label2In2.place(relx=0.5, rely=0.26, anchor=N)

# tạo frame chứa 6 khung display ảnh
frame1In2 = tkinter.Frame(frame2, height=int(
    0.20*win_h), width=int(0.31*win_h), bg=bgFrame2)
frame1In2.place(relx=0.5, rely=0.44, anchor=N)

size_image_display = int(0.08*win_h)
bg_image_display = _from_rgb((160,  160, 160))
addButton = tkinter.Button(
    frame1In2, text="+", font="Helvetica " + str(int(0.8*size_image_display))+" bold", justify=CENTER,
    fg="blue", bg=bg_image_display, relief=FLAT, height=size_image_display, width=size_image_display,
    image=pixel, command=startVideo)

addButton.place(relx=0, rely=0, anchor=NW)

imageButton1 = tkinter.Button(
    frame1In2, text="", bg=bg_image_display, relief=FLAT, height=size_image_display, width=size_image_display, image=pixel)

imageButton1.place(relx=0.5, rely=0, anchor=N)

imageButton2 = tkinter.Button(
    frame1In2, text="", bg=bg_image_display, relief=FLAT, height=size_image_display, width=size_image_display, image=pixel)

imageButton2.place(relx=1, rely=0, anchor=NE)

imageButton3 = tkinter.Button(
    frame1In2, text="", bg=bg_image_display, relief=FLAT, height=size_image_display, width=size_image_display, image=pixel)

imageButton3.place(relx=0, rely=1, anchor=SW)

imageButton4 = tkinter.Button(
    frame1In2, text="", bg=bg_image_display, relief=FLAT, height=size_image_display, width=size_image_display, image=pixel)

imageButton4.place(relx=0.5, rely=1, anchor=S)

imageButton5 = tkinter.Button(
    frame1In2, text="", bg=bg_image_display, relief=FLAT, height=size_image_display, width=size_image_display, image=pixel)

imageButton5.place(relx=1, rely=1, anchor=SE)


# END Frame2
win.mainloop()
