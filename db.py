import sqlite3

db = sqlite3.connect("data.db", check_same_thread=False)
db.row_factory = sqlite3.Row
cursor = db.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS products (id INTEGER PRIMARY KEY, name TEXT, price DOUBLE)")

# sequelize, typeorm - Node
# eloquent - PHP
# gorm - Golang
# JPA