import psycopg2
import sql_statements
import password_Hashing

'''replace "dbname" with database_name
           "user" with postgresSQL user_name
           "password" with postgresSQL database_password
'''

def db_Connection():
    conn = psycopg2.connect("dbname=****** user=***** password=*****")
    return conn

def insert(username,password,email,app_name):
    try:
        conn = db_Connection()
        cur = conn.cursor()
        insert_query = sql_statements.insert_db_row()
        cur.execute(insert_query,(username,password,email,app_name ))
        conn.commit()
    except (Exception, psycopg2.Error) as error:
        print(error)


def delete():
    try:
        conn = db_Connection()
        cur = conn.cursor()
        delete_query = sql_statements.delete_db_row()
        cur.execute(delete_query,("www.google.com", ))
        conn.commit()
    except (Exception,psycopg2.Error) as error:
        print(error)



def find_password(app_name):
    try:
        conn = db_Connection()
        cur = conn.cursor()
        find_query = sql_statements.find_password()
        cur.execute(find_query,(app_name, ))
        conn.commit()
        result = cur.fetchone()
        print("password is: ")
        print(str(password_Hashing.decrypt_password(result[1]).decode('utf-8')))
    except (Exception,psycopg2.Error) as error:
        print(error)


def update_password(password,app_name):
    try:
        conn = db_Connection()
        cur = conn.cursor()
        update_query = sql_statements.update_password()
        cur.execute(update_query,(password,app_name, ))
        conn.commit()
        print("password has been successfully updated")
    except (Exception,psycopg2.Error) as error:
        print(error)

def password_list():
    conn = db_Connection()
    cur = conn.cursor()
    list_query = sql_statements.password_list()
    cur.execute(list_query)
    record = cur.fetchall()
    for i in range(len(record)):
        entry = record[i]
        print("-" * 40)
        for j in range(len(entry)):
            titles = ["Username: ", "Password: ","email: ","app_name: "]
            if titles[j] == "Password: ":
                bytes_row = entry[j]
                password = password_Hashing.decrypt_password(bytes_row)
                print("Password: " + str(password.decode('utf-8')))
            else:
                print(titles[j] + entry[j])