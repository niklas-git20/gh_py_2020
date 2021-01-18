# ATM with database functionality
# create ATM database with tables:
# account, users balances, users transactions, users promoes

import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return conn

def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
        conn.close()
    except Error as e:
        print(e)

def insert_tables(conn, insert_table_sql, record_table_sql):
    """ insert a data into table from the insert_table_sql statement
    :param conn: Connection object
    :param insert_table_sql: a INSERT INTO statement
    :param record_table_sql: list with inserted data
    :return:
    """
    try:
        c = conn.cursor()
        c.executemany(insert_table_sql, record_table_sql)
        conn.commit()
    except Error as e:
        print(e)


def select_table(conn, select_table_sql):
    """ select a data into table from the select_table_sql statement
    :param conn: Connection object
    :param select_table_sql: a SELECT statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(select_table_sql)
        rd = c.fetchall()
        conn.commit()
        return rd
    except Error as e:
        print(e)

def update_table(conn, update_table_sql):
    """ update a data into table from the update_table_sql statement
    :param conn: Connection object
    :param update_table_sql: a UPDATE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(update_table_sql)
        conn.commit()
    except Error as e:
        print(e)

def delete_table(conn, delete_table_sql):
    """ delete a data from table from the delete_table_sql statement
    :param conn: Connection object
    :param delete_table_sql: a DELETE statement
    :return:
    """
    try:
        c = conn.cursor()
        c.execute(delete_table_sql)
        conn.commit()
    except Error as e:
        print(e)


