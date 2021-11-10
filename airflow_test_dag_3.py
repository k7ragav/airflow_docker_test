import mysql.connector
from datetime import datetime
mydb = mysql.connector.connect(host="5.255.98.125 ",
                               user = "keshava",
                               password = 'Dhanam_7',
                               database = 'test'
                               )

mycursor = mydb.cursor()

date_check = str(datetime.now())

sql = (f"INSERT INTO airflow_test_3 (date) VALUES ('{date_check}');")
print(sql)
mycursor.execute(sql)
mydb.commit()

