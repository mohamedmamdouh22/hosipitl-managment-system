from gui import *
import sqlite3
data=sqlite3.connect('hospital.db')
data.commit()
data.close()

