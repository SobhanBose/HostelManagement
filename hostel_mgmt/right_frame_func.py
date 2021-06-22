from os import get_inheritable
import tkinter
from tkinter import ttk
from hostel_mgmt import root
from hostel_mgmt.left_frame_func import btn_list
from tkcalendar import DateEntry
from hostel_mgmt.models import *
from hostel_mgmt.support_queries import *


def btn_exit(btn_window):
        btn_window.destroy()


def ref():
    for widget in root.winfo_children():
        if isinstance(widget, tkinter.Toplevel):
            widget.destroy()
    for btn in btn_list:
        btn.place_forget()


def add_stu():
    def pass_stu():
        c_id = courseid_input.get()
        name = f"{firstname_input.get()} {lastname_input.get()}"
        dob = f"{dob_input.get()[6:]}-{dob_input.get()[3:5]}-{dob_input.get()[:2]}"
        gender = gender_input.get()
        blood_grp = bgrp_input.get()
        c_no = contact_input.get()
        r_id = roomid_input.get()
        is_veg = isveg_input.get()
        add = address_input.get('1.0', 'end-1c')
        g_name = guarname_input.get()
        g_c_no = guarcont_input.get()
        insert_stu(name, dob, c_id, g_name, gender, add, r_id, c_no, g_c_no, blood_grp, is_veg)
        sid = get_last_stu_id()
    
    def update_r_list(cat_input):
        cat = cat_input.get().lower()
        r_list = fetch_room_category(cat)
        roomid_input['values'] = r_list

    btn_window = tkinter.Toplevel(root)
    btn_window.attributes("-topmost", "true")
    btn_window.focus_set()
    btn_window.title("Add Student")
    windowWidth = 800
    windowHeight = int(root.winfo_screenheight())
    positionRight = int(root.winfo_screenwidth()/2 - windowWidth/2)
    positionDown = int(root.winfo_screenheight()/2 - windowHeight/2)
    btn_window.geometry(f"{windowWidth}x{windowHeight}+{positionRight}+{positionDown}")
    btn_window.configure(bg="bisque3")
    btn_window.grab_set()

    tkinter.Label(btn_window, text="Add Student Form", font=('Courier New', 20, 'bold'), bg="bisque3").place(x=260, y=30)
    
    # stuid_label = tkinter.Label(btn_window, text="Student ID :", font=('Courier New', 15), bg="bisque3")
    # stuid_input = tkinter.Entry(btn_window, width=10,  font=('Courier New', 15))

    c_list = show_courses()
    courseid_label = tkinter.Label(btn_window, text="Course ID :", font=('Courier New', 15), bg="bisque3")
    courseid_input = ttk.Combobox(btn_window, width=10, font=('Courier New', 15), values=c_list)
    
    firstname_label = tkinter.Label(btn_window, text="First Name :", font=('Courier New', 15), bg="bisque3")
    firstname_input = tkinter.Entry(btn_window, width=10,  font=('Courier New', 15))

    lastname_label = tkinter.Label(btn_window, text="Last Name :", font=('Courier New', 15), bg="bisque3")
    lastname_input = tkinter.Entry(btn_window, width=11,  font=('Courier New', 15))
    
    dob_label = tkinter.Label(btn_window, text="Birth Date:", font=('Courier New', 15), bg="bisque3")
    dob_input = DateEntry(btn_window, locale='en_US', date_pattern='dd/MM/yyyy', font=('Courier New', 15), width=9)

    gender_label = tkinter.Label(btn_window, text="Gender:", font=('Courier New', 15), bg="bisque3")
    gender_input = ttk.Combobox(btn_window, width = 10, font=('Courier New', 15), values=['Male', 'Female', 'Other'])
    
    bgrp_label = tkinter.Label(btn_window, text="Blood Group:", font=('Courier New', 15), bg="bisque3")
    bgrp_input = ttk.Combobox(btn_window, width=8, font=('Courier New', 15), values=['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-'])

    contact_label = tkinter.Label(btn_window, text="Contact:", font=('Courier New', 15), bg="bisque3")
    contact_input = tkinter.Entry(btn_window, width=11,  font=('Courier New', 15))
    
    roomid_label = tkinter.Label(btn_window, text="Room ID :", font=('Courier New', 15), bg="bisque3")
    roomid_input = ttk.Combobox(btn_window, width=8, font=('Courier New', 15))

    isveg_label = tkinter.Label(btn_window, text="Is Veg?", font=('Courier New', 15), bg="bisque3")
    isveg_input = ttk.Combobox(btn_window, width=10, font=('Courier New', 15), values=['Yes', 'No'])
    
    address_label = tkinter.Label(btn_window, text="Address :", font=('Courier New', 15), bg="bisque3")
    address_input = tkinter.Text(btn_window, width=35,  font=('Courier New', 15), height=3)
    
    tkinter.Label(btn_window, text="----------Guardian Details----------", font=('Courier New', 20), bg="bisque3").place(x=102, y=410)
    
    guarname_label = tkinter.Label(btn_window, text="Guardian Name:", font=('Courier New', 15), bg="bisque3")
    guarname_input = tkinter.Entry(btn_window, width=33,  font=('Courier New', 15))
    
    guarcont_label = tkinter.Label(btn_window, text="Contact:", font=('Courier New', 15), bg="bisque3")
    guarcont_input = tkinter.Entry(btn_window, width=11,  font=('Courier New', 15))
    
    con_button = tkinter.Button(btn_window, text="Rooms", bg="bisque4", activebackground="bisque3", relief="flat", font=("Courier New", 12), cursor="hand2", command=lambda: update_r_list(gender_input))
    add_button = tkinter.Button(btn_window, text="Add Student", bg="bisque4", activebackground="bisque3", relief="flat", font=("Courier New", 12), cursor="hand2", command=lambda: pass_stu())
    exit_button = tkinter.Button(btn_window, text="Exit", bg="bisque4", activebackground="bisque3", relief="flat", font=("Courier New", 12), cursor="hand2", command=lambda: btn_exit(btn_window))

    # stuid_label.place(x=100, y=110)
    # stuid_input.place(x=255, y=110)

    courseid_label.place(x=400, y=110)
    courseid_input.place(x=545, y=110)
    
    firstname_label.place(x=100, y=150)
    firstname_input.place(x=255, y=150)
    lastname_label.place(x=400, y=150)
    lastname_input.place(x=545, y=150)
    
    dob_label.place(x=100, y=190)
    dob_input.place(x=255, y=190)
    gender_label.place(x=400, y=190)
    gender_input.place(x=545, y=190)
    
    bgrp_label.place(x=100, y=230)
    bgrp_input.place(x=255, y=230)
    contact_label.place(x=400, y=230)
    contact_input.place(x=545, y=230)
    
    roomid_label.place(x=100, y=270)
    roomid_input.place(x=255, y=270)
    isveg_label.place(x=400, y=270)
    isveg_input.place(x=545, y=270)
    
    address_label.place(x=100, y=310)
    address_input.place(x=255, y=310)
    
    guarname_label.place(x=100, y=480)
    guarname_input.place(x=285, y=480)
    
    guarcont_label.place(x=100, y=520)
    guarcont_input.place(x=285, y=520)
    
    
    con_button.place(x=100, y=620)
    add_button.place(x=300, y=620)
    exit_button.place(x=440, y=620)


    btn_window.bind('<Escape>', lambda event: btn_window.destroy())
    btn_window.bind('<F5>', lambda event: ref())


