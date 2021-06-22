"""
Before running this make sure you have a databse named hostel_mgmt in your mysql server.
Update login credentials
"""


import mysql.connector
import json

db = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='Admin@root',
    database='hostel_mgmt',
)


# months_due = json.dumps(["JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEPT", "OCT", "NOV", "DEC"])

cursor = db.cursor()

cursor.execute("drop table if exists stu_details")
cursor.execute("drop table if exists student")
cursor.execute("drop table if exists stu_fees")
cursor.execute("drop table if exists courses")
cursor.execute("drop table if exists transactions")
cursor.execute("drop table if exists room")
cursor.execute("drop table if exists blocks")
cursor.execute("drop table if exists staff")
cursor.execute("drop table if exists mess")

cursor.execute("set time_zone = '+5:30'")

cursor.execute(f"create table stu_details(stu_id int(4) primary key auto_increment not null, name longtext not null, dob date not null, guardian_name longtext not null, gender varchar(20) not null, address varchar(255) not null, contact_no bigint(10) not null, guardian_cont_no bigint(10) not null, blood_grp char(5) not null, entry_date timestamp not null default now())")
cursor.execute(f"create table student(stu_id int(4) primary key not null, course_id varchar(6) not null, room_id varchar(10) not null, is_veg char(3) not null, months_due varchar(255) default '[\"JAN\", \"FEB\", \"MAR\", \"APR\", \"MAY\", \"JUN\", \"JUL\", \"AUG\", \"SEPT\", \"OCT\", \"NOV\", \"DEC\"]')")
cursor.execute(f"create table stu_fees(stu_id int(4) primary key not null, room_charges float not null, mess_charges float not null, add_charges float not null, total_charge float generated always as (room_charges+mess_charges+add_charges) stored)")
cursor.execute(f"create table courses(course_id varchar(8) primary key not null, course_name longtext not null, num_sems int(1) not null)")
cursor.execute(f"create table transactions(transaction_id bigint primary key not null auto_increment, stu_id int(4) not null, amount float not null, date_of_tran timestamp default now(), month_paid longtext, remarks longtext)")
cursor.execute(f"create table room(room_id varchar(10) primary key not null, block_id varchar(3) not null, room_type varchar(8) not null, cost int not null, no_of_beds int(3) not null, occupants int(1) not null, status varchar(8) not null default 'vacant')")
cursor.execute(f"create table blocks(block_id varchar(3) primary key not null, block_type varchar(3) not null, warden_id varchar(5) not null, gender varchar(20) not null, no_of_rooms int(3) not null, mess_id varchar(4) not null, vacant int not null, status varchar(8) not null)")
cursor.execute(f"create table staff(staff_id varchar(5) primary key not null, name longtext not null, contact_no bigint(10) not null, gender varchar(8), dob date not null)")
cursor.execute(f"create table mess(mess_id varchar(4) primary key not null, mess_charges int not null)")

db.commit()