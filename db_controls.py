import sqlite3

from flask import g
from app import app


def get_db():
    db = getattr(g, "_database", None)
    if db is None:
        db = g._database = sqlite3.connect("app.db")
        cursor = db.cursor()
        cursor.execute("select * from market2")
        all_data = cursor.fetchall()
        return all_data


def input_db(thing, price):
    db = getattr(g, "_database", None)
    if db is None:
        db = g._database = sqlite3.connect("app.db")
        cursor = db.cursor()
        print(thing)
        cursor.execute(f"""INSERT INTO market2
        (thing, price) VALUES ('{thing}', '{price}')""")
        db.commit()


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, "_database", None)
    if db is not None:
        db.close()
