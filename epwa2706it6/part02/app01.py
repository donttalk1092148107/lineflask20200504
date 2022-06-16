import psycopg2

conn = psycopg2.connect(database="d22lt2rkasaf2d", user="uonrecelbyjgcj", password="9201b61af6dd39ae37cb7e9f62408bae516a7597b29c6102340374b1ff3550a1", host="ec2-54-81-37-115.compute-1.amazonaws.com", port="5432")
print ("Opened database successfully")

cur = conn.cursor()

cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY)VALUES (1, 'Paul', 32, 'California', 20000.00 )")

cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY)VALUES (2, 'Allen', 25, 'Texas', 15000.00 )")

cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY)VALUES (3, 'Teddy', 23, 'Norway', 20000.00 )")

cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY)VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 )")

conn.commit()
print ("Records created successfully")
conn.close()