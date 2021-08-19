import master_password_hash_generator
import password_generator
from db_connect import db_Connection
import db_connect
import password_Hashing

def interface():
    db_connection = db_Connection()
    option = 0
    while option != 5:
        print("\t\tSELECT AN OPTION\t\t")
        print("-" * 60 + "\n")
        option = input("1. Enter the new password\n2. update the password\n3. Find the password\n4. Show all the passwords\n5. exit\n")
        if option == "1":
            username = input("Enter the username: ")
            password = input("Enter the password: ")
            if password == "":
                password = password_generator.password()
                hashed_password = password_Hashing.encrypt_password(password)
            else:
                hashed_password = password_Hashing.encrypt_password(password)
            email = input("Enter the Email: ")
            app_name = input("Enter the app name or website name: ")
            db_connect.insert(username,hashed_password,email,app_name)
        elif option == "2":
            password = input("Enter the password: ")
            app_name = input("Enter the app_name: ")
            hashed_password = password_Hashing.encrypt_password(password)
            db_connect.update_password(hashed_password,app_name)
        elif option == "3":
            app_name = input("Enter the app_name: ")
            db_connect.find_password(app_name)
        elif option == "4":
            db_connect.password_list()
        elif option == "5":
            exit()
        else:
            print("-" * 60)
            print("Select the correct option\n")


result = password_Hashing.query_master_pwd()

if __name__ == '__main__':
    if result == True:
        interface()
    else:
        print("You Have Entered wrong password")
