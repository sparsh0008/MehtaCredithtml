import mysql.connector as conn

con = conn.Connect(host="localhost", user="root", password="Sparsh@08", database="mehta")
cur = con.cursor()


def data(DETAIL, amount):
    table_name = "CREDIT"

    # Execute the SQL query to get the number of rows in the table
    cur.execute(f"SELECT COUNT(*) FROM {table_name}")
    row_count = cur.fetchone()[0]
    Id = str(row_count + 1)


    if row_count == 0:

        TOTAL = 0 + amount
        #  SQL Query for inserting data
        a = f'insert into {table_name} (ID, DETAILS, AMOUNT, TOTAL) VALUES(%s,%s,%s,%s)'
        data = (Id, DETAIL.upper(), amount, TOTAL,)
        cur.execute(a, data)
        con.commit()
        print("ADDED\n\nDETAIL - {0}\nAMOUNT - {1}\nTOTAL - {2}".format(DETAIL, amount, TOTAL))

    elif row_count != 0:

        aa = 'SELECT SUM(AMOUNT) AS TOTAL FROM CREDIT'
        cur.execute(aa)
        result = cur.fetchone()

        priviousBalance = int(result[0])
        Total = priviousBalance + int(amount)

        print(priviousBalance)
        print(Total)

        #  SQL Query for inserting data
        a = f'insert into {table_name} (ID, DETAILS, AMOUNT, TOTAL) VALUES(%s,%s,%s,%s)'
        data = (Id, DETAIL.upper(), amount, Total,)
        cur.execute(a, data)
        con.commit()

        print("ADDED\n\nDETAIL - {0}\nAMOUNT - {1}\nTOTAL - {2}".format(DETAIL, amount, Total))
        # m = input("Do you want to View Mini Statement (Y/N) or (y/n) : ")
        # if m == "Y" or m == "y":
        #     print("THANK YOU")
        # elif m == "N" or m == "n":
        #     print("THANK YOU")


if __name__ == '__main__':
    data("HELLO", 100)