def edit_stu():
    def pass_edit_stu(sid, firstname_input, lastname_input, g_name_input, add_input, c_no_input, g_c_no_input, is_veg_input):
        name = f"{firstname_input.get()} {lastname_input.get()}"
        g_name = g_name_input.get()
        add = add_input.get()
        c_no = c_no_input.get()
        g_c_no = g_c_no_input.get()
        is_veg = is_veg_input.get()
        change_stu_details(sid, name, g_name, add, c_no, g_c_no, is_veg)

    def con():
        sid = sid_input.get()
        sid_label.place_forget()
        sid_input.place_forget()
        con_button.place_forget()
        exit_button1.place_forget()

        windowWidth = 800
        windowHeight = int(root.winfo_screenheight())
        positionRight = int(root.winfo_screenwidth()/2 - windowWidth/2)
        positionDown = int(root.winfo_screenheight()/2 - windowHeight/2)
        btn_window.geometry(f"{windowWidth}x{windowHeight}+{positionRight}+{positionDown}")

        
        stuid_label = tkinter.Label(btn_window, text="Student ID:", font=('Courier New', 15), bg="bisque3")
        stuid_input = tkinter.Label(btn_window, text=sid, font=('Courier New', 15), bg="bisque3")
        courseid_label = tkinter.Label(btn_window, text="Course ID :", font=('Courier New', 15), bg="bisque3")
        courseid_input = tkinter.Label(btn_window, text="Course ID", font=('Courier New', 15), bg="bisque3")
        
        firstname_label = tkinter.Label(btn_window, text="First Name :", font=('Courier New', 15), bg="bisque3")
        firstname_input = tkinter.Entry(btn_window, width=10,  font=('Courier New', 15))
        lastname_label = tkinter.Label(btn_window, text="Last Name :", font=('Courier New', 15), bg="bisque3")
        lastname_input = tkinter.Entry(btn_window, width=11,  font=('Courier New', 15))
        
        dob_label = tkinter.Label(btn_window, text="Birth Date:", font=('Courier New', 15), bg="bisque3")
        dob_input = tkinter.Label(btn_window, text="dd/MM/yyyy", font=('Courier New', 15), bg="bisque3")
        gender_label = tkinter.Label(btn_window, text="Gender:", font=('Courier New', 15), bg="bisque3")
        gender_input = tkinter.Label(btn_window, text="Gender", font=('Courier New', 15), bg="bisque3")
        
        bgrp_label = tkinter.Label(btn_window, text="Blood Group:", font=('Courier New', 15), bg="bisque3")
        bgrp_input = tkinter.Label(btn_window, text="Blood Group", font=('Courier New', 15), bg="bisque3")
        contact_label = tkinter.Label(btn_window, text="Contact:", font=('Courier New', 15), bg="bisque3")
        contact_input = tkinter.Entry(btn_window, width=11,  font=('Courier New', 15))
        
        roomid_label = tkinter.Label(btn_window, text="Room ID :", font=('Courier New', 15), bg="bisque3")
        roomid_input = tkinter.Label(btn_window, text="Room ID", font=('Courier New', 15), bg="bisque3")
        isveg_label = tkinter.Label(btn_window, text="Is Veg?", font=('Courier New', 15), bg="bisque3")
        isveg_input = ttk.Combobox(btn_window, width=10, font=('Courier New', 15), values=['Yes', 'No'])
        
        address_label = tkinter.Label(btn_window, text="Address :", font=('Courier New', 15), bg="bisque3")
        address_input = tkinter.Text(btn_window, width=35,  font=('Courier New', 15), height=3)
        
        tkinter.Label(btn_window, text="----------Guardian Details----------", font=('Courier New', 20), bg="bisque3").place(x=102, y=410)
        
        guarname_label = tkinter.Label(btn_window, text="Guardian Name:", font=('Courier New', 15), bg="bisque3")
        guarname_input = tkinter.Entry(btn_window, width=33,  font=('Courier New', 15))
        
        guarcont_label = tkinter.Label(btn_window, text="Contact:", font=('Courier New', 15), bg="bisque3")
        guarcont_input = tkinter.Entry(btn_window, width=11,  font=('Courier New', 15))
        
        add_button = tkinter.Button(btn_window, text="Save Changes", bg="bisque4", activebackground="bisque3", relief="flat", font=("Courier New", 12), cursor="hand2", command=lambda: pass_edit_stu(sid, firstname_input, lastname_input, guarname_input, address_input, contact_input, guarcont_input, isveg_input))
        exit_button = tkinter.Button(btn_window, text="Exit", bg="bisque4", activebackground="bisque3", relief="flat", font=("Courier New", 12), cursor="hand2", command=lambda: btn_exit(btn_window))

        stuid_label.place(x=100, y=110)
        stuid_input.place(x=255, y=110)
        courseid_label.place(x=400, y=110)
        courseid_input.place(x=545, y=110)
        
        firstname_label.place(x=100, y=150)
        firstname_input.place(x=255, y=150)
        lastname_label.place(x=400, y=150)
        lastname_input.place(x=545, y=150)
        
        dob_label.place(x=100, y=190)
        dob_input.place(x=255, y=190)
        gender_label.place(x=400, y=190)
        gender_input.place(x=545, y=190)
        
        bgrp_label.place(x=100, y=230)
        bgrp_input.place(x=255, y=230)
        contact_label.place(x=400, y=230)
        contact_input.place(x=545, y=230)
        
        roomid_label.place(x=100, y=270)
        roomid_input.place(x=255, y=270)
        isveg_label.place(x=400, y=270)
        isveg_input.place(x=545, y=270)
        
        address_label.place(x=100, y=310)
        address_input.place(x=255, y=310)
        
        guarname_label.place(x=100, y=480)
        guarname_input.place(x=285, y=480)
        
        guarcont_label.place(x=100, y=520)
        guarcont_input.place(x=285, y=520)
        
        
        add_button.place(x=300, y=620)
        exit_button.place(x=440, y=620)


        btn_window.bind('<Escape>', lambda event: btn_window.destroy())
        btn_window.bind('<F5>', lambda event: ref())


    btn_window = tkinter.Toplevel(root)
    btn_window.attributes("-topmost", "true")
    btn_window.focus_set()
    btn_window.title("Edit Student")
    # btn_window.overrideredirect(True)
    windowWidth = 800
    windowHeight = int(root.winfo_screenheight())-400
    positionRight = int(root.winfo_screenwidth()/2 - windowWidth/2)
    positionDown = int(root.winfo_screenheight()/2 - windowHeight/2)
    btn_window.geometry(f"{windowWidth}x{windowHeight}+{positionRight}+{positionDown}")
    btn_window.configure(bg="bisque3")
    btn_window.grab_set()

    s_id_list = show_all_stu()
    tkinter.Label(btn_window, text="Edit Student Form", font=('Courier New', 20, 'bold'), bg="bisque3").place(x=260, y=30)
    sid_label = tkinter.Label(btn_window, text="Student ID :", font=('Courier New', 15), bg="bisque3")
    sid_input = ttk.Combobox(btn_window, width=10, font=('Courier New', 15), values=s_id_list)
    sid_label.place(x=250, y=165)
    sid_input.place(x=405, y=165)

    con_button = tkinter.Button(btn_window, text="Continue", bg="bisque4", activebackground="bisque3", relief="flat", font=("Courier New", 12), cursor="hand2", command= con)
    exit_button1 = tkinter.Button(btn_window, text="Exit", bg="bisque4", activebackground="bisque3", relief="flat", font=("Courier New", 12), cursor="hand2", command=lambda: btn_exit(btn_window))

    con_button.place(x=300, y=290)
    exit_button1.place(x=440, y=290)

    btn_window.bind('<Return>', lambda event: con())
    btn_window.bind('<Escape>', lambda event: btn_window.destroy())
    btn_window.bind('<F5>', lambda event: ref())


