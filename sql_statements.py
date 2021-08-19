def insert_db_row():
    insert_query = """INSERT INTO passwords (username,password,url,app_name) values (%s, %s, %s, %s)"""
    return insert_query


def delete_db_row():
    delete_query = """delete from passwords Where url = %s"""
    return delete_query


def find_password():
    find_query = """select * from passwords where app_name = %s"""
    return find_query


def update_password():
    update_query = """ UPDATE passwords SET password = %s WHERE app_name = %s"""
    return update_query

def password_list():
    list_query = """select * from passwords"""
    return list_query