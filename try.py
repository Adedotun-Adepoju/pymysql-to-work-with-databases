import pymysql

# TO view all the databases in the server
db=pymysql.connect(host="localhost",user="guest",passwd="welcome123",db="studentsdb") # open database connection
cursor=db.cursor() # Prepare a cursor object
cursor.execute('SHOW DATABASES')
data=cursor.fetchall()
print(f'The available databses are {data}') # Print all the available databases
# Results printed in terminal: (('information_schema',), ('mysql',), ('performance_schema',), ('studentsdb',), ('sys',), ('testdb',))
db.close()

# To view the tables in the studentsdb database
db=pymysql.connect(host="localhost",user="guest",passwd="welcome123",db="studentsdb") # open database connection
cursor=db.cursor() # Prepare a cursor object
cursor.execute("USE studentsdb") # select the studentsdb
cursor.execute("""SHOW TABLES""")
data=cursor.fetchall()
print(f'The tables in studentsdb are {data}')
# Results i=displayed in terminal : The tables in studentsdb are (('cgpa',), ('user',))
db.close()

# To drop a table
db=pymysql.connect(host="localhost",user="guest",passwd="welcome123",db="studentsdb") # open database connection
cursor=db.cursor() # Prepare a cursor object
cursor.execute("USE studentsdb") # select the studentsdb
cursor.execute("DROP TABLE if exists cgpa") # Drop the cgpa table
db.close()

# To create another table
db=pymysql.connect(host="localhost",user="guest",passwd="welcome123",db="studentsdb") # open database connection
cursor=db.cursor() # Prepare a cursor object
cursor.execute("USE studentsdb") # select the studentsdb
sql="""CREATE TABLE demography(
                reg_no INT NOT NULL,
                state  VARCHAR(40),
                PRIMARY KEY(reg_no))"""
#cursor.execute(sql)
db.close()

# Insert Operation
db=pymysql.connect(host="localhost",user="guest",passwd="welcome123",db="studentsdb") # open database connection
cursor=db.cursor() # Prepare a cursor object
cursor.execute("USE studentsdb") # select the studentsdb
sql="""INSERT INTO user(reg_no,matric_no,first_name,last_name) VALUES ('15001','15cg02893','Emmanuel','Oluleye'),
                                                                       ('16001','16ght050','Dave','Ade')"""
try:
   # Execute the SQL command
   cursor.execute(sql)
   # Commit your changes in the database
   db.commit()
except:
   # Rollback in case there is any error
   db.rollback()

# disconnect from server
db.close()

# Read Operation
db=pymysql.connect(host="localhost",user="guest",passwd="welcome123",db="studentsdb") # open database connection
cursor=db.cursor() # Prepare a cursor object
cursor.execute("USE studentsdb") # select the studentsdb
sql="""SELECT * FROM user"""
cursor.execute(sql)
results=cursor.fetchall()
for index,row in enumerate(results):
    id=row[0]
    matric_no=row[1]
    first_name=row[2]
    last_name=row[3]

    #print fetched result
    print(f'The record {index+1} is: \nid={id},matriculation number={matric_no},first_name={first_name},last_name={last_name}')
db.close()

# DELETE operation
db=pymysql.connect(host="localhost",user="guest",passwd="welcome123",db="studentsdb") # open database connection
cursor=db.cursor() # Prepare a cursor object
cursor.execute("USE studentsdb") # select the studentsdb
sql="""DELETE FROM user WHERE first_name='%s' % ('Emmanuel') """