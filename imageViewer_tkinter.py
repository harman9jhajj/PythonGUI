from tkinter import *
from PIL import Image,ImageTk

root = Tk()
my_img1 = ImageTk.PhotoImage(Image.open("d:/Harman/wallpapers/toronto-skyline-at-sunset.jpg"))
my_img2 = ImageTk.PhotoImage(Image.open("d:/Harman/wallpapers/python.ico"))
my_img3 = ImageTk.PhotoImage(Image.open("d:/Harman/wallpapers/man utd.jpg"))
my_img4 = ImageTk.PhotoImage(Image.open("d:/Harman/wallpapers/bubble_chat.ico"))
my_img5 = ImageTk.PhotoImage(Image.open("d:/Harman/wallpapers/calculator.ico"))

my_img_list = [my_img1, my_img2, my_img3, my_img4, my_img5]

status = Label(root, text="Image 1 of "+ str(len(my_img_list)), bd=1, relief=SUNKEN) #status button
my_label = Label(root, image=my_img1)
my_label.grid(row=0, column=0, columnspan=3)

def forward(img_num):
    global my_label
    global back_button
    global forward_button

    my_label.grid_forget()  #removes the current image
    my_label = Label(image = my_img_list[img_num-1]) #next image

    forward_button = Button(root, text=">>", command=lambda: forward(img_num+ 1))
    back_button = Button(root, text = "<<",command=lambda: back(img_num- 1))

    if img_num == 5:
        forward_button = Button(root, text=">>", state=DISABLED)
    my_label.grid(row=0, column=0, columnspan=3)
    back_button.grid(row=1, column=0)
    forward_button.grid(row=1, column=2)

    status = Label(root, text="Image "+ str(img_num) +" of " + str(len(my_img_list)), bd=1, relief=SUNKEN)  # update status button
    status.grid(row=2, column=0, columnspan=3, pady=10, sticky=W + E)

def back(img_num):
    global my_label
    global back_button
    global forward_button

    my_label.grid_forget()
    my_label = Label(image=my_img_list[img_num - 1])

    forward_button = Button(root, text=">>", command=lambda: forward(img_num + 1))
    back_button = Button(root, text="<<", command=lambda: back(img_num - 1))

    if img_num == 1:
        back_button = Button(root, text="<<", state=DISABLED)
    my_label.grid(row=0, column=0, columnspan=3)
    back_button.grid(row=1, column=0)
    forward_button.grid(row=1, column=2)

    status = Label(root, text="Image " + str(img_num) + " of " + str(len(my_img_list)), bd=1, #update status bar
                   relief=SUNKEN)  # status button
    status.grid(row=2, column=0, columnspan=3, pady=10, sticky=W + E)

back_button = Button(root, text = "<<", state=DISABLED) #initial stage
back_button.grid(row=1, column=0)

quit_button = Button(root, text = "exit", command=root.quit)
quit_button.grid(row=1, column=1)

forward_button = Button(root, text = ">>", command=lambda : forward(2)) #initial stage
forward_button.grid(row=1, column=2)

status.grid(row=2, column=0, columnspan=3, pady=10, sticky= W+E)


root.mainloop()