def change_rooms():
    def pass_change_rooms(stu_id, new_b_id_input, new_r_id_input):
        new_b_id = new_b_id_input.get()
        new_r_id = new_r_id_input.get()
        change_room(stu_id, new_b_id, new_r_id)

    def con():

        sid = sid_input.get()
        bid = new_blockid_input.get()
        sid_label.place_forget()
        sid_input.place_forget()
        new_blockid_input.place_forget()
        new_blockid_label.place_forget()

        stuid_label = tkinter.Label(btn_window, text="Student ID:", font=('Courier New', 15), bg="bisque3")
        stuid_input = tkinter.Label(btn_window, text=sid, font=('Courier New', 15), bg="bisque3")
        stuname_label = tkinter.Label(btn_window, text="Name:", font=('Courier New', 15), bg="bisque3")
        stuname_input = tkinter.Label(btn_window, text="Name", font=('Courier New', 15), bg="bisque3")
        
        roomid_label = tkinter.Label(btn_window, text="Room ID :", font=('Courier New', 15), bg="bisque3")
        roomid_input = tkinter.Label(btn_window, text="Room ID", font=('Courier New', 15), bg="bisque3")

        r_id_list = show_rooms_from_block(bid)
        new_roomid_label = tkinter.Label(btn_window, text="New Room ID :", font=('Courier New', 15), bg="bisque3")
        new_roomid_input = ttk.Combobox(btn_window, width=10, font=('Courier New', 15), values=r_id_list) 

        add_button = tkinter.Button(btn_window, text="Add Student", bg="bisque4", activebackground="bisque3", relief="flat", font=("Courier New", 12), cursor="hand2", command=lambda: pass_change_rooms(sid, new_blockid_input, new_roomid_input))
        exit_button = tkinter.Button(btn_window, text="Exit", bg="bisque4", activebackground="bisque3", relief="flat", font=("Courier New", 12), cursor="hand2", command=lambda: btn_exit(btn_window))

        stuid_label.place(x=100, y=110)
        stuid_input.place(x=255, y=110)
        stuname_label.place(x=400, y=110)
        stuname_input.place(x=545, y=110)   

        roomid_label.place(x=100, y=150)
        roomid_input.place(x=255, y=150)

        new_roomid_label.place(x=400, y=190)
        new_roomid_input.place(x=545, y=190)

        add_button.place(x=300, y=620)
        exit_button.place(x=440, y=620)

        btn_window.bind('<Escape>', lambda event: btn_window.destroy())
        btn_window.bind('<F5>', lambda event: ref())
        

    btn_window = tkinter.Toplevel(root)
    btn_window.attributes("-topmost", "true")
    btn_window.focus_set()
    btn_window.title("Change Room")
    # btn_window.overrideredirect(True)
    windowWidth = 800
    windowHeight = int(root.winfo_screenheight())-400
    positionRight = int(root.winfo_screenwidth()/2 - windowWidth/2)
    positionDown = int(root.winfo_screenheight()/2 - windowHeight/2)
    btn_window.geometry(f"{windowWidth}x{windowHeight}+{positionRight}+{positionDown}")
    btn_window.configure(bg="bisque3")
    btn_window.grab_set()

    s_id_list = show_all_stu()
    tkinter.Label(btn_window, text="Change Room Form", font=('Courier New', 20, 'bold'), bg="bisque3").place(x=260, y=30)
    sid_label = tkinter.Label(btn_window, text="Student ID :", font=('Courier New', 15), bg="bisque3")
    sid_input = ttk.Combobox(btn_window, width=10, font=('Courier New', 15), values=s_id_list)

    b_id_list = show_all_blocks()
    new_blockid_label = tkinter.Label(btn_window, text="New Block ID :", font=('Courier New', 15), bg="bisque3")
    new_blockid_input = ttk.Combobox(btn_window, width=8, font=('Courier New', 15), values=b_id_list)

    sid_label.place(x=250, y=165)
    sid_input.place(x=405, y=165)

    new_blockid_label.place(x=100, y=200)
    new_blockid_input.place(x=255, y=200)

    con_button = tkinter.Button(btn_window, text="Continue", bg="bisque4", activebackground="bisque3", relief="flat", font=("Courier New", 12), cursor="hand2", command= con)
    exit_button = tkinter.Button(btn_window, text="Exit", bg="bisque4", activebackground="bisque3", relief="flat", font=("Courier New", 12), cursor="hand2", command=lambda: btn_exit(btn_window))

    con_button.place(x=300, y=290)
    exit_button.place(x=440, y=290)

    btn_window.bind('<Return>', lambda event: con())
    btn_window.bind('<Escape>', lambda event: btn_window.destroy())
    btn_window.bind('<F5>', lambda event: ref())



def add_block():

    def pass_block():
        id = blockid_input.get()
        type = blocktype_input.get()
        w_id = wardenid_input.get()
        gender = gender_input.get()
        mess_id = messid_input.get()
        num_single = int(singroom_input.get())
        num_double = int(doubroom_input.get())
        num_tripple = int(triproom_input.get())
        num_rooms = num_single + num_double + num_tripple
        insert_block(id, type, w_id, gender, mess_id, num_rooms, num_single, num_double, num_tripple)

    btn_window = tkinter.Toplevel(root)
    btn_window.attributes("-topmost", "true")
    btn_window.focus_set()
    btn_window.title("Add Block")
    # btn_window.overrideredirect(True)
    windowWidth = 800
    windowHeight = int(root.winfo_screenheight())-200
    positionRight = int(root.winfo_screenwidth()/2 - windowWidth/2)
    positionDown = int(root.winfo_screenheight()/2 - windowHeight/2)
    btn_window.geometry(f"{windowWidth}x{windowHeight}+{positionRight}+{positionDown}")
    btn_window.configure(bg="bisque3")
    btn_window.grab_set()

    tkinter.Label(btn_window, text="Add Block Form", font=('Courier New', 20, 'bold'), bg="bisque3").place(x=275, y=30)
    
    blockid_label = tkinter.Label(btn_window, text="Block ID :", font=('Courier New', 15), bg="bisque3")
    blockid_input = tkinter.Entry(btn_window, width=10,  font=('Courier New', 15))

    blocktype_label = tkinter.Label(btn_window, text="Block Type:", font=('Courier New', 15), bg="bisque3")
    blocktype_input = ttk.Combobox(btn_window, width=10, font=('Courier New', 15), values=['AC', 'NAC'])
    
    wardenid_label = tkinter.Label(btn_window, text="Warden ID:", font=('Courier New', 15), bg="bisque3")
    wardenid_input = ttk.Combobox(btn_window, width=8, font=('Courier New', 15), values=['S01'])

    gender_label = tkinter.Label(btn_window, text="Gender:", font=('Courier New', 15), bg="bisque3")
    gender_input = ttk.Combobox(btn_window, width = 10, font=('Courier New', 15), values=['Male', 'Female', 'Other'])

    mess_id = show_all_mess()
    messid_label = tkinter.Label(btn_window, text="Mess ID:", font=('Courier New', 15), bg="bisque3")
    messid_input = ttk.Combobox(btn_window, width=8, font=('Courier New', 15), values=mess_id)

    tkinter.Label(btn_window, text="----------Room Details----------", font=('Courier New', 20), bg="bisque3").place(x=135, y=255)
    
    singroom_label = tkinter.Label(btn_window, text="Single Sharing:", font=('Courier New', 15), bg="bisque3")
    singroom_input = tkinter.Entry(btn_window, width=3,  font=('Courier New', 15))
    
    doubroom_label = tkinter.Label(btn_window, text="Double Sharing:", font=('Courier New', 15), bg="bisque3")
    doubroom_input = tkinter.Entry(btn_window, width=3,  font=('Courier New', 15))

    triproom_label = tkinter.Label(btn_window, text="Triple Sharing:", font=('Courier New', 15), bg="bisque3")
    triproom_input = tkinter.Entry(btn_window, width=3,  font=('Courier New', 15))
    
    add_button = tkinter.Button(btn_window, text="Add Block", bg="bisque4", activebackground="bisque3", relief="flat", font=("Courier New", 12), cursor="hand2", command=lambda: pass_block())
    exit_button = tkinter.Button(btn_window, text="Exit", bg="bisque4", activebackground="bisque3", relief="flat", font=("Courier New", 12), cursor="hand2", command=lambda: btn_exit(btn_window))

    blockid_label.place(x=100, y=110)
    blockid_input.place(x=255, y=110)
    blocktype_label.place(x=400, y=110)
    blocktype_input.place(x=545, y=110)
    
    wardenid_label.place(x=100, y=150)
    wardenid_input.place(x=255, y=150)

    gender_label.place(x=400, y=150)
    gender_input.place(x=545, y=150)
    
    messid_label.place(x=100, y=190)
    messid_input.place(x=255, y=190)

    singroom_label.place(x=100, y=330)
    singroom_input.place(x=300, y=330)
    
    doubroom_label.place(x=450, y=330)
    doubroom_input.place(x=650, y=330)

    triproom_label.place(x=275, y=370)
    triproom_input.place(x=475, y=370)
    
    
    add_button.place(x=300, y=450)
    exit_button.place(x=440, y=450)


    btn_window.bind('<Escape>', lambda event: btn_window.destroy())
    btn_window.bind('<F5>', lambda event: ref())

