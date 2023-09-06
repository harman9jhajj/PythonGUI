from tkinter import *
from PIL import Image,ImageTk
from tkinter import filedialog
root = Tk()
root.title("my GUI")
root.iconbitmap("d:/Harman/wallpapers/python.ico")

def open():
    global my_img
    #returns file location
    root.filename = filedialog.askopenfilename(initialdir="d:/Harman/wallpapers", title="Select a file",filetypes=(("png files","*.png"),("all files","*.*")))
    Label(root, text=root.filename).pack()
    my_img = ImageTk.PhotoImage(Image.open(root.filename))
    my_img_label = Label(root, image=my_img)
    my_img_label.pack()
    Button(root, text= "Close", command=root.destroy).pack()

Button(root, text="Open File", command=open).pack()



root.mainloop()