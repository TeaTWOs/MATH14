import mysql.connector
from xlsxwriter import worksheet
from xlsxwriter import workbook
from xlsxwriter.workbook import Workbook
from datetime import date


# ==========================
# export to excel class
# ==========================
class ExportExcel:
    def __init__(self):
        
        # connects to database
        self.conn = mysql.connector.connect(
                    host = '127.0.0.1',
                    user = 'root',
                    passwd = 'emman23',
                    database = 'trial'
                    )
        self.cur = self.conn.cursor()
        self.cur.execute("SELECT * FROM customers")
        res = self.cur.fetchall()
        # print(res)
        
        # creates excel spreadsheet
        self.title = 'TRACE ' + str(date.today()) + '.xlsx'
        self.workbook = Workbook(self.title)
        self.worksheet = self.workbook.add_worksheet()
        
        # writes column names to spreadsheet
        self.worksheet.write('A1', 'ID')
        self.worksheet.write('B1', 'Name')
        self.worksheet.write('C1', 'Age')
        self.worksheet.write('D1', 'Address')
        self.worksheet.write('E1', 'Contact Number')
        self.worksheet.write('F1', 'Time In')
        self.worksheet.write('G1', 'Time Out')
        self.worksheet.write('H1', 'Status')

        # writes values from database down to spreadsheet
        for i, row in enumerate(res, 1):
            for j, value in enumerate(row):
                self.worksheet.write(i, j, value)
        

        self.workbook.close()
        
        # deletes all records from database
        # after exporting to spreadsheet
        # self.delete = "DELETE FROM records"
        # self.cur.execute(self.delete)
        self.conn.commit()
        self.conn.close()
        
        
ExportExcel()
        