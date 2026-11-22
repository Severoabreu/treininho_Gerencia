import os
import sqlite3

def get_connection():
<<<<<<< HEAD
    conn = sqlite3.connect("database/banco.db")
    conn.row_factory = sqlite3.Row
    
    return conn

=======
    return sqlite3.connect("./database/loja.db")
>>>>>>> 03817c7958e8d6a2f5777d34bfb4464453074c2f
