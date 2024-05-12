import mysql.connector


def main():
    # Replace these with your database connection details
    db_config = {
        "host": "localhost",
        "user": "root",
        "password": "Sparsh@08",
        "database": "mehta",
    }
    datem = []
    detailsm = []
    amountm = []
    totalm = []

    # Establish a connection to the database
    connection = mysql.connector.connect(**db_config)

    # date fech
    a = 'select Date from credit'
    c = connection.cursor()
    c.execute(a)
    myname = c.fetchall()
    for i in myname:
        d = i[0]
        datem.append(d)

    # date fech
    a = 'select DETAILS from credit'
    c = connection.cursor()
    c.execute(a)
    myname = c.fetchall()
    for i in myname:
        d = i[0]
        detailsm.append(d)

    # date fech
    a = 'select AMOUNT from credit'
    c = connection.cursor()
    c.execute(a)
    myname = c.fetchall()
    for i in myname:
        d = i[0]
        amountm.append(str(d))

    # date fech
    a = 'select TOTAL from credit'
    c = connection.cursor()
    c.execute(a)
    myname = c.fetchall()
    for i in myname:
        d = i[0]
        totalm.append(str(d))

    return datem, detailsm, amountm, totalm

