import sqlite3
from datetime import datetime

# ATM functionality classes

class Atm_trans(object):
		"""ATM transaction processing"""
		db_file = r"C:\\Users\\Nik\\Desktop\\gh_py_2020\\atm\\atmsqlite.db"
		def __init__(self, usr_name):
			self.usr_name = usr_name

		def create_connection(self, db_file):
		    """ create a database connection to the SQLite database 
		    specified by db_file"""
		    conn = sqlite3.connect(db_file)    
		    return conn

		def create_trans_table(self, conn, usr_name):
		    """ create a processing table """
		    conn = create_connection(db_file)
		    sql_cmd = " CREATE TABLE IF NOT EXISTS "
			table_name = f"{usr_name}_trans"
			table_cons = """ (
						date text NOT NULL,
						trans int
						);"""
			sql_query = sql_cmd + table_name + table_cons
		    curs = conn.cursor()
		    curs.execute(sql_query)
		    conn.close()

		def select_trans_table(self, conn, usr_name):
		    """ select a data into table """
		    conn = create_connection(db_file)
			sql_cmd = " SELECT * FROM "
			table_name = f"{usr_name}_trans"
			table_cons = " "
			sql_query = sql_cmd + table_name + table_cons			
	        curs = conn.cursor()
	        curs.execute(sql_query)
	        rd = curs.fetchall()
	        conn.commit()
	        [print(d) for d in rd]


	    def insert_table(self, conn, usr_name, trans_sum):
		    """ insert a data into table from """
		    conn = create_connection(db_file)
			sql_cmd = " INSERT INTO "
			table_name = f"{usr_name}_trans"
			table_cons = " VALUES (?, ?)"				
			sql_query = sql_cmd + table_name + table_cons	
			trans_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
			trans_rec = (trans_date, trans_sum)	   
	        curs = conn.cursor()
	        curs.execute(sql_query, trans_rec)
	        conn.commit()
		    