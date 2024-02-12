from csv import *
from fpdf import FPDF

fh = open("student.csv", "w+", newline="")
w = writer(fh)
header = ["Student Id", "Name", "Roll", "Semester", "Shift", 'Department', "Date of Birth", 'Phone No.']
w.writerow(header)
data = []
while True:
    try:
        n = int(input("How many student Records will be inserted: "))
    except ValueError:
        print("Student Record are number. Please enter again:")
        continue
    else:
        break
# noinspection PyUnboundLocalVariable
for i in range(n):
    print(f"Enter the student {i + 1} record: ")
    student_id = input("Student Id: ")
    name = input("Name: ")
    while True:
        try:
            roll = int(input("Roll: "))
        except ValueError:
            print("Invalid Roll. Please Enter again: ")
            continue
        else:
            break
    semester = input("Semester: ")
    shift = input("Shift: ")
    dept = input("Department: ")
    dob = input("Date of birth: ")
    phone_no = input("Phone No.: ")
    # noinspection PyUnboundLocalVariable
    rec = [student_id, name, roll, semester, shift, dept, dob, phone_no]
    data.append(rec)
w.writerows(data)
fh.close()
print("Student Record from stored CSV File")
print("If you went to see pdf report, Please open student pdf file you current dictionary location")
fh = open("student.csv", "r")
r = reader(fh)
pdf = FPDF()
pdf.add_page()
page_width=pdf.w-2*pdf.l_margin


pdf.set_font('Times', "B", 12.0)
pdf.cell(page_width, 0.0, "Students Data Report", align='C')
pdf.ln(10)

pdf.set_font("Courier", "", 12)
col_width = page_width / 6
th = pdf.font_size


for row in r:
    for e in range(6):
        pdf.cell(col_width, th, str(row[e]), border=1)
    pdf.ln(th)
pdf.ln(10)

pdf.set_font("Times", "", 10.0)
pdf.cell(page_width, 0.0, '-end of report-', align='C')


pdf.output("student.pdf")
fh.close()
