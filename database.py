import mysql.connector
import time

class DataBase:
    def __init__(self, data):
        
        
        
        # creates and connects to database
        self.conn = mysql.connector.connect(
                    host = '127.0.0.1',
                    user = 'root',
                    passwd = 'emman23',
                    database = 'trial'
                    )
        
        self.cur = self.conn.cursor()
        
        # creates table and columns inside database
        self.cur.execute("""CREATE TABLE IF NOT EXISTS customers (
                            id MEDIUMINT NOT NULL AUTO_INCREMENT,
                            PRIMARY KEY (id),
                            name varchar(255),
                            age int,
                            address varchar (255),
                            number text,
                            time_in datetime,
                            time_out datetime,
                            status text)
                            """)
        
        self.dt = time.strftime("%Y-%m-%d %H:%M:%S")
        
        self.cur.execute(f"SELECT name FROM customers WHERE name = '{data[0]}' AND status = 'In'")
        self.res = self.cur.fetchall()
        
        if len(self.res) == 1:
            self.cur.execute(f"UPDATE customers SET time_out = '{self.dt}', status = 'Out'")
            
        else:
            self.cur.execute(f"""INSERT INTO customers (name, age, address, number,
                                 time_in, time_out, status) VALUES 
                                 (%s, %s, %s, %s, '{self.dt}', NULL, 'In')
                                 """, data)

        self.conn.commit()
        self.conn.close()
        
        
d = ('Emman', 21, 'GMA', '09561324385')
DataBase(d)
