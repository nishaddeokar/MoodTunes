import sqlite3

# MAKE CONNECTION TO DATABASE
con = sqlite3.connect("sleep.db")
print("Opened database successfully")

con.execute('''CREATE TABLE IF NOT EXISTS HEALTH_DATA
    (DATE             DATETIME     NOT NULL,
    USER_ID           STRING    NOT NULL,
    BPM               INT      NOT NULL,
    OXYGEN_SAT        INT      NOT NULL,
    REM_EVENT_NO      INT      NOT NULL,
    WAKEUP_NO         INT      NOT NULL, 
    SLEEP_EFFICIENCY  FLOAT    NOT NULL,
    PRIMARY KEY (DATE, USER_ID))''')

print("Table created successfully")

con.close()