import tkinter
from hostel_mgmt import root, pswd_correct


def check_user():
    global pswd_correct
    username = user_input.get()
    password = pswd_input.get()
    if username == "admin" and password == pswd_correct:
        entry.destroy()
        root.deiconify()
    else:
        tkinter.Label(entry, text= "Incorrect username or password!", fg="red", bg="bisque3", font=("Courier New", 12)).place(x=90, y=100)
        entry.update()

def _exit():
    quit()

root.withdraw()

entry = tkinter.Toplevel(root)
entry.attributes("-topmost", "true")
entry.overrideredirect(True)
windowWidth = 500
windowHeight = 300
positionRight = int(root.winfo_screenwidth()/2 - windowWidth/2)
positionDown = int(root.winfo_screenheight()/2 - windowHeight/2)
entry.geometry(f"{windowWidth}x{windowHeight}+{positionRight}+{positionDown}")
entry.configure(bg="bisque3")

tkinter.Label(entry, text="Admin Login", font=('Courier New', 20, 'bold'), bg="bisque3").place(x=150, y=30)
user_input_label = tkinter.Label(entry, text="User ID :", font=('Courier New', 15), bg="bisque3")
user_input = tkinter.Entry(entry, width=15,  font=('Courier New', 15))
user_input.focus_set()
pswd_input_label = tkinter.Label(entry, text="Password :", font=('Courier New', 15), bg="bisque3")
pswd_input = tkinter.Entry(entry, show="*", width=15,  font=('Courier New', 15))
login_button = tkinter.Button(entry, text="Login", bg="bisque4", activebackground="bisque4", relief="flat", font=("Courier New", 12), cursor="hand2", command=check_user)
exit_button = tkinter.Button(entry, text="Exit", bg="bisque4", activebackground="bisque4", relief="flat", font=("Courier New", 12), cursor="hand2", command=_exit)


user_input_label.place(x=85, y=140)
user_input.place(x=230, y=140)
pswd_input_label.place(x=85, y=180)
pswd_input.place(x=230, y=180)
login_button.place(x=180, y=230)
exit_button.place(x=260, y=230)


entry.bind('<Return>', lambda event: check_user())
entry.bind('<Escape>', lambda event: _exit())
