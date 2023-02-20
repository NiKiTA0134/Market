import sqlite3

connection = sqlite3.connect("app.db")
cursor = connection.cursor()
print("Db created!")
cursor.execute("create table market2 (id INTEGER PRIMARY KEY AUTOINCREMENT, thing TEXT, price TEXT)")
print("Table created")
connection.close()


# import sqlite3
#
# connection = sqlite3.connect("app.db")
# cursor = connection.cursor()
#
# cursor.execute("create table groceries (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT)")
#
# groceries = [
#     "Apples",
#     "Bananas",
#     "Strawberries",
#     "Avocados",
#     "Bell Peppers",
#     "Carrots",
#     "Broccoli",
#     "Garlic",
#     "Lemons",
#     "Onion",
#     "Parsley",
#     "Cilantro",
#     "Basil",
#     "Potatoes",
#     "Spinach",
#     "Tomatoes"
# ]
#
# connection.commit()
# connection.close()