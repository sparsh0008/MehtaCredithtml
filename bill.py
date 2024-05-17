from datetime import datetime
from reportlab.pdfgen import canvas
import openpdf
import fetch
import calendar


def dateSet(year, month):
    return calendar.monthrange(year, month)[1]


def main():
    local = datetime.now()
    t = local.strftime(" %d-%m-%Y %H %M %S")
    td = local.strftime("%d-%m-%Y")
    name = "MEHTA GENERAL STORE"
    file_path = "E:/Invoice/" + name + t + ".pdf"
    loc = "MEHTA GENERAL STORE"

    # Create a PDF document
    pdf = canvas.Canvas(file_path)

    # Set the title of the PDF
    pdf.setTitle(file_path)

    # Add text to the PDF

    pdf.drawString(170, 710, 'MONTHLY CREDIT NOTE - HN 455R MODEL TOWN')

    pdf.drawString(100, 685, '*' * 85)

    pdf.drawString(100, 670, "Date : {}".format(td))
    pdf.drawString(100, 655, "Location : {}".format(loc))

    pdf.drawString(100, 635, '-' * 99)

    pdf.drawString(100, 620, "DATE")
    pdf.drawString(200, 620, "DETAILS")
    pdf.drawString(400, 620, "AMOUNT")
    pdf.drawString(460, 620, "TOTAL")

    pdf.drawString(100, 605, '-' * 99)

    # today = datetime.date.today()
    # s = today.strftime('%d-%m-%Y')
    sp = td.split("-")
    int_year = int(sp[2])
    int_month = int(sp[1])
    numberOfDate = dateSet(int_year, int_month)
    if int_month < 10:
        start_date = "01-0" + str(int_month) + "-" + str(int_year)
        end_date = str(numberOfDate) + "-0" + str(int_month) + "-" + str(int_year)
        dates_m, details_m, amount_m, total_m = fetch.main(start_date, end_date)
    else:
        start_date = "01-" + str(int_month) + "-" + str(int_year)
        print("Start Date - ", start_date)
        end_date = str(numberOfDate) + "-" + str(int_month) + "-" + str(int_year)
        dates_m, details_m, amount_m, total_m = fetch.main(start_date, end_date)

    y = 590
    for i in dates_m:
        pdf.drawString(100, y, i)
        y = y - 20
    y = 590
    for d in details_m:
        pdf.drawString(200, y, d)
        y = y - 20
    y = 590
    for a in amount_m:
        pdf.drawString(410, y, a)
        y = y - 20
    y = 590
    for t in total_m:
        pdf.drawString(470, y, t)
        y = y - 20
    length = len(total_m)

    pdf.drawString(100, y + 5, '-' * 99)
    pdf.drawString(330, y - 13, "TOTAL OUTSTANDING - ".format(total_m[length - 1]))
    pdf.drawString(470, y - 13, "{}".format(total_m[length - 1]))
    pdf.drawString(100, y - 30, '-' * 99)

    # Save the PDF
    pdf.save()
    print(f"INVOICE : {file_path}")
    openpdf.main(file_path)


if __name__ == '__main__':
    main()