def edit_block():
    def pass_edit_block(id, type, size_input, num_rooms_input):
        size = size_input.get()
        num_of_rooms = num_rooms_input.get()
        extend_block(id, type, size, num_of_rooms)

    def con():
        b_id = b_id_input.get()
        b_id_label.place_forget()
        b_id_input.place_forget()
        con_button.place_forget()
        exit_button1.place_forget()

        block_type = get_block_type(b_id)
        blockid_label = tkinter.Label(btn_window, text="Block ID :", font=('Courier New', 15), bg="bisque3")
        blockid_input = tkinter.Label(btn_window, text=b_id, font=('Courier New', 15), bg="bisque3")

        blocktype_label = tkinter.Label(btn_window, text="Block Type:", font=('Courier New', 15), bg="bisque3")
        blocktype_input = tkinter.Label(btn_window, text=block_type, font=('Courier New', 15), bg="bisque3")

        wardenid_label = tkinter.Label(btn_window, text="Warden ID:", font=('Courier New', 15), bg="bisque3")
        wardenid_input = tkinter.Label(btn_window, text="Warden ID", font=('Courier New', 15), bg="bisque3")

        gender_label = tkinter.Label(btn_window, text="Gender:", font=('Courier New', 15), bg="bisque3")
        gender_input = tkinter.Label(btn_window, text="Gender", font=('Courier New', 15), bg="bisque3")
        
        size_label = tkinter.Label(btn_window, text="Bed sharing:", font=('Courier New', 15), bg="bisque3")
        size_input = ttk.Combobox(btn_window, width=8, font=('Courier New', 15), values=['Single', 'Double', 'Triple'])
    
        num_room_label = tkinter.Label(btn_window, text="No. of rooms:", font=('Courier New', 15), bg="bisque3")
        num_room_input = tkinter.Entry(btn_window, width=3,  font=('Courier New', 15))

        add_button = tkinter.Button(btn_window, text="Save Changes", bg="bisque4", activebackground="bisque3", relief="flat", font=("Courier New", 12), cursor="hand2", command=lambda: pass_edit_block(b_id, block_type, size_input, num_room_input))
        exit_button = tkinter.Button(btn_window, text="Exit", bg="bisque4", activebackground="bisque3", relief="flat", font=("Courier New", 12), cursor="hand2", command=lambda: btn_exit(btn_window))

        blockid_label.place(x=100, y=110)
        blockid_input.place(x=255, y=110)
        blocktype_label.place(x=400, y=110)
        blocktype_input.place(x=545, y=110)

        wardenid_label.place(x=100, y=150)
        wardenid_input.place(x=235, y=150)

        gender_label.place(x=400, y=150)
        gender_input.place(x=545, y=150)

        size_label.place(x=100, y=190)
        size_input.place(x=265, y=190)

        num_room_label.place(x=400, y=190)
        num_room_input.place(x=565, y=190)

        add_button.place(x=280, y=290)
        exit_button.place(x=440, y=290)
    
        btn_window.bind('<Escape>', lambda event: btn_window.destroy())
        btn_window.bind('<F5>', lambda event: ref())


    btn_window = tkinter.Toplevel(root)
    btn_window.attributes("-topmost", "true")
    btn_window.focus_set()
    btn_window.title("Edit Block")
    windowWidth = 800
    windowHeight = int(root.winfo_screenheight())-400
    positionRight = int(root.winfo_screenwidth()/2 - windowWidth/2)
    positionDown = int(root.winfo_screenheight()/2 - windowHeight/2)
    btn_window.geometry(f"{windowWidth}x{windowHeight}+{positionRight}+{positionDown}")
    btn_window.configure(bg="bisque3")
    btn_window.grab_set()

    b_id_list = show_all_blocks()
    tkinter.Label(btn_window, text="Edit Block Form", font=('Courier New', 20, 'bold'), bg="bisque3").place(x=270, y=30)
    b_id_label = tkinter.Label(btn_window, text="Block ID :", font=('Courier New', 15), bg="bisque3")
    b_id_input = ttk.Combobox(btn_window, width=10, font=('Courier New', 15), values=b_id_list)
    b_id_label.place(x=250, y=165)
    b_id_input.place(x=405, y=165)

    con_button = tkinter.Button(btn_window, text="Continue", bg="bisque4", activebackground="bisque3", relief="flat", font=("Courier New", 12), cursor="hand2", command= con)
    exit_button1 = tkinter.Button(btn_window, text="Exit", bg="bisque4", activebackground="bisque3", relief="flat", font=("Courier New", 12), cursor="hand2", command=lambda: btn_exit(btn_window))

    con_button.place(x=300, y=290)
    exit_button1.place(x=440, y=290)

    btn_window.bind('<Escape>', lambda event: btn_window.destroy())
    btn_window.bind('<Return>', lambda event: con())
    btn_window.bind('<F5>', lambda event: ref())

def changewarden():
    def pass_change_warden(b_id, w_id_input):
        w_id = w_id_input.get()
        change_warden(b_id, w_id)

    def con():
        b_id = b_id_input.get()
        b_id_label.place_forget()
        b_id_input.place_forget()
        con_button.place_forget()
        exit_button1.place_forget()

        wid = get_w_id(b_id)
        wardenid_label = tkinter.Label(btn_window, text="Warden ID :", font=('Courier New', 15), bg="bisque3")
        wardenid_input = tkinter.Label(btn_window, text=wid, font=('Courier New', 15), bg="bisque3")

        newwarden_label = tkinter.Label(btn_window, text="New Warden ID:", font=('Courier New', 15), bg="bisque3")
        newwarden_input = ttk.Combobox(btn_window, width=8, font=('Courier New', 15))

        wardenid_label.place(x=100, y=110)
        wardenid_input.place(x=255, y=110)
        newwarden_label.place(x=360, y=110)
        newwarden_input.place(x=545, y=110)

        add_button = tkinter.Button(btn_window, text="Save Changes", bg="bisque4", activebackground="bisque3", relief="flat", font=("Courier New", 12), cursor="hand2", command=lambda: pass_change_warden(b_id, newwarden_input))
        exit_button = tkinter.Button(btn_window, text="Exit", bg="bisque4", activebackground="bisque3", relief="flat", font=("Courier New", 12), cursor="hand2", command=lambda: btn_exit(btn_window))

        add_button.place(x=280, y=290)
        exit_button.place(x=440, y=290)

        btn_window.bind('<Escape>', lambda event: btn_window.destroy())
        btn_window.bind('<F5>', lambda event: ref())

    btn_window = tkinter.Toplevel(root)
    btn_window.attributes("-topmost", "true")
    btn_window.focus_set()
    btn_window.title("Change Warden")
    # btn_window.overrideredirect(True)
    windowWidth = 800
    windowHeight = int(root.winfo_screenheight())-400
    positionRight = int(root.winfo_screenwidth()/2 - windowWidth/2)
    positionDown = int(root.winfo_screenheight()/2 - windowHeight/2)
    btn_window.geometry(f"{windowWidth}x{windowHeight}+{positionRight}+{positionDown}")
    btn_window.configure(bg="bisque3")
    btn_window.grab_set()

    b_id_list = show_all_blocks()
    tkinter.Label(btn_window, text="Change Warden Form", font=('Courier New', 20, 'bold'), bg="bisque3").place(x=250, y=30)
    b_id_label = tkinter.Label(btn_window, text="Block ID :", font=('Courier New', 15), bg="bisque3")
    b_id_input = ttk.Combobox(btn_window, width=10, font=('Courier New', 15), values=b_id_list)
    b_id_label.place(x=250, y=165)
    b_id_input.place(x=405, y=165)

    con_button = tkinter.Button(btn_window, text="Continue", bg="bisque4", activebackground="bisque3", relief="flat", font=("Courier New", 12), cursor="hand2", command= con)
    exit_button1 = tkinter.Button(btn_window, text="Exit", bg="bisque4", activebackground="bisque3", relief="flat", font=("Courier New", 12), cursor="hand2", command=lambda: btn_exit(btn_window))

    con_button.place(x=300, y=290)
    exit_button1.place(x=440, y=290)
    
    btn_window.bind('<Escape>', lambda event: btn_window.destroy())
    btn_window.bind('<Return>', lambda event: con())
    btn_window.bind('<F5>', lambda event: ref())

