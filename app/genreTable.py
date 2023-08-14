import sqlite3

# MAKE CONNECTION TO DATABASE
con = sqlite3.connect("out.db")
print("Opened database successfully")

con.execute('''CREATE TABLE IF NOT EXISTS HEALTH_DATA
    (DATE             DATETIME     NOT NULL,
    USER_ID           STRING    NOT NULL,
    GENRE             STRING    NOT NULL,
    PRIMARY KEY (DATE, USER_ID))''')

print("Table created successfully")