#! /usr/env/python3
# oc_tax_parse.py
#
# Author:		David McLaren
# Description:	Converts Orange County's Tax Assesment Data into a SQLite
#				database for easy querying.
# ------------------------------------------------------------------------------
import sqlite3

# Global Variables
DB_NAME = 'oc_tax_info.db'
TABLE_SQL = 'oc_tax_assessment.sql'
FILE_LIST = [
				'G:\Tax Assesment\AT04BB01.FILE1.TXT',
				'G:\Tax Assesment\AT04BB01.FILE2.TXT',
				'G:\Tax Assesment\AT04BB01.FILE3.TXT',
				'G:\Tax Assesment\AT04BB01.FILE4.TXT',
				'G:\Tax Assesment\AT04BB01.FILE5.TXT',
				'G:\Tax Assesment\AT04BB01.FILE6.TXT',
				'G:\Tax Assesment\AT04BB01.FILE7.TXT',
				'G:\Tax Assesment\AT04BB01.FILE8.TXT',
				'G:\Tax Assesment\AT04BB01.FILE9.TXT',
				'G:\Tax Assesment\AT04BB01.FILE10.TXT',
				'G:\Tax Assesment\AT04BB01.FILE11.TXT',
				'G:\Tax Assesment\AT04BB01.FILE12.TXT',
				'G:\Tax Assesment\AT04BB01.FILE13.TXT',
				'G:\Tax Assesment\AT04BB01.FILE14.TXT',
				'G:\Tax Assesment\AT04BB01.FILE15.TXT'
			]

TEST_LIST = [
				'TEST.TXT'
			]

class OC_Tax_Interface(object):
	"""docstring for OC_Tax_Interface"""
	def __init__(self, db_name, table_sql, file_list):
		super(OC_Tax_Interface, self).__init__()
		self.db_name = db_name
		self.table_sql = table_sql
		self.file_list = file_list

		self.create_table()
		self.digest_records(self.file_list)


	def digest_records(self, file_list):
		index = 0

		conn = sqlite3.connect(self.db_name)
		curs = conn.cursor()

		for file_name in file_list:
			index += 1
			print('Opening File', index)

			with open(file_name, 'r') as in_file:
				for line in in_file:
					district 		= line[0:4]
					tax_rate_area 	= int(line[4:9])
					parcel_number 	= int(line[9:17])

					if (line[19:24].isdigit()):
						addr_zip 		= int(line[19:24])
					else:
						addr_zip = 0

					if (line[25:29].isdigit()):
						addr_zip4		= int(line[25:29])
					else:
						addr_zip4 = 0

					addr_01			= line[29:54].rstrip()
					addr_02			= line[54:79].rstrip()
					addr_03			= line[104:129].rstrip()
					addr_04			= line[129:154].rstrip()
					addr_05			= line[154:179].rstrip()
					addr_06			= line[179:204].rstrip()
					num 			= int(line[-2:-1])
					# line[-1:] is '\n'

					record = (district, tax_rate_area, parcel_number, addr_zip,
							  addr_zip4, addr_01, addr_02, addr_03, addr_04,
							  addr_05, addr_06, num)
					
					curs.execute('INSERT INTO oc_tax_info VALUES (?,?,?,?,?,?,?,?,?,?,?,?)', record)

		conn.commit()
		conn.close()


	def create_table(self):
		conn = sqlite3.connect(self.db_name)
		curs = conn.cursor()

		# Create Table
		with open(self.table_sql, 'r') as sql_file:
			sql = sql_file.read()
			curs.executescript(sql)
			conn.commit()

		conn.close()

def main():
	inteface = OC_Tax_Interface(DB_NAME, TABLE_SQL, TEST_LIST)


if __name__ == '__main__':
	main()
