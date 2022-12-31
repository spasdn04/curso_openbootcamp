import sqlite3 as sql

class Mi_Base:
    def CreateDB():
        conn = sql.connect('mifichero.db')
        conn.commit()
        conn.close()

    def CreateTable():
        conn = sql.connect('mifichero.db')
        cursor = conn.cursor()
        cursor.execute(
            """CREATE TABLE streamers (
                name text,
                followers integer
                subs integer
                )"""
        )
        conn.commit()
        conn.close()

if __name__=='__main__':
    Mi_Base