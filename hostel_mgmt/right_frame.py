import tkinter
from hostel_mgmt import root
from PIL import Image, ImageTk
from hostel_mgmt.design import right_frame

image_load = Image.open("./Fee Chart.png")
image_render = ImageTk.PhotoImage(image_load)


pos = {'x': 12, 'btn1': 10, 'btn2': 60, 'btn3': 110, 'btn4': 160, 'btn5': 210, 'btn6': 260, 'btn7':310}

btn1 = tkinter.Button(right_frame, text="Button 1", bg="bisque3", activebackground="bisque3", relief="flat", font=("Courier New", 12), cursor="hand2", width=26)

btn2 = tkinter.Button(right_frame, text="Button 2", bg="bisque3", activebackground="bisque3", relief="flat", font=("Courier New", 12), cursor="hand2", width=26)

btn3 = tkinter.Button(right_frame, text="Button 3", bg="bisque3", activebackground="bisque3", relief="flat", font=("Courier New", 12), cursor="hand2", width=26)


btn4 = tkinter.Button(right_frame, text="Button 4", bg="bisque3", activebackground="bisque3", relief="flat", font=("Courier New", 12), cursor="hand2", width=26)

img = tkinter.Label(right_frame, image=image_render)
img.image = image_render
img.config(bg='bisque4')
img.place(x=5, y=435)

btn_list = [btn1, btn2, btn3, btn4]



