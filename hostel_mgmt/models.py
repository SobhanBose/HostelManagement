import re
from hostel_mgmt import db, cursor
import json
from datetime import datetime
from hostel_mgmt.gen_pdf import gen_pdf
from collections import Counter

month_index = {"JAN": 1, "FEB": 2, "MAR": 3, "APR": 4, "MAY": 5, "JUN": 6, "JUL": 7, "AUG": 8, "SEPT": 9, "OCT": 10, "NOV": 11, "DEC": 12}


def insert_stu(name, dob, c_id, g_name, gender, add, r_id, c_no, g_c_no, blood_grp, is_veg):
    #Inserting into stu_details table
    cursor.execute(f"insert into stu_details (name, dob, guardian_name, gender, address, contact_no, guardian_cont_no, blood_grp) values ('{name}', '{dob}', '{g_name}', '{gender}', '{add}', {c_no}, {g_c_no}, '{blood_grp}')")
    db.commit()

    cursor.execute(f"select last_insert_id() from stu_details ")
    id = cursor.fetchone()[0]

    cursor.execute(f"select cost from room where room_id='{r_id}'")
    room_charges = cursor.fetchone()[0]
    
    cursor.execute(f"select block_id from room where room_id='{r_id}'")
    block_id = cursor.fetchone()[0]

    cursor.execute(f"select mess_id from blocks where block_id='{block_id}'")
    mess_id = cursor.fetchone()[0]

    cursor.execute(f"select mess_charges from mess where mess_id='{mess_id}'")
    mess_charges = cursor.fetchone()[0]

    #Inserting into stu_fees table
    cursor.execute(f"insert into stu_fees (stu_id, room_charges, mess_charges, add_charges) values ({id}, {room_charges}, {mess_charges}, 0)")
    db.commit()

    cursor.execute(f"select total_charge from stu_fees where stu_id='{id}'")
    total_charge = cursor.fetchone()[0]

    #Inserting into student table
    cursor.execute(f"insert into student (stu_id, course_id, room_id, is_veg) values ({id}, '{c_id}', '{r_id}', '{is_veg}')")
    db.commit()

    #Update room occupants and status
    cursor.execute(f"select occupants from room where room_id='{r_id}'")
    occupants = int(cursor.fetchone()[0])
    cursor.execute(f"select no_of_beds from room where room_id='{r_id}'")
    num_beds = int(cursor.fetchone()[0])
    cursor.execute(f"update room set occupants=occupants+1 where room_id='{r_id}'")
    if occupants+1 == num_beds:
        cursor.execute(f"update room set status='occupied' where room_id='{r_id}'")

    #Update block status
    cursor.execute(f"select vacant from blocks where block_id='{block_id}'")
    vacancy = int(cursor.fetchone()[0])
    cursor.execute(f"select no_of_rooms from blocks where block_id='{block_id}'")
    num_rooms = int(cursor.fetchone()[0])
    cursor.execute(f"update blocks set vacant=vacant+1 where block_id='{block_id}'")
    if vacancy+1 == num_rooms:
        cursor.execute(f"update blocks set status='occupied' where block_id='{block_id}'") 

    db.commit()


def change_stu_details(id, name, g_name, add, c_no, g_c_no, is_veg):
    #Updating student details
    cursor.execute(f"update stu_details set name='{name}', guardian_name='{g_name}', address='{add}', contact_no={c_no}, guardian_cont_no={g_c_no} where stu_id={id}")
    cursor.execute(f"update student set is_veg='{is_veg}'")
    db.commit()


def change_room(stu_id, new_b_id, new_r_id):
    cursor.execute(f"select cost from room where room_id='{new_r_id}'")
    room_charges = cursor.fetchone()[0]

    cursor.execute(f"select mess_id from blocks where block_id='{new_b_id}'")
    mess_id = cursor.fetchone()[0]

    cursor.execute(f"select mess_charges from mess where mess_id='{mess_id}'")
    mess_charges = cursor.fetchone()[0]

    cursor.execute(f"select room_id from student where stu_id={stu_id}")
    old_r_id = cursor.fetchone()[0]

    cursor.execute(f"select block_id from room where room_id='{old_r_id}'")
    old_b_id = cursor.fetchone()[0]

    #Change room
    cursor.execute(f"update student set room_id='{new_r_id}' where stu_id={stu_id}")
    cursor.execute(f"update stu_fees set room_charges={room_charges}, mess_charges={mess_charges} where stu_id={stu_id}")

    #Update room occupants and status
    cursor.execute(f"select occupants from room where room_id='{new_r_id}'")
    occupants = int(cursor.fetchone()[0])
    cursor.execute(f"select no_of_beds from room where room_id='{new_r_id}'")
    num_beds = int(cursor.fetchone()[0])
    cursor.execute(f"update room set occupants=occupants+1 where room_id='{new_r_id}'")
    if occupants+1 == num_beds:
        cursor.execute(f"update room set status='occupied' where room_id='{new_r_id}'")

    #Update block status
    cursor.execute(f"select vacant from blocks where block_id='{new_b_id}'")
    vacancy = int(cursor.fetchone()[0])
    cursor.execute(f"select no_of_rooms from blocks where block_id='{new_b_id}'")
    num_rooms = int(cursor.fetchone()[0])
    cursor.execute(f"update blocks set vacant=vacant+1 where block_id='{new_b_id}'")
    if vacancy+1 == num_rooms:
        cursor.execute(f"update blocks set status='occupied' where block_id='{new_b_id}'")

    #Update old room/block details
    cursor.execute(f"update room set occupants=occupants-1, status='vacant' where room_id='{old_r_id}'")
    cursor.execute(f"update blocks set vacant=vacant-1, status='vacant' where block_id='{old_b_id}'")

    db.commit()


