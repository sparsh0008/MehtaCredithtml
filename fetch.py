import mysql.connector


def main(sd, ed):
    db_config = {
        "host": "localhost",
        "user": "root",
        "password": "Sparsh@08",
        "database": "mehta",
    }

    date_m = []
    details_m = []
    amount_m = []
    total_m = []

    # Establish a connection to the database
    connection = mysql.connector.connect(**db_config)

    a = 'select Date from credit WHERE Date BETWEEN %s AND %s'
    data = (sd, ed,)
    c = connection.cursor()
    c.execute(a, data)
    myname = c.fetchall()
    for i in myname:
        d = i[0]
        date_m.append(d)

    # date fech
    a = 'select DETAILS from credit WHERE Date BETWEEN %s AND %s'
    data = (sd, ed,)
    c = connection.cursor()
    c.execute(a, data)
    myname = c.fetchall()
    for i in myname:
        d = i[0]
        details_m.append(d)

    # date fech
    a = 'select AMOUNT from credit WHERE Date BETWEEN %s AND %s'
    data = (sd, ed,)
    c = connection.cursor()
    c.execute(a, data)
    myname = c.fetchall()
    for i in myname:
        d = i[0]
        amount_m.append(str(d))

    # date fech
    a = 'select TOTAL from credit WHERE Date BETWEEN %s AND %s'
    data = (sd, ed,)
    c = connection.cursor()
    c.execute(a, data)
    myname = c.fetchall()
    for i in myname:
        d = i[0]
        total_m.append(str(d))

    return date_m, details_m, amount_m, total_m
