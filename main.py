# import sqlite3 as sq
#
# with sq.connect("aircrafts.db") as con:
#     cur = con.cursor()
#     cur.execute("""
#     CREATE TABLE IF NOT EXISTS aircrafts (
#         avion_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         model TEXT,
#         year INTEGER,
#         author TEXT
#     )
#     """)
#
#     cur.execute("INSERT INTO aircrafts VALUES(1, '������ ���������', 1910, '�.�. ��������')")
#     cur.execute("INSERT INTO aircrafts VALUES(2, '�������-VIII', 1912, '�.�. �������')")
#     cur.execute("INSERT INTO aircrafts VALUES(3, '�-6�', 1912, '�.�. ���������')")
#     cur.execute("INSERT INTO aircrafts VALUES(4, '������� ������', 1913, '�.�. ���������')")
#     cur.execute("INSERT INTO aircrafts VALUES(5, '������-12', 1915, '�.�. �������')")


# import os
#
# from mod.database import DATABASE_NAME
# import create_database as db_creator
#
# if __name__ == '__main__':
#     db_is_created = os.path.exists(DATABASE_NAME)
#     if not db_is_created:
#         db_creator.create_database()

import os

from mod.database import DATABASE_NAME
import create_database as db_creator

if __name__ == '__main__':
    db_is_created = os.path.exists(DATABASE_NAME)
    if not db_is_created:
        db_creator.create_database()