def insert_block(id, type, w_id, gender, mess_id, num_rooms, num_single, num_double, num_tripple):
    #Creating blocks
    cursor.execute(f"insert into blocks values ('{id}', '{type}', '{w_id}', '{gender}', {num_rooms}, '{mess_id}', {num_rooms}, 'vacant')")
    db.commit()

    if type == "NAC":
        cost_single = 3000
        cost_double = 2500
        cost_tripple = 2000
    elif type == "AC":
        cost_single = 4000
        cost_double = 3500
        cost_tripple = 3000

    #Creating rooms
    for num in range(1, num_single+1):
        cursor.execute(f"insert into room values ('{id}{str(num).zfill(3)}', '{id}', '{type}', {float(cost_single)}, 1, 0, 'vacant')")
    for num in range(num_single+1, num_single+num_double+1):
        cursor.execute(f"insert into room values ('{id}{str(num).zfill(3)}', '{id}', '{type}', {float(cost_double)}, 2, 0, 'vacant')")
    for num in range(num_single+num_double+1, num_single+num_double+num_tripple+1):
        cursor.execute(f"insert into room values ('{id}{str(num).zfill(3)}', '{id}', '{type}', {float(cost_tripple)}, 3, 0, 'vacant')")

    db.commit()


def extend_block(id, type, size, num_of_rooms):
    cursor.execute(f"select room_id from room where block_id='{id}'")
    n = int(cursor.fetchall()[-1][0][2:])
    
    cursor.execute(f"select type from blocks where block_id='{id}'")
    type = cursor.fetchone()[0]

    if type == "NAC":
        cost_single = 3000
        cost_double = 2500
        cost_tripple = 2000
    elif type == "AC":
        cost_single = 4000
        cost_double = 3500
        cost_tripple = 3000

    if size == 'single':
        beds = 1
        cost = cost_single
    elif size == 'double':
        beds = 2
        cost = cost_double
    elif size == 'tripple':
        beds = 3
        cost = cost_tripple
    
    #Adding rooms
    for num in range(n+1, num_of_rooms+1):
        cursor.execute(f"insert into room values ('{id}{str(num).zfill(3)}', '{id}', '{type}', {float(cost)}, {beds}, 0, 'vacant')")
    
    db.commit()


def change_warden(b_id, w_id):
    #Change warden
    cursor.execute(f"update blocks set warden_id='{w_id}' where block_id='{b_id}'")
    db.commit()


def insert_mess(id, charges=2100):
    #Inserting into mess table
    cursor.execute(f"insert into mess values ('{id}', {charges})")
    db.commit()


def insert_staff(id, name, c_no, dob, gender):
    #Adding staff
    cursor.execute(f"insert into staff values ('{id}', '{name}', {c_no}, '{gender}', '{dob}')")
    db.commit()


def change_staff_details(id, name, c_no):
    #Changing staff details
    cursor.execute(f"update staff set name='{name}' contact_no='{c_no}'where staff_id='{id}'")
    db.commit()


# def change_assigned_block(s_id, new_b_id):
#     #Changing assigned block
#     cursor.execute(f"update table staff set block_id='{new_b_id}'where staff_id='{s_id}'")
#     db.commit()


def insert_course(c_id, c_name, sems):
    #Adding a course
    cursor.execute(f"insert into courses values ('{c_id}', '{c_name}', {sems})")
    db.commit()


