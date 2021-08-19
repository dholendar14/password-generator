import hashlib


'''hash your master password'''
def master_password_gen():
    master_password = input("Enter your password: ").encode()
    hased_master_password = hashlib.sha256(master_password).hexdigest()
    print(hased_master_password)

master_password_gen()