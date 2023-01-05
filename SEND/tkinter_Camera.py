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
# config window
win.title("Nhận diện khuôn mặt")
win_w = 1000
win_h = int(0.72*win_w)
win.resizable(False, False)

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

count = 0
# path thư mục hiện tại
base_dir = os.path.dirname(__file__)
name = ""
# base folder image person
base_path_image = base_dir + "\\image\\"
# base foler image GUI
base_path_GUI = base_dir + "\\imageGUI\\"


def startVideo():
    global camera, count
    path = base_path_image+name
    if not os.path.exists(path):
        os.makedirs(path)
    count = len(os.listdir(path))
    camera = True
    show_frames()


def endVideo():
    global camera, labelVideo, name
    name = ""
    labelVideo['image'] = defaultImage
    camera = False
    reRenderImageButton()


def takeAPhoto():
    global capture
    capture = True


def save(file_name, img, path):
    # Set vị trí lưu ảnh
    os.chdir(path)
    # Lưu ảnh
    cv2.imwrite(file_name, img)


def getName():
    top = tkinter.Toplevel(win)

    top.title("window")
    top.geometry("230x100")

    label = tkinter.Label(top, text="Nhập tên:", font="Arial 16 bold")
    label.place(relx=0.5, rely=0.2, anchor=N)

    text = tkinter.Text(top, height=1, width=20)
    text.place(relx=0.5, rely=0.5, anchor=N)

    def get():
        global name
        name = text.get(1.0, END)[0:-1]
        startVideo()
        top.destroy()

    button = tkinter.Button(top, text="OK", command=get)
    button.place(relx=0.5, rely=0.8, anchor=N)


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
    base_path_GUI+'default_Image.png'))
load_img = load_img.resize((int(0.49*win_w), int(0.53*win_h)), Image.ANTIALIAS)
defaultImage = ImageTk.PhotoImage(load_img)

labelVideo = tkinter.Label(frame1, text="", bg=bgFrame1, image=defaultImage)
labelVideo.place(relx=0.04, rely=0.26, anchor=NW)

# Create a camera
cap = cv2.VideoCapture(0)
# Define function to show frame


def show_frames():
    global capture, name, count
    new_path = base_path_image + name

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
        count += 1
        # tạo tên ảnh
        file_name = name + str(count)+".png"
        print("Captured!")
        photoSave = cv2image
        photoSave = cv2.resize(src=photoSave, dsize=(640, 480))
        save(file_name, photoSave, new_path)
        # plt.imshow(photoSave, cmap='gray')
        # get img capture
        # end capture
        capture = False
    labelVideo.imgtk = imgtk
    labelVideo.configure(image=imgtk)

    # Repeat after an interval to capture continiously
    labelVideo.after(5, show_frames)


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
    base_path_GUI+"arow.png"))
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
load_img = (Image.open(
    base_path_GUI+"image_add_button.png"))
load_img = load_img.resize(
    (size_image_display, size_image_display), Image.ANTIALIAS)
image_add_button_defailt = ImageTk.PhotoImage(load_img)
addButton = tkinter.Button(
    frame1In2, text="+", font="Helvetica " + str(int(0.8*size_image_display))+" bold", justify=CENTER,
    fg="blue", bg=bg_image_display, relief=FLAT, height=size_image_display, width=size_image_display,
    image=image_add_button_defailt, command=getName)

addButton.place(relx=0, rely=0, anchor=NW)

load_img = (Image.open(
    base_path_GUI+"image_button_default.png"))
load_img = load_img.resize(
    (size_image_display, size_image_display), Image.ANTIALIAS)
image_button_defailt = ImageTk.PhotoImage(load_img)

list_image = [image_button_defailt, image_button_defailt,
              image_button_defailt, image_button_defailt, image_button_defailt]

imageButton1 = tkinter.Button(
    frame1In2, text="", bg=bg_image_display, relief=FLAT, height=size_image_display, width=size_image_display, image=list_image[0])

imageButton1.place(relx=0.5, rely=0, anchor=N)

imageButton2 = tkinter.Button(
    frame1In2, text="", bg=bg_image_display, relief=FLAT, height=size_image_display, width=size_image_display, image=list_image[1])

imageButton2.place(relx=1, rely=0, anchor=NE)

imageButton3 = tkinter.Button(
    frame1In2, text="", bg=bg_image_display, relief=FLAT, height=size_image_display, width=size_image_display, image=list_image[2])

imageButton3.place(relx=0, rely=1, anchor=SW)

imageButton4 = tkinter.Button(
    frame1In2, text="", bg=bg_image_display, relief=FLAT, height=size_image_display, width=size_image_display, image=list_image[3])

imageButton4.place(relx=0.5, rely=1, anchor=S)

imageButton5 = tkinter.Button(
    frame1In2, text="", bg=bg_image_display, relief=FLAT, height=size_image_display, width=size_image_display, image=list_image[4])

imageButton5.place(relx=1, rely=1, anchor=SE)

list_imageButton = [imageButton1, imageButton2,
                    imageButton3, imageButton4, imageButton5]


def reRenderImageButton():

    folder_image = [os.path.join(base_path_image, f)
                    for f in os.listdir(base_path_image)]
    for i in range(len(folder_image)):
        if (i > 4):
            break
        else:
            path_folder = folder_image[i]
            if not len(os.listdir(path_folder)):
                continue
            else:
                image_path = os.path.join(
                    path_folder, os.listdir(path_folder)[0])
                load_img = (Image.open(
                    image_path))
                load_img = load_img.resize(
                    (size_image_display, size_image_display), Image.ANTIALIAS)
                list_image[i] = ImageTk.PhotoImage(load_img)
                list_imageButton[i]['image'] = list_image[i]


reRenderImageButton()

# END Frame2
win.mainloop()