def add_mess():
    def pass_mess():
        id = messid_input.get()
        insert_mess(id)

    btn_window = tkinter.Toplevel(root)
    btn_window.attributes("-topmost", "true")
    btn_window.focus_set()
    btn_window.title("Add Mess")
    # btn_window.overrideredirect(True)
    windowWidth = 800
    windowHeight = int(root.winfo_screenheight())-400
    positionRight = int(root.winfo_screenwidth()/2 - windowWidth/2)
    positionDown = int(root.winfo_screenheight()/2 - windowHeight/2)
    btn_window.geometry(f"{windowWidth}x{windowHeight}+{positionRight}+{positionDown}")
    btn_window.configure(bg="bisque3")
    btn_window.grab_set()

    tkinter.Label(btn_window, text="Add Mess Form", font=('Courier New', 20, 'bold'), bg="bisque3").place(x=280, y=30)
    messid_label = tkinter.Label(btn_window, text="Mess ID :", font=('Courier New', 15), bg="bisque3")
    messid_input = tkinter.Entry(btn_window, width=10, font=('Courier New', 15))
    messid_label.place(x=250, y=165)
    messid_input.place(x=405, y=165)

    add_button = tkinter.Button(btn_window, text="Add Mess", bg="bisque4", activebackground="bisque3", relief="flat", font=("Courier New", 12), cursor="hand2", command=lambda: pass_mess())
    exit_button = tkinter.Button(btn_window, text="Exit", bg="bisque4", activebackground="bisque3", relief="flat", font=("Courier New", 12), cursor="hand2", command=lambda: btn_exit(btn_window))

    add_button.place(x=280, y=290)
    exit_button.place(x=440, y=290)
    
    btn_window.bind('<Escape>', lambda event: btn_window.destroy())
    btn_window.bind('<F5>', lambda event: ref())

def add_staff():
    def pass_add_staff():
        id = staffid_input.get()
        # b_id = blockid_input.get()
        name = name_input.get()
        c_no = contact_input.get()
        dob = f"{dob_input.get()[6:]}-{dob_input.get()[3:5]}-{dob_input.get()[:2]}"
        gender = gender_input.get()
        insert_staff(id, name, c_no, dob, gender)

    btn_window = tkinter.Toplevel(root)
    btn_window.attributes("-topmost", "true")
    btn_window.focus_set()
    btn_window.title("Add Staff")
    # btn_window.overrideredirect(True)
    windowWidth = 800
    windowHeight = int(root.winfo_screenheight())-400
    positionRight = int(root.winfo_screenwidth()/2 - windowWidth/2)
    positionDown = int(root.winfo_screenheight()/2 - windowHeight/2)
    btn_window.geometry(f"{windowWidth}x{windowHeight}+{positionRight}+{positionDown}")
    btn_window.configure(bg="bisque3")
    btn_window.grab_set()

    tkinter.Label(btn_window, text="Add Staff Form", font=('Courier New', 20, 'bold'), bg="bisque3").place(x=275, y=30)

    staffid_label = tkinter.Label(btn_window, text="Staff ID :", font=('Courier New', 15), bg="bisque3")
    staffid_input = tkinter.Entry(btn_window, width=10,  font=('Courier New', 15))
    # blockid_label = tkinter.Label(btn_window, text="Block ID:", font=('Courier New', 15), bg="bisque3")
    # blockid_input = ttk.Combobox(btn_window, width=10, font=('Courier New', 15))

    name_label = tkinter.Label(btn_window, text="Name:", font=('Courier New', 15), bg="bisque3")
    name_input = tkinter.Entry(btn_window, font=('Courier New', 15), width=10)

    contact_label = tkinter.Label(btn_window, text="Contact:", font=('Courier New', 15), bg="bisque3")
    contact_input = tkinter.Entry(btn_window, font=('Courier New', 15), width=10)

    dob_label = tkinter.Label(btn_window, text="Birth Date:", font=('Courier New', 15), bg="bisque3")
    dob_input = DateEntry(btn_window, locale='en_US', date_pattern='dd/MM/yyyy', font=('Courier New', 15), width=9)
    gender_label = tkinter.Label(btn_window, text="Gender:", font=('Courier New', 15), bg="bisque3")
    gender_input = ttk.Combobox(btn_window, width = 10, font=('Courier New', 15), values=['Male', 'Female', 'Other'])

    add_button = tkinter.Button(btn_window, text="Add Staff", bg="bisque4", activebackground="bisque3", relief="flat", font=("Courier New", 12), cursor="hand2", command=lambda: pass_add_staff())
    exit_button = tkinter.Button(btn_window, text="Exit", bg="bisque4", activebackground="bisque3", relief="flat", font=("Courier New", 12), cursor="hand2", command=lambda: btn_exit(btn_window))

    staffid_label.place(x=100, y=110)
    staffid_input.place(x=255, y=110)
    # blockid_label.place(x=400, y=110)
    # blockid_input.place(x=545, y=110)
    
    name_label.place(x=100, y=150)
    name_input.place(x=255, y=150)
    contact_label.place(x=400, y=150)
    contact_input.place(x=545, y=150)
    
    dob_label.place(x=100, y=190)
    dob_input.place(x=255, y=190)
    gender_label.place(x=400, y=190)
    gender_input.place(x=545, y=190)

    add_button.place(x=280, y=290)
    exit_button.place(x=440, y=290)

    btn_window.bind('<Escape>', lambda event: btn_window.destroy())
    btn_window.bind('<F5>', lambda event: ref())

