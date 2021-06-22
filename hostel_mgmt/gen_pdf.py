from num2words import num2words
from reportlab.pdfgen import canvas
from num2words import num2words


def gen_pdf(stu_name, stu_id, c_id, r_id, r_type, t_id, t_date, month_paid_list, r_charge, m_charge, late_fee, add_fee, total_charge):
    fileName = f'FeeReceipt{t_id}.pdf'
    documentTitle = 'Hostel Management'
    title = 'Hostel Management'
    subTitle = 'Fee Receipt'

    pdf = canvas.Canvas(fileName)
    pdf.setTitle(documentTitle)

    pdf.setFont("Courier-Bold", 24)
    pdf.drawCentredString(290, 770, title)

    name = f"Name: {stu_name}"
    stu_id = f"Student ID.: {stu_id}"
    c_id = f"Course ID: {c_id}"
    r_id = f"Room ID: {r_id}"
    r_type = f"Room Type: {r_type}"
    tran_id = f"Transaction ID: {t_id}"
    tran_date = f"Transaction Date: {t_date}"
    month_paid = "Month Paid: "+str(", ".join(month_paid_list))

    pdf.setFont("Courier", 8)
    pdf.drawString(90, 720, name)
    pdf.drawString(90, 705, stu_id)
    pdf.drawString(90, 690, c_id)
    pdf.drawString(90, 675, r_id)
    pdf.drawString(90, 660, r_type)
    pdf.drawString(320, 720, tran_id)
    pdf.drawString(320, 705, tran_date)
    pdf.drawString(320, 690, month_paid)


    bed_charge_label = "Bed Charge: "
    bed_charge = f"₹ {r_charge}"
    mess_charge_label = "Mess Charge: "
    mess_charge = f"Rs {m_charge}"
    late_fee_label = "Late Fee: "
    late_fee = f"₹ {late_fee}"
    add_fee_label = "Additional Fee: "
    add_fee = f"₹ {add_fee}"
    total_fee_label = "Total Amount Payable: "
    total_fee = f"₹ {total_charge}"
    words_label = "Total Amount Payable in Words: "
    total_fee_inwords = "₹ " + num2words(int(total_fee[4:])).replace(",", "").title()


    pdf.setFont("Courier", 10)
    pdf.drawString(150, 540, bed_charge_label)
    pdf.drawString(150, 515, mess_charge_label)
    pdf.drawString(150, 490, late_fee_label)
    pdf.drawString(150, 465, add_fee_label)
    pdf.line(120, 445, 450, 445)
    pdf.drawString(150, 425, total_fee_label)

    pdf.drawString(370, 540, bed_charge)
    pdf.drawString(370, 515, mess_charge)
    pdf.drawString(370, 490, late_fee)
    pdf.drawString(370, 465, add_fee)
    pdf.drawString(370, 425, total_fee)
    pdf.setFont("Courier", 6)
    pdf.drawString(150, 410, words_label)
    pdf.drawString(270, 410, total_fee_inwords)

    pdf.setFont("Courier", 18)
    pdf.drawCentredString(290,620, subTitle)

    pdf.line(30, 610, 550, 610)


    pdf.save()