from getpass import getpass
from db_connect import db_Connection


def interface():
    db_connection = db_Connection()
    print("\t\tSELECT AN OPTION\t\t")
    print("-"*60+"\n")
    option = 0
    while option != 5:
        option = input("1. Enter the new password\n2. update the password\n3. delete the password\n4. Show all the passwords\n5. exit\n")
        if option == "1":
            print("created")
        elif option == "2":
            print("showed")
        elif option == "3":
            pass
        elif option == "4":
            pass
        elif option == "5":
            exit()
        else:
            print("-" * 60)
            print("Select the correct option\n")


master_Password = getpass(prompt='Enter the MASTER password:', stream=None)
print(master_Password)
if master_Password == "venkatasai":
    interface()
