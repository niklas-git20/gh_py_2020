# temporary for testing
import sqlite3
from sqlite3 import Error


# read data from note box table
db_file = r"C:\\Users\\Nik\\Desktop\\gh_py_2020\\HT_13_atm\\atmsqlite.db"
conn = sqlite3.connect(db_file)
curs = conn.cursor()
sql_cmd = " SELECT * FROM "
table_name = 'note_box'
table_cons = " "
sql_query = sql_cmd + table_name + table_cons
curs.execute(sql_query)
rd = curs.fetchone()
# nominal value rd type: tuple --> list
val_list = (list(rd))
# nominal names type: list
nom_list = list(map(lambda x: x[0], curs.description))
# using dictionary comprehension 
# to convert lists to dictionary 
note_data = {nom_list[i]: val_list[i] for i in range(len(nom_list))}
#commit the changes to db			
conn.commit()
#close the connection
conn.close()

print(nom_list)
print(val_list)
print(note_data)


# split dictionary into keys and values 
# keys = note_data.keys() 
# values = note_data.values() 
# split dictionary into keys and values 
keys, values = zip(*note_data.items()) 

print(keys)
print(values)

a,b,c,d,e,f = 1,2,3,4,5,6

table_data = (f" SET '50' = {a}, '20' = {b},'10' = {c},"
			f"'5' = {d}, '2' = {e}, '1' = {f} ")	
print(table_data)