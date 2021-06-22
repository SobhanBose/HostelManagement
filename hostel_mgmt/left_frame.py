import tkinter
from hostel_mgmt import root
from hostel_mgmt.design import left_frame
from hostel_mgmt.left_frame_func import chng1, chng2, chng3, chng4, chng5, chng6, chng7, chng8, ref, chg_pswd, _exit
# from hostel_mgmt.left_frame_func import chng1, chng2, chng3, chng4, chng5, chng6, chng7, chng8

btn1 = tkinter.Button(left_frame, text="Student Details", bg="bisque3", activebackground="bisque3", relief="flat", font=("Courier New", 12), cursor="hand2", width=27, command=chng1)
btn1.place(x=10, y=10)

btn2 = tkinter.Button(left_frame, text="Block/Room Details", bg="bisque3", activebackground="bisque3", relief="flat", font=("Courier New", 12), cursor="hand2", width=27, command=chng2)
btn2.place(x=10, y=60)

btn3 = tkinter.Button(left_frame, text="Mess", bg="bisque3", activebackground="bisque3", relief="flat", font=("Courier New", 12), cursor="hand2", width=27, command=chng3)
btn3.place(x=10, y=110)

btn4 = tkinter.Button(left_frame, text="Staff", bg="bisque3", activebackground="bisque3", relief="flat", font=("Courier New", 12), cursor="hand2", width=27, command=chng4)
btn4.place(x=10, y=160)

btn5 = tkinter.Button(left_frame, text="Courses", bg="bisque3", activebackground="bisque3", relief="flat", font=("Courier New", 12), cursor="hand2", width=27, command=chng5)
btn5.place(x=10, y=210)

btn6 = tkinter.Button(left_frame, text="Fee Payment", bg="bisque3", activebackground="bisque3", relief="flat", font=("Courier New", 12), cursor="hand2", width=27, command=chng6)
btn6.place(x=10, y=260)

btn7 = tkinter.Button(left_frame, text="Billing", bg="bisque3", activebackground="bisque3", relief="flat", font=("Courier New", 12), cursor="hand2", width=27, command=chng7)
btn7.place(x=10, y=310)

btn8 = tkinter.Button(left_frame, text="Delete record(s)", bg="bisque3", activebackground="bisque3", relief="flat", font=("Courier New", 12), cursor="hand2", width=27, command=chng8)
btn8.place(x=10, y=360)

refresh = tkinter.Button(left_frame, text="Refresh", bg="bisque3", activebackground="bisque3", relief="flat", font=("Courier New", 12), cursor="hand2", width=27, command=ref)
refresh.place(x=10, y=410)

chng_pswd = tkinter.Button(left_frame, text="Change Password", bg="bisque3", activebackground="bisque3", relief="flat", font=("Courier New", 12), cursor="hand2", width=27, command=chg_pswd)
chng_pswd.place(x=10, y=460)

exit_btn = tkinter.Button(left_frame, text="Exit", bg="bisque3", activebackground="bisque3", relief="flat", font=("Courier New", 12), cursor="hand2", width=27, command=_exit)
exit_btn.place(x=10, y=510)



root.bind('1', lambda event: chng1())
root.bind('2', lambda event: chng2())
root.bind('3', lambda event: chng3())
root.bind('4', lambda event: chng4())
root.bind('5', lambda event: chng5())
root.bind('6', lambda event: chng6())
root.bind('7', lambda event: chng7())
root.bind('8', lambda event: chng8())
root.bind('<F5>', lambda event: ref())
root.bind('<Control-c>', lambda event: chg_pswd())
root.bind('<Escape>', lambda event: _exit())