if __name__ == '__main__':
	# create ATM SQLite3 database
	atm_sqlite_db = r"C:\\Users\\Nik\\Desktop\\gh_py_2020\\HT_13_atm\\atmsqlite.db"
	user_list = [(1, 'john', '12'), (2, 'jane', '34'), (3, 'tom', '56'), (4, 'timaty', '156')]
	user_balance = [(1, 'john', '2021-01-01', 100), (2, 'jane', '2021-01-01', 200), 
					(3, 'tom', '2021-01-01', 300), (4, 'timaty', '2021-01-01', 400)]
	user_promo = [(1, 'john', 0, 0), (2, 'jane', 0, 0), 
					(3, 'tom', 0, 0), (4, 'timaty', 0, 0)]
	user_trans = [('2021-01-01', 0)]
	note_box = [(99, 99, 99, 99, 99, 99)]

	##### initialize users account table ######
	# create user accounts table
	conn = create_connection(atm_sqlite_db)
	sql_cmd = " CREATE TABLE IF NOT EXISTS "
	table_name = "users"
	table_cons = """ (
				id integer PRIMARY KEY,
				name text NOT NULL,
				pass text
				);"""
	sql_query = sql_cmd + table_name + table_cons
	create_table(conn, sql_query)

	# insert data to user accounts table
	conn = create_connection(atm_sqlite_db)
	sql_cmd = " INSERT INTO "
	table_name = "users"
	table_cons = " VALUES (?, ?, ?)"			
	sql_query = sql_cmd + table_name + table_cons
	insert_tables(conn, sql_query, user_list)	

	# read data from user accounts table
	conn = create_connection(atm_sqlite_db)
	sql_cmd = " SELECT * FROM "
	table_name = "users"
	table_cons = " "
	sql_query = sql_cmd + table_name + table_cons
	usr_data = select_table(conn, sql_query)
	print(usr_data)

	# delete data from user accounts table
	# temporary delete account 'timaty'
	conn = create_connection(atm_sqlite_db)
	sql_cmd = " DELETE FROM "
	table_name = "users"
	table_cons = " WHERE name IS 'timaty'"
	sql_query = sql_cmd + table_name + table_cons
	usr_data = delete_table(conn, sql_query)

	# update data in user accounts table
	# temporary change password for account 'tom'
	conn = create_connection(atm_sqlite_db)
	sql_cmd = " UPDATE "
	table_name = "users"
	table_data = " SET pass = 56 "
	table_cons = " WHERE name IS 'tom'"
	sql_query = sql_cmd + table_name + table_data + table_cons
	usr_data = update_table(conn, sql_query)
	

	##### initialize users balance table ######
	# create user balance table
	conn = create_connection(atm_sqlite_db)	
	sql_cmd = " CREATE TABLE IF NOT EXISTS "
	table_name = "balance"
	table_cons = """ (
				id integer PRIMARY KEY,
				name text NOT NULL,
				bdate text,
				bamm int
				);"""
	sql_query = sql_cmd + table_name + table_cons
	create_table(conn, sql_query)

	# insert data to user balance table
	conn = create_connection(atm_sqlite_db)
	sql_cmd = " INSERT INTO "
	table_name = "balance"
	table_cons = " VALUES (?, ?, ?, ?)"			
	sql_query = sql_cmd + table_name + table_cons
	insert_tables(conn, sql_query, user_balance)

	# read data from user balance table
	conn = create_connection(atm_sqlite_db)
	sql_cmd = " SELECT * FROM "
	table_name = "balance"
	table_cons = " "
	sql_query = sql_cmd + table_name + table_cons
	usr_data = select_table(conn, sql_query)
	print(usr_data)

	##### initialize users promotion table ######
	# create user promotion table
	conn = create_connection(atm_sqlite_db)	
	sql_cmd = " CREATE TABLE IF NOT EXISTS "
	table_name = "promo"
	table_cons = """ (
					id integer PRIMARY KEY,
					name text,
					entry int,
					bonus_entry int
					);"""
	sql_query = sql_cmd + table_name + table_cons
	create_table(conn, sql_query)

	# insert data to user promotion table
	conn = create_connection(atm_sqlite_db)
	sql_cmd = " INSERT INTO "
	table_name = "promo"
	table_cons = " VALUES (?, ?, ?, ?)"			
	sql_query = sql_cmd + table_name + table_cons
	insert_tables(conn, sql_query, user_promo)

	# read data from user promotion table
	conn = create_connection(atm_sqlite_db)
	sql_cmd = " SELECT * FROM "
	table_name = "promo"
	table_cons = " "
	sql_query = sql_cmd + table_name + table_cons
	usr_data = select_table(conn, sql_query)
	print(usr_data)

	##### initialize note box table ######
	# create note box table
	conn = create_connection(atm_sqlite_db)	
	sql_cmd = " CREATE TABLE IF NOT EXISTS "
	table_name = "note_box"
	table_cons = """ (
					'50' integer,
					'20' integer,
					'10' integer,
					'5' integer,
					'2' integer,
					'1' integer
					);"""
	sql_query = sql_cmd + table_name + table_cons
	create_table(conn, sql_query)

	# insert data to note box table
	conn = create_connection(atm_sqlite_db)
	sql_cmd = " INSERT INTO "
	table_name = "note_box"
	table_cons = " VALUES (?, ?, ?, ?, ?, ?)"			
	sql_query = sql_cmd + table_name + table_cons
	insert_tables(conn, sql_query, note_box)

	# read data from note box table
	conn = create_connection(atm_sqlite_db)
	sql_cmd = " SELECT * FROM "
	table_name = "note_box"
	table_cons = " "
	sql_query = sql_cmd + table_name + table_cons
	usr_data = select_table(conn, sql_query)
	print(note_box)





	##### initialize users transaction tables table ######
	# create user transaction table	
	for rec in user_list:
		name = rec[1]
		conn = create_connection(atm_sqlite_db)			
		sql_cmd = " CREATE TABLE IF NOT EXISTS "
		print(name)
		table_name = f'{name}' + '_transaction'
		table_cons = """ (
					trans_date text,
					trans_amm int
					);"""
		sql_query = sql_cmd + table_name + table_cons
		create_table(conn, sql_query)

	# insert data to user transaction table
	for rec in user_list:
		name = rec[1]		
		conn = create_connection(atm_sqlite_db)
		sql_cmd = " INSERT INTO "
		table_name = f'{name}' + '_transaction'
		table_cons = " VALUES (?, ?)"			
		sql_query = sql_cmd + table_name + table_cons
		insert_tables(conn, sql_query, user_trans)	
	

	# read data from user transaction table
	for rec in user_list:
		name = rec[1]
		conn = create_connection(atm_sqlite_db)
		sql_cmd = " SELECT * FROM "
		table_name = f'{name}' + '_transaction'
		table_cons = " "
		sql_query = sql_cmd + table_name + table_cons
		usr_data = select_table(conn, sql_query)
		print(usr_data)

	


	


	