def transaction(s_id):
    cursor.execute(f"select months_due from student where stu_id={s_id}")
    month_list = json.loads(f"{cursor.fetchone()[0]}")

    #Month to be paid
    month_paid = month_list.pop(0)
    month_paid_index = month_index[month_paid]
    months_due = json.dumps(month_list)

    #Calculating Charges & Date
    cursor.execute(f"select room_charges, mess_charges, add_charges, total_charge from stu_fees where stu_id={s_id}")
    result = cursor.fetchone()
    room_charges = result[0]
    mess_charges = result[1]
    add_charges = result[2]
    total_charge = result[3]

    date = datetime.now()
    # month = month_index[date.strftime("%a").upper()]
    month = int(date.strftime("%m"))

    late_fee = float(100*(abs(month-month_paid_index)))

    fee_amount = total_charge + late_fee
    
    #Remarks to get data later during bill generation
    remarks = json.dumps({"room_charge": room_charges, "mess_charges": mess_charges, "late_fee": late_fee, "add_charges": add_charges})

    #Making transaction
    cursor.execute(f"insert into transactions (stu_id, amount, month_paid, remarks) values ({s_id}, {fee_amount}, '{month_paid}', '{remarks}')")

    cursor.execute(f"update student set months_due='{months_due}' where stu_id={s_id}")

    cursor.execute(f"update stu_fees set add_charges={float(0)} where stu_id={s_id}")

    db.commit()


def give_add_charges(s_id, amount):
    cursor.execute(f"update stu_fees set add_charges=add_charges+{amount} where stu_id='{s_id}'")
    db.commit()


def gen_monthly_bill(s_id, t_id):
    #Student details
    cursor.execute(f"select name, course_id, room_id, from stu_details, student where stu_details.stu_id=student.stu_id and stu_id={s_id}")
    result = cursor.fetchone()
    name = result[0]
    c_id = result[1]
    r_id = result[2]

    cursor.execute(f"select room_type from room where room_id='{r_id}'")
    r_type = cursor.fetchone()[0]

    #Fee details
    cursor.execute(f"select date_of_tran, month_paid, amount, remarks from transactions where transaction_id={t_id}")
    result = cursor.fetchone()
    t_date = result[0]
    month_paid_list = list(result[1])
    total_charge = result[2]
    remarks = json.loads(result[3])
    r_charge = remarks["room_charge"]
    m_charge = remarks["mess_charges"]
    late_fee = remarks["late_fee"]
    add_fee = remarks["add_charges"]

    gen_pdf(name, s_id, c_id, r_id, r_type, t_id, t_date, month_paid_list, r_charge, m_charge, late_fee, add_fee, total_charge)


#Generate Cumulative Bill - Incomplete
def gen_cum_bill(s_id):
    #Months paid for till date
    month_list = list(month_index.keys())
    cursor.execue(f"select months_due from student where stu_id={s_id}")
    month_due_list = cursor.fetchone()[0]
    month_paid_list = list((Counter(month_list)-Counter(month_due_list)).elements())

    #Student details
    cursor.execute(f"select name, course_id, room_id, from stu_details, student where stu_details.stu_id=student.stu_id")
    result = cursor.fetchone()
    name = result[0]
    c_id = result[1]
    r_id = result[2]

    cursor.execute(f"select room_type from room where room_id='{r_id}'")
    r_type = cursor.fetchone()[0]

    #Fee details
    cursor.execute(f"select amount, remarks from transactions having stu_id={s_id}")
    result = cursor.fetchall()


def del_stu(s_id):
    cursor.execute(f"select r_id from student where stu_id={s_id}")
    r_id = cursor.fetchone()[0]
    cursor.execute(f"select b_id from room where room_id='{r_id}'")
    b_id = cursor.fetchone()[0]

    #Update block status
    cursor.execute(f"select status from blocks where block_id='{b_id}'")
    status = cursor.fetchone()[0]
    if status == "occupied":
        cursor.execute(f"update blocks set status='vacant' where block_id='{b_id}'")
    cursor.execute(f"update blocks set vacant=vacant-1 where block_id='{b_id}'")

    #Update room_status
    cursor.execute(f"select status from blocks where block_id='{b_id}'")
    status = cursor.fetchone()[0]
    if status == "occupied":
        cursor.execute(f"update room set status='occupied' where room_id='{r_id}'")
    cursor.execute(f"update room set occupants=occupants-1 where room_id='{r_id}'")

    #Removing student details
    cursor.execute(f"remove from student where stu_id={s_id}")
    cursor.execute(f"remove from stu_fees where stu_id={s_id}")
    cursor.execute(f"remove from student where stu_id={s_id}")

    db.commit()


def del_staff(id):
    cursor.execute(f"select warden_id from blocks")
    res = cursor.fetchone()
    if id in res:
        return False    #Assigned as warden
    else:
        cursor.execute(f"remove from staff where staff_id='{id}'")
        db.commit()