def edit_staff():
    def pass_edit_staff(sid, name_input, contact_input):
        name = name_input.get()
        c_no = contact_input.get()
        change_staff_details(sid, name, c_no)

    def con():
        sid = sid_input.get()
        sid_label.place_forget()
        sid_input.place_forget()
        con_button.place_forget()
        exit_button1.place_forget()

        staffid_label = tkinter.Label(btn_window, text="Staff ID :", font=('Courier New', 15), bg="bisque3")
        staffid_input = tkinter.Label(btn_window, text=sid, font=('Courier New', 15), bg="bisque3")
        # blockid_label = tkinter.Label(btn_window, text="Block ID:", font=('Courier New', 15), bg="bisque3")
        # blockid_input = tkinter.Label(btn_window, text="Block ID", font=('Courier New', 15), bg="bisque3")

        name_label = tkinter.Label(btn_window, text="Name:", font=('Courier New', 15), bg="bisque3")
        name_input = tkinter.Entry(btn_window, font=('Courier New', 15), width=10)

        contact_label = tkinter.Label(btn_window, text="Contact:", font=('Courier New', 15), bg="bisque3")
        contact_input = tkinter.Entry(btn_window, font=('Courier New', 15), width=10)

        dob_label = tkinter.Label(btn_window, text="Birth Date:", font=('Courier New', 15), bg="bisque3")
        dob_input = tkinter.Label(btn_window, text="dd/MM/yyyy", font=('Courier New', 15), bg="bisque3")
        gender_label = tkinter.Label(btn_window, text="Gender:", font=('Courier New', 15), bg="bisque3")
        gender_input = tkinter.Label(btn_window, text="Gender", font=('Courier New', 15), bg="bisque3")

        add_button = tkinter.Button(btn_window, text="Save Changes", bg="bisque4", activebackground="bisque3", relief="flat", font=("Courier New", 12), cursor="hand2", command=lambda: pass_edit_staff(sid, name_input, contact_input))
        exit_button = tkinter.Button(btn_window, text="Exit", bg="bisque4", activebackground="bisque3", relief="flat", font=("Courier New", 12), cursor="hand2", command=lambda: btn_exit(btn_window))

        staffid_label.place(x=100, y=110)
        staffid_input.place(x=255, y=110)
        # blockid_label.place(x=400, y=110)
        # blockid_input.place(x=545, y=110)
        
        name_label.place(x=100, y=150)
        name_input.place(x=255, y=150)
        contact_label.place(x=400, y=150)
        contact_input.place(x=545, y=150)
        
        dob_label.place(x=100, y=190)
        dob_input.place(x=255, y=190)
        gender_label.place(x=400, y=190)
        gender_input.place(x=545, y=190)

        add_button.place(x=280, y=290)
        exit_button.place(x=440, y=290)

        btn_window.bind('<Escape>', lambda event: btn_window.destroy())
        btn_window.bind('<F5>', lambda event: ref())
        
    btn_window = tkinter.Toplevel(root)
    btn_window.attributes("-topmost", "true")
    btn_window.focus_set()
    btn_window.title("Edit Staff")
    windowWidth = 800
    windowHeight = int(root.winfo_screenheight())-400
    positionRight = int(root.winfo_screenwidth()/2 - windowWidth/2)
    positionDown = int(root.winfo_screenheight()/2 - windowHeight/2)
    btn_window.geometry(f"{windowWidth}x{windowHeight}+{positionRight}+{positionDown}")
    btn_window.configure(bg="bisque3")
    btn_window.grab_set()

    s_id_list = show_all_staff()
    tkinter.Label(btn_window, text="Edit Staff Form", font=('Courier New', 20, 'bold'), bg="bisque3").place(x=260, y=30)
    sid_label = tkinter.Label(btn_window, text="Staff ID :", font=('Courier New', 15), bg="bisque3")
    sid_input = ttk.Combobox(btn_window, width=10, font=('Courier New', 15), values=s_id_list)
    sid_label.place(x=250, y=165)
    sid_input.place(x=405, y=165)

    con_button = tkinter.Button(btn_window, text="Continue", bg="bisque4", activebackground="bisque3", relief="flat", font=("Courier New", 12), cursor="hand2", command= con)
    exit_button1 = tkinter.Button(btn_window, text="Exit", bg="bisque4", activebackground="bisque3", relief="flat", font=("Courier New", 12), cursor="hand2", command=lambda: btn_exit(btn_window))

    con_button.place(x=300, y=290)
    exit_button1.place(x=440, y=290)

    btn_window.bind('<Escape>', lambda event: btn_window.destroy())
    btn_window.bind('<Return>', lambda event: con())
    btn_window.bind('<F5>', lambda event: ref())


# def chng_assigned_block():
#     def pass_change_block(s_id, new_b_id_input):
#         new_b_id = new_b_id_input.get()
#         change_assigned_block(s_id, new_b_id)

#     def con():
#         sid = sid_input.get()
#         sid_label.place_forget()
#         sid_input.place_forget()
#         con_button.place_forget()
#         exit_button1.place_forget()

#         staffid_label = tkinter.Label(btn_window, text="Staff ID :", font=('Courier New', 15), bg="bisque3")
#         staffid_input = tkinter.Label(btn_window, text=sid, font=('Courier New', 15), bg="bisque3")
#         name_label = tkinter.Label(btn_window, text="Name:", font=('Courier New', 15), bg="bisque3")
#         name_input = tkinter.Label(btn_window, text="Name", font=('Courier New', 15), bg="bisque3")

#         dob_label = tkinter.Label(btn_window, text="Birth Date:", font=('Courier New', 15), bg="bisque3")
#         dob_input = tkinter.Label(btn_window, text="dd/MM/yyyy", font=('Courier New', 15), bg="bisque3")
#         gender_label = tkinter.Label(btn_window, text="Gender:", font=('Courier New', 15), bg="bisque3")
#         gender_input = tkinter.Label(btn_window, text="Gender", font=('Courier New', 15), bg="bisque3")

#         old_blockid_label = tkinter.Label(btn_window, text="Old Block:", font=('Courier New', 15), bg="bisque3")
#         old_blockid_input = tkinter.Label(btn_window, text="Block ID", font=('Courier New', 15), bg="bisque3")

#         new_blockid_label = tkinter.Label(btn_window, text="New Block:", font=('Courier New', 15), bg="bisque3")
#         new_blockid_input = ttk.Combobox(btn_window, width=10, font=('Courier New', 15), values=['ABC'])

#         add_button = tkinter.Button(btn_window, text="Save Changes", bg="bisque4", activebackground="bisque3", relief="flat", font=("Courier New", 12), cursor="hand2", command=lambda: pass_change_block(sid, new_blockid_input))
#         exit_button = tkinter.Button(btn_window, text="Exit", bg="bisque4", activebackground="bisque3", relief="flat", font=("Courier New", 12), cursor="hand2", command=lambda: btn_exit(btn_window))

#         staffid_label.place(x=100, y=110)
#         staffid_input.place(x=255, y=110)
#         name_label.place(x=400, y=110)
#         name_input.place(x=545, y=110)
        
#         dob_label.place(x=100, y=150)
#         dob_input.place(x=255, y=150)
#         gender_label.place(x=400, y=150)
#         gender_input.place(x=545, y=150)
        
#         old_blockid_label.place(x=100, y=190)
#         old_blockid_input.place(x=255, y=190)
#         new_blockid_label.place(x=400, y=190)
#         new_blockid_input.place(x=545, y=190)

#         add_button.place(x=280, y=290)
#         exit_button.place(x=440, y=290)

#         btn_window.bind('<Escape>', lambda event: btn_window.destroy())
#         btn_window.bind('<F5>', lambda event: ref())


#     btn_window = tkinter.Toplevel(root)
#     btn_window.attributes("-topmost", "true")
#     btn_window.focus_set()
#     btn_window.title("Change Assigned Block")
#     windowWidth = 800
#     windowHeight = int(root.winfo_screenheight())-400
#     positionRight = int(root.winfo_screenwidth()/2 - windowWidth/2)
#     positionDown = int(root.winfo_screenheight()/2 - windowHeight/2)
#     btn_window.geometry(f"{windowWidth}x{windowHeight}+{positionRight}+{positionDown}")
#     btn_window.configure(bg="bisque3")
#     btn_window.grab_set()

