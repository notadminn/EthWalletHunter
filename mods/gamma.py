import sqlite3

def uhb_nmk():
    """Initialize the database and table efficiently"""
    fizz = sqlite3.connect("zyx_iku.zyga")
    fizz.execute('''
        CREATE TABLE IF NOT EXISTS mzz (
            qid INTEGER PRIMARY KEY AUTOINCREMENT,
            f0 TEXT NOT NULL,
            f1 TEXT NOT NULL,
            f2 TEXT NOT NULL
        )
    ''')
    fizz.commit()
    fizz.close()

def bop_waz(pepper_salt_sugar_list):
    """Optimized Insert with Batch Processing"""
    jar = sqlite3.connect("zyx_iku.zyga")
    cursor = jar.cursor()

    # Insert data in bulk using executemany
    cursor.executemany("INSERT INTO mzz (f0, f1, f2) VALUES (?, ?, ?)", pepper_salt_sugar_list)

    # Commit the transaction in bulk after inserting all records
    jar.commit()
    jar.close()
