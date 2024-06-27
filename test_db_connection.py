import MySQLdb

try:
    db = MySQLdb.connect(
        host="localhost",
        user="root",
        passwd="",
        db="arka_test_db"
    )
    print("Connection successful")
    db.close()
except MySQLdb.Error as e:
    print(f"Error: {e}")
