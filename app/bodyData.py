import sqlite3

# MAKE CONNECTION TO DATABASE
con = sqlite3.connect("body.db")
print("Opened database successfully")

con.execute('''CREATE TABLE IF NOT EXISTS HEALTH_DATA
    (DATE             DATETIME     NOT NULL,
    USER_ID           STRING    NOT NULL,
    
    PRIMARY KEY (DATE, USER_ID))''')

print("Table created successfully")

con.close()