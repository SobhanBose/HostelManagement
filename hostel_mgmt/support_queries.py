from hostel_mgmt import db, cursor

def get_last_stu_id():
    cursor.execute(f"select last_insert_id() from stu_details")
    return cursor.fetchone()[0]

def show_vacant_rooms():
    cursor.execute(f"select room_id from room where status='vacant'")
    return [res[0] for res in cursor.fetchall()]


def show_vacant_blocks():
    cursor.execute(f"select block_id from blocks where status='vacant'")
    return [res[0] for res in cursor.fetchall()]


def fetch_room_category(cat):
    cursor.execute(f"select block_id from blocks where gender='{cat}'")
    b_id = cursor.fetchone()[0]
    cursor.execute(f"select room_id from room where block_id='{b_id}'")
    return [res[0] for res in cursor.fetchall()]


def show_all_rooms():
    cursor.execute(f"select room_id from room")
    return [res[0] for res in cursor.fetchall()]


def show_rooms(type):
    cursor.execute(f"select room_id from room where type='{type}'")
    return [res[0] for res in cursor.fetchall()]


def show_rooms_from_block(b_id):
    cursor.execute(f"select room_id from room where block_id='{b_id}' and status='vacant'")
    return [res[0] for res in cursor.fetchall()]


def show_all_blocks():
    cursor.execute("select block_id from blocks")
    return [res[0] for res in cursor.fetchall()]


def get_block_type(b_id):
    cursor.execute(f"select type from blocks where block_id='{b_id}'")
    return cursor.fetchone()[0]


def get_w_id(b_id):
    cursor.execute(f"select warden_id from blocks where block_id='{b_id}'")
    return cursor.fetchone()[0]


def show_courses():
    cursor.execute(f"select course_id from courses")
    return [res[0] for res in cursor.fetchall()]


def show_all_stu():
    cursor.execute(f"select stu_id from student")
    return [res[0] for res in cursor.fetchall()]

def get_stu_name(sid):
    cursor.execute(f"select name from stu_details where stu_id='{sid}'")
    return cursor.fetchone()[0]


def show_all_staff():
    cursor.execute(f"select staff_id from staff")
    return [res[0] for res in cursor.fetchall()]


def show_all_mess():
    cursor.execute(f"select mess_id from mess")
    return [res[0] for res in cursor.fetchall()]


def get_fee_details(sid):
    cursor.execute(f"select room_charges, mess_charges, add_charges, total_charge from stu_fees where stu_id={sid}")
    result = cursor.fetchone()
    room_charges = result[0]
    mess_charges = result[1]
    add_charges = result[2]
    total_charge = result[3]
    return (room_charges, mess_charges, add_charges, total_charge)


def get_tranid(sid):
    cursor.execute(f"select transaction_id, month_paid from transaction where stu_id='{sid}'")
    return cursor.fetchall()