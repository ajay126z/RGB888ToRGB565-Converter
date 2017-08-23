# -*- coding: utf-8 -*-

import Image, ImageTk
import os, sys
import struct
from ctypes import *
import Tkinter
import tkFileDialog
import PIL
import tkMessageBox

libc = cdll.msvcrt

r,b,g = 0,0,0
ls = [r,g,b]
temp = 0

libcall_c = CDLL('final.so')

root = Tkinter.Tk(className = "\RGB(888)->RGB(565) Converter")
menubar = Tkinter.Menu(root)
frame = Tkinter.Frame(root)

def exit_mainloop ():
    global root
    root.destroy() # this will cause mainloop to unblock.

def help_about():
    tkMessageBox.showinfo("Help...", "This Software is created by Ajay Zapadiya.\n" +
                          "\nThis Program is used to convert RGB(888) format to RGB(565) format. \nIt can be used with 3 image formats(jpg,png and bmp) with any resolution. \n" +
                          "Simply Open the Image and It will be converted into RGB(565) in the same directory of image.\nHere Default Extension is nothing, hence FILE type."+
                          "\nI Hope that it will be helpful.\n\n" +
                          "BUG : When we open second image it is displayed on the same frame with exsisting image. So window size is increased. :-O")

def open_file():
    #frame = Tkinter.Frame(root)
    global frame
    global root
    frame.pack()
    frame.fileName = tkFileDialog.askopenfilename()
    im = Image.open(frame.fileName)
    
    label_image = ImageTk.PhotoImage(image = im)
    label = Tkinter.Label(frame, image = label_image)
    
    label.label_image = label_image  # keep copy
    label.pack(side = "bottom", fill = "both", expand = "yes")
    
    "This is used to find the name of file without path : "
    rev_name = frame.fileName[-1:-len(frame.fileName)-1:-1]
    actual_name = rev_name[rev_name.find("/")-1:rev_name.find("."):-1]
    ext = frame.fileName[frame.fileName.find("."):]
    image_name = actual_name + ext

    if (image_name[image_name.find(".")+1:] == "jpg") or (image_name[image_name.find(".")+1:] == "jpeg") or (image_name[image_name.find(".")+1:] == "png") or (image_name[image_name.find(".")+1:] == "bmp"):
        im_data_aquire(frame.fileName)
    root.mainloop()


def im_data_aquire(Im_name):
    im = Image.open(Im_name)
    pix = im.load()

    rev_name = Im_name[-1:-len(Im_name)-1:-1]
    actual_name = rev_name[rev_name.find("/")-1:rev_name.find("."):-1]
    ext = frame.fileName[Im_name.find("."):]
    f_name = actual_name + ".txt"
    
    path = Im_name[:Im_name.find(actual_name)]
    path_txt = path + f_name
    path_file = path + actual_name

    print "Location = " + path
    print "File_Name = " + actual_name + ext
    print ('Image Size = %d x %d' % (im.size[0],im.size[1]))
    print "Image Format : " + im.format

    '''width,height = im.size[0], im.size[1]
    print "width : {}".format(width)
    print "height : {}".format(height)'''
    f = open(path_txt,'w+')
    for i in range(im.size[0]):
        for j in range(im.size[1]):
            ls = list(im.getpixel((i,j)))
            for k in range(len(ls)):
                temp = ls[k]
                temp = str(temp) + " "
                f.write(temp)
    f.close()
    name = c_char_p(path_txt)
    newfilename = c_char_p(path_file)
    im_width, im_height = c_uint(im.size[0]), c_uint(im.size[1])
    libcall_c.data_processing(name, im_width, im_height, newfilename)
    os.remove(path_txt) # This will remove your txt file and save space...
    print "\nNow go to Image Directory(Location)...!"
    print "\nHave you got raw image file? I hope you got."
    print "The size of Raw Image File : %d Bytes" % (im.size[0]*im.size[1]*2)
    print "\nNow Have Fun... :-)"



'''def update_file():
    global frame,img
    frame.destroy()
    open_file()
    #frame.pack()
    frame.fileName = tkFileDialog.askopenfilename()
    im = Image.open(frame.fileName)
    #print ('%dx%d' % (im.size[0],im.size[1]))
    label_image = ImageTk.PhotoImage(image = im)
    label = Tkinter.Label(frame, image = label_image)
    if old_label_image is not None:
        old_labe_image.destroy()
    old_labe_image = label
    #label.label_image = label_image  # keep copy
    label.pack(side = "bottom", fill = "both", expand = "yes")
    print frame.fileName
    #im_data_aquire(frame.fileName)
    root.mainloop()'''


filemenu = Tkinter.Menu(menubar, tearoff = 0)
menubar.add_cascade(label = "File", menu = filemenu)
filemenu.add_command(label = "Open", command = open_file)
#filemenu.add_command(label = "Update Image", command = update_file)
filemenu.add_separator()
filemenu.add_command(label = "Exit", command = exit_mainloop)

helpmenu = Tkinter.Menu(menubar, tearoff = 0)
menubar.add_cascade(label= "Help", menu = helpmenu)
helpmenu.add_command(label="About...", command=help_about)

root.config(menu = menubar)
root.mainloop()
