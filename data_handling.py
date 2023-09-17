from rider import *
from route import *
from driver import *
import sqlite3

class Database():
	def __init__(self):
		self.open()
	def open(self):
        """Initializes the database"""
        self.conn = sqlite3.connect('database.db')
        self.cur = self.conn.cursor()
        self.cur.execute("""CREATE TABLE IF NOT EXISTS economy (
            drivers INTEGER NOT NULL PRIMARY KEY,
            riders INTEGER NOT NULL DEFAULT 0,
            credits INTEGER NOT NULL DEFAULT 0
        )""")
