import mysql.connector as conn
from datetime import *
import bill

con = conn.Connect(host="localhost", user="root", password="Sparsh@08", database="mehta")
cur = con.cursor()


def data(DETAIL, amount):
    table_name = "CREDIT"

    # Execute the SQL query to get the number of rows in the table
    cur.execute(f"SELECT COUNT(*) FROM {table_name}")
    row_count = cur.fetchone()[0]
    Id = str(row_count + 1)

    if row_count == 0:
        current = datetime.now().date()
        stringdate = current.strftime("%d-%m-%Y")
        TOTAL = 0 + int(amount)
        #  SQL Query for inserting data
        a = f'insert into {table_name} (ID, DETAILS, AMOUNT, TOTAL, DATE) VALUES(%s,%s,%s,%s,%s)'
        data = (Id, DETAIL.upper(), int(amount), TOTAL,stringdate,)
        cur.execute(a, data)
        con.commit()
        print("ADDED\n\nDETAIL - {0}\nAMOUNT - {1}\nTOTAL - {2}".format(DETAIL, amount, TOTAL))

    elif row_count != 0:
        current = datetime.now().date()
        stringdate = current.strftime("%d-%m-%Y")
        aa = 'SELECT SUM(AMOUNT) AS TOTAL FROM CREDIT'
        cur.execute(aa)
        result = cur.fetchone()

        priviousBalance = int(result[0])
        Total = priviousBalance + int(amount)

        print(priviousBalance)
        print(Total)

        #  SQL Query for inserting data
        a = f'insert into {table_name} (ID, DETAILS, AMOUNT, TOTAL, DATE) VALUES(%s,%s,%s,%s,%s)'
        data = (Id, DETAIL.upper(), int(amount), Total, stringdate,)
        cur.execute(a, data)
        con.commit()
