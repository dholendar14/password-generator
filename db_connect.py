import psycopg2


def db_Connection():
    conn = psycopg2.connect("dbname=Valut-Db user=postgres password=dholu")
    return conn