#     tkinter.Label(btn_window, text="Change Assigned Block", font=('Courier New', 20, 'bold'), bg="bisque3").place(x=240, y=30)
#     sid_label = tkinter.Label(btn_window, text="Staff ID :", font=('Courier New', 15), bg="bisque3")
#     sid_input = ttk.Combobox(btn_window, width=10, font=('Courier New', 15), values=['ABC'])
#     sid_label.place(x=250, y=165)
#     sid_input.place(x=405, y=165)

#     con_button = tkinter.Button(btn_window, text="Continue", bg="bisque4", activebackground="bisque3", relief="flat", font=("Courier New", 12), cursor="hand2", command= con)
#     exit_button1 = tkinter.Button(btn_window, text="Exit", bg="bisque4", activebackground="bisque3", relief="flat", font=("Courier New", 12), cursor="hand2", command=lambda: btn_exit(btn_window))

#     con_button.place(x=300, y=290)
#     exit_button1.place(x=440, y=290)

#     btn_window.bind('<Escape>', lambda event: btn_window.destroy())
#     btn_window.bind('<Return>', lambda event: con())
#     btn_window.bind('<F5>', lambda event: ref())

def add_course():
    def pass_course():
        c_id = courseid_input.get()
        c_name = course_input.get
        sems = sems_input.get()
        insert_course(c_id, c_name, sems)

    btn_window = tkinter.Toplevel(root)
    btn_window.attributes("-topmost", "true")
    btn_window.focus_set()
    btn_window.title("Add Course")
    # btn_window.overrideredirect(True)
    windowWidth = 800
    windowHeight = int(root.winfo_screenheight())-450
    positionRight = int(root.winfo_screenwidth()/2 - windowWidth/2)
    positionDown = int(root.winfo_screenheight()/2 - windowHeight/2)
    btn_window.geometry(f"{windowWidth}x{windowHeight}+{positionRight}+{positionDown}")
    btn_window.configure(bg="bisque3")
    btn_window.grab_set()

    tkinter.Label(btn_window, text="Add Course", font=('Courier New', 20, 'bold'), bg="bisque3").place(x=320, y=30)
    
    courseid_label = tkinter.Label(btn_window, text="Course ID :", font=('Courier New', 15), bg="bisque3")
    courseid_input = tkinter.Entry(btn_window, width=10,  font=('Courier New', 15))
    course_label = tkinter.Label(btn_window, text="Course Name:", font=('Courier New', 15), bg="bisque3")
    course_input = ttk.Entry(btn_window, width=10, font=('Courier New', 15))
    
    sems_label = tkinter.Label(btn_window, text="Semesters:", font=('Courier New', 15), bg="bisque3")
    sems_input = ttk.Combobox(btn_window, width=8, font=('Courier New', 15), values=[8])
    
    add_button = tkinter.Button(btn_window, text="Add Course", bg="bisque4", activebackground="bisque3", relief="flat", font=("Courier New", 12), cursor="hand2", command=lambda: pass_course())
    exit_button = tkinter.Button(btn_window, text="Exit", bg="bisque4", activebackground="bisque3", relief="flat", font=("Courier New", 12), cursor="hand2", command=lambda: btn_exit(btn_window))

    courseid_label.place(x=100, y=110)
    courseid_input.place(x=255, y=110)
    course_label.place(x=400, y=110)
    course_input.place(x=555, y=110)
    
    sems_label.place(x=100, y=150)
    sems_input.place(x=255, y=150)

    add_button.place(x=300, y=230)
    exit_button.place(x=440, y=230)


    btn_window.bind('<Escape>', lambda event: btn_window.destroy())
    btn_window.bind('<F5>', lambda event: ref())


def pay_fees():
    def pass_pay_fees(s_id):
        transaction(s_id)

    def con():
        sid = sid_input.get()
        sid_label.place_forget()
        sid_input.place_forget()
        con_button.place_forget()
        exit_button1.place_forget()

        studid_label = tkinter.Label(btn_window, text="Student ID :", font=('Courier New', 15), bg="bisque3")
        studid_input = tkinter.Label(btn_window, text=sid, font=('Courier New', 15), bg="bisque3")

        name = get_stu_name(sid)
        sname_label = tkinter.Label(btn_window, text="Name:", font=('Courier New', 15), bg="bisque3")
        sname_input = tkinter.Label(btn_window, text=f"{name}", font=('Courier New', 15), bg="bisque3")

        room_charges, mess_charges, add_charges, total_charge = get_fee_details(sid)

        roomcharges_label = tkinter.Label(btn_window, text="Bed Charges:", font=('Courier New', 15), bg="bisque3")
        roomcharges_input = tkinter.Label(btn_window, text=f"₹ {room_charges}", font=('Courier New', 15), bg="bisque3")

        messcharges_label = tkinter.Label(btn_window, text="Mess Charges:", font=('Courier New', 15), bg="bisque3")
        messcharges_input = tkinter.Label(btn_window, text=f"₹ {mess_charges}", font=('Courier New', 15), bg="bisque3")
        
        additional_label = tkinter.Label(btn_window, text="Addn. Charges:", font=('Courier New', 15), bg="bisque3")
        additional_input = tkinter.Label(btn_window, text=f"₹ {add_charges}", font=('Courier New', 15), bg="bisque3")
    
        total_label = tkinter.Label(btn_window, text="Total:", font=('Courier New', 15), bg="bisque3")
        total_input = tkinter.Label(btn_window, text=f"₹ {total_charge}", font=('Courier New', 15), bg="bisque3")

        add_button = tkinter.Button(btn_window, text="Pay Fees", bg="bisque4", activebackground="bisque3", relief="flat", font=("Courier New", 12), cursor="hand2", command=lambda: pass_pay_fees(sid))
        exit_button = tkinter.Button(btn_window, text="Exit", bg="bisque4", activebackground="bisque3", relief="flat", font=("Courier New", 12), cursor="hand2", command=lambda: btn_exit(btn_window))

        studid_label.place(x=100, y=110)
        studid_input.place(x=255, y=110)
        sname_label.place(x=400, y=110)
        sname_input.place(x=545, y=110)

        roomcharges_label.place(x=100, y=150)
        roomcharges_input.place(x=270, y=150)

        messcharges_label.place(x=400, y=150)
        messcharges_input.place(x=565, y=150)

        additional_label.place(x=100, y=190)
        additional_input.place(x=270, y=190)

        total_label.place(x=400, y=190)
        total_input.place(x=565, y=190)

        add_button.place(x=280, y=290)
        exit_button.place(x=440, y=290)
    

        btn_window.bind('<Escape>', lambda event: btn_window.destroy())
        btn_window.bind('<F5>', lambda event: ref())

        # add_button.bind("<Enter>", lambda event: on_enter(add_button))
        # add_button.bind("<Leave>", lambda event: on_leave(add_button))
        # exit_button.bind("<Enter>", lambda event: on_enter(exit_button))
        # exit_button.bind("<Leave>", lambda event: on_leave(exit_button))


    btn_window = tkinter.Toplevel(root)
    btn_window.attributes("-topmost", "true")
    btn_window.focus_set()
    btn_window.title("Pay Fees")
    # btn_window.overrideredirect(True)
    windowWidth = 800
    windowHeight = int(root.winfo_screenheight())-400
    positionRight = int(root.winfo_screenwidth()/2 - windowWidth/2)
    positionDown = int(root.winfo_screenheight()/2 - windowHeight/2)
    btn_window.geometry(f"{windowWidth}x{windowHeight}+{positionRight}+{positionDown}")
    btn_window.configure(bg="bisque3")
    btn_window.grab_set()

    head = tkinter.Label(btn_window, text="Pay Fees", font=('Courier New', 20, 'bold'), bg="bisque3", fg="bisque3")
    head.place(x=260, y=30)
    btn_window.update()
    pos_x = int((btn_window.winfo_width()/2)-(head.winfo_width()/2))
    pos_y = int((btn_window.winfo_height()/2)-(head.winfo_height()/2))/3
    head['fg'] = "black"
    head.place(x=pos_x, y=pos_y)
    btn_window.update()

    s_list = show_all_stu()
    sid_label = tkinter.Label(btn_window, text="Student ID :", font=('Courier New', 15), bg="bisque3")
    sid_input = ttk.Combobox(btn_window, width=10, font=('Courier New', 15), values=s_list)
    sid_label.place(x=250, y=165)
    sid_input.place(x=405, y=165)

    con_button = tkinter.Button(btn_window, text="Continue", bg="bisque4", activebackground="bisque3", relief="flat", font=("Courier New", 12), cursor="hand2", command=con)
    exit_button1 = tkinter.Button(btn_window, text="Exit", bg="bisque4", activebackground="bisque3", relief="flat", font=("Courier New", 12), cursor="hand2", command=lambda: btn_exit(btn_window))

    con_button.place(x=300, y=290)
    exit_button1.place(x=440, y=290)

    btn_window.bind('<Return>', lambda event: con())
    btn_window.bind('<Escape>', lambda event: btn_window.destroy())
    btn_window.bind('<F5>', lambda event: ref())

    # con_button.bind("<Enter>", lambda event: on_enter(con_button))
    # con_button.bind("<Leave>", lambda event: on_leave(con_button))
    # exit_button1.bind("<Enter>", lambda event: on_enter(exit_button1))
    # exit_button1.bind("<Leave>", lambda event: on_leave(exit_button1))


def addn_charges():
    def pass_add_charges(sid, charges_input):
        amount = charges_input.get()
        give_add_charges(sid, amount)

    def con():
        sid = sid_input.get()
        sid_label.place_forget()
        sid_input.place_forget()
        con_button.place_forget()
        exit_button1.place_forget()

        studid_label = tkinter.Label(btn_window, text="Student ID :", font=('Courier New', 15), bg="bisque3")
        studid_input = tkinter.Label(btn_window, text=sid, font=('Courier New', 15), bg="bisque3")
        sname_label = tkinter.Label(btn_window, text="Name:", font=('Courier New', 15), bg="bisque3")
        sname_input = tkinter.Label(btn_window, text="Name", font=('Courier New', 15), bg="bisque3")

        roomid_label = tkinter.Label(btn_window, text="Room ID:", font=('Courier New', 15), bg="bisque3")
        roomid_input = tkinter.Label(btn_window, text="Room ID", font=('Courier New', 15), bg="bisque3")

        charges_label = tkinter.Label(btn_window, text="Charges(in ₹):", font=('Courier New', 15), bg="bisque3")
        charges_input = tkinter.Entry(btn_window, width=10, font=('Courier New', 15))
        
        add_button = tkinter.Button(btn_window, text="Add Charges", bg="bisque4", activebackground="bisque3", relief="flat", font=("Courier New", 12), cursor="hand2", command=lambda: pass_add_charges(sid, charges_input))
        exit_button = tkinter.Button(btn_window, text="Exit", bg="bisque4", activebackground="bisque3", relief="flat", font=("Courier New", 12), cursor="hand2", command=lambda: btn_exit(btn_window))

        studid_label.place(x=100, y=110)
        studid_input.place(x=255, y=110)
        sname_label.place(x=400, y=110)
        sname_input.place(x=545, y=110)

        roomid_label.place(x=100, y=150)
        roomid_input.place(x=270, y=150)

        charges_label.place(x=400, y=150)
        charges_input.place(x=575, y=150)

        add_button.place(x=280, y=290)
        exit_button.place(x=440, y=290)
    

        btn_window.bind('<Escape>', lambda event: btn_window.destroy())
        btn_window.bind('<F5>', lambda event: ref())

        # add_button.bind("<Enter>", lambda event: on_enter(add_button))
        # add_button.bind("<Leave>", lambda event: on_leave(add_button))
        # exit_button.bind("<Enter>", lambda event: on_enter(exit_button))
        # exit_button.bind("<Leave>", lambda event: on_leave(exit_button))


    btn_window = tkinter.Toplevel(root)
    btn_window.attributes("-topmost", "true")
    btn_window.focus_set()
    btn_window.title("Additional Charges")
    # btn_window.overrideredirect(True)
    windowWidth = 800
    windowHeight = int(root.winfo_screenheight())-400
    positionRight = int(root.winfo_screenwidth()/2 - windowWidth/2)
    positionDown = int(root.winfo_screenheight()/2 - windowHeight/2)
    btn_window.geometry(f"{windowWidth}x{windowHeight}+{positionRight}+{positionDown}")
    btn_window.configure(bg="bisque3")
    btn_window.grab_set()

    head = tkinter.Label(btn_window, text="Additional Charges", font=('Courier New', 20, 'bold'), bg="bisque3", fg="bisque3")
    head.place(x=260, y=30)
    btn_window.update()
    pos_x = int((btn_window.winfo_width()/2)-(head.winfo_width()/2))
    pos_y = int((btn_window.winfo_height()/2)-(head.winfo_height()/2))/3
    head['fg'] = "black"
    head.place(x=pos_x, y=pos_y)
    btn_window.update()
    sid_label = tkinter.Label(btn_window, text="Student ID :", font=('Courier New', 15), bg="bisque3")
    sid_input = ttk.Combobox(btn_window, width=10, font=('Courier New', 15), values=['ABC'])
    sid_label.place(x=250, y=165)
    sid_input.place(x=405, y=165)

    con_button = tkinter.Button(btn_window, text="Continue", bg="bisque4", activebackground="bisque3", relief="flat", font=("Courier New", 12), cursor="hand2", command=con)
    exit_button1 = tkinter.Button(btn_window, text="Exit", bg="bisque4", activebackground="bisque3", relief="flat", font=("Courier New", 12), cursor="hand2", command=lambda: btn_exit(btn_window))

    con_button.place(x=300, y=290)
    exit_button1.place(x=440, y=290)

    btn_window.bind('<Return>', lambda event: con())
    btn_window.bind('<Escape>', lambda event: btn_window.destroy())
    btn_window.bind('<F5>', lambda event: ref())

    # con_button.bind("<Enter>", lambda event: on_enter(con_button))
    # con_button.bind("<Leave>", lambda event: on_leave(con_button))
    # exit_button1.bind("<Enter>", lambda event: on_enter(exit_button1))
    # exit_button1.bind("<Leave>", lambda event: on_leave(exit_button1))


def btnB():
    btnB_window = tkinter.Toplevel(root)
    btnB_window.attributes("-topmost", "true")
    btnB_window.focus_set()
    btnB_window.overrideredirect(True)
    windowWidth = 800
    windowHeight = 500
    positionRight = int(root.winfo_screenwidth()/2 - windowWidth/2)
    positionDown = int(root.winfo_screenheight()/2 - windowHeight/2)
    btnB_window.geometry(f"{windowWidth}x{windowHeight}+{positionRight}+{positionDown}")
    btnB_window.configure(bg="bisque4")
    btnB_window.grab_set()

    btnB_window.bind('<Escape>', lambda event: btnB_window.destroy())
    btnB_window.bind('<F5>', lambda event: ref())

def btnC():
    btnC_window = tkinter.Toplevel(root)
    btnC_window.attributes("-topmost", "true")
    btnC_window.focus_set()
    btnC_window.overrideredirect(True)
    windowWidth = 900
    windowHeight = 500
    positionRight = int(root.winfo_screenwidth()/2 - windowWidth/2)
    positionDown = int(root.winfo_screenheight()/2 - windowHeight/2)
    btnC_window.geometry(f"{windowWidth}x{windowHeight}+{positionRight}+{positionDown}")
    btnC_window.configure(bg="bisque4")
    btnC_window.grab_set()

    btnC_window.bind('<Escape>', lambda event: btnC_window.destroy())
    btnC_window.bind('<F5>', lambda event: ref())
