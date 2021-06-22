import tkinter
from hostel_mgmt import root


left_frame = tkinter.Frame(root, bg="bisque4", width=300, height=root.winfo_screenheight())
left_frame.grid(row=0, column=0)
center_frame = tkinter.Frame(root, bg="bisque3", width=root.winfo_screenwidth()-600, height=root.winfo_screenheight())
center_frame.grid(row=0, column=1)
right_frame = tkinter.Frame(root, bg="bisque4", width=300, height=root.winfo_screenheight())
right_frame.grid(row=0, column=2)



import hostel_mgmt.left_frame
import hostel_mgmt.center_frame
import hostel_mgmt.right_frame
