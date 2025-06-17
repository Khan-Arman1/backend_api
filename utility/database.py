import sqlite3 # sqlite3 for database creation
from datetime import datetime # for current date
from dotenv import load_dotenv # load the env file
import os

# loading the fucntion
load_dotenv()

# create a database instance
# But we have already created a database so lets connect to it(if not exits then it will be created)
connection = sqlite3.connect("student_records.db")
# create a cursor instance
cursor = connection.cursor()
if connection:
    if cursor:
        print("cursor -", cursor)
        # Now create a new table into the database
        table_creation = """
                CREATE TABLE IF NOT EXISTS user_access_record(
                    user_email VARCHAR(20) PRIMARY KEY,
                    user_password VARCHAR(10) UNIQUE,
                    user_creadits INTEGER(3),
                    register_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    )"""


    def user_registration(Uemail,Upassword):
        """
        Create table if not exists, creates a user login 
        """
        # print("connection -", connection)
        # Now execute the above query
        if cursor.execute(table_creation):
            print("Table creation success")
        # Insert some records into the table
        query1 = """INSERT INTO user_access_record(user_email,user_password,user_creadits,register_date)
          VALUES(?,?,?,?);"""
        query1_data = (Uemail,Upassword,'15',datetime.today())
        # print(datetime.now())
        # user date.today() for current date only for more details use datetime.now()
        # Now insert it into the table
        try:
            if cursor.execute(query1,query1_data):
                connection.commit()
                print("record insertion success")
        except sqlite3.IntegrityError as E:
            return Exception("User Already Exists ",E)
        
            # print("Insertion skipped (probably due to duplicate key):", E)
        # # select table user_credit recorded value
        # query2 = """SELECT * FROM user_access_record WHERE user_email = ?;"""
        # if cursor.execute(query2,(Uemail,)):
        #     result = cursor.fetchone()
        #     if len(result) == 0:
        #         print(f"{len(result)} records found")
        #     else:
        #         print("Record found- ",result)



    def update_table(email_logged_in,credits_remain):
        """
        Update user credits 
        """
        # Now update a record
        update_query = """UPDATE user_access_record
        SET user_creadits = ?
        WHERE user_email = ?
        """
        updation_data = (credits_remain,email_logged_in)
        cursor.execute(update_query,updation_data) # execute the above query
        connection.commit()

        # # select table user_credit recorded value
        # query2 = """SELECT * FROM user_access_record WHERE user_email = ?;"""
        # if cursor.execute(query2,(email_logged_in,)):
        #     result = cursor.fetchone()
        #     if len(result) == 0:
        #         print(f"{len(result)} records found")
        #     else:
        #         print("Record found- ",result)

    def check_user_existance(checking_mail,checking_pwd):
        """
        Checks weather the user exists or not
        """
        # select table user_credit recorded value
        query3 = """SELECT user_email,user_creadits FROM user_access_record WHERE user_email = ? 
        AND user_password = ?;"""
        try:
            if cursor.execute(query3,(checking_mail,checking_pwd)):
                result = cursor.fetchall()
                if len(result) == 0:
                    print("not found", result)
                else:
                    returned_tuple = result[0]
                    print(returned_tuple[0])
                    print(returned_tuple[1])
                    return returned_tuple
        except:
            print("record not found")
            return "notfounduser"
                

        
        



# print("Your Email- ",user_mail,"\nYour Password- ", user_pass)
print("registering user")
user_mail1,user_pass = str(input("Reg Email - ")),str(input("Reg Password - "))
user_registration(Uemail=user_mail1,Upassword=user_pass)

# print("udpating user credits")
# user_mail2,user_credits = str(input("Up Email- ")),int(input("Up Credits- "))
# update_table(email_logged_in=user_mail2,credits_remain=user_credits)

print("checking user existence")
user_mail3,user_pass2 = str(input("Reg Email - ")),str(input("Reg Password - "))
check_user_existance(user_mail3,user_pass2)


# Now ends the connection
connection.close()