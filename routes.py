import sqlite3

from flask import render_template, request, session, redirect
from app import app, db_controls
from app.db_controls import get_db, input_db


@app.route("/")
def index():
    session["all_data"] = get_db()
    return render_template("index.html", all_data=session["all_data"])


@app.route("/add_order", methods=["POST", "GET"])
def add_order():
    thing = request.form["thing"]
    price = request.form["price"]
    # print(request.form)
    input_db(thing, price)
    return redirect("/")


@app.route("/my_orders", methods=["POST", "GET"])
def my_orders():
    return render_template("my_orders.html", all_orders=get_db())


# @app.route("/add_items", methods=["POST"])
# def add_items():
#     session["s_list"].append(request.form["selected"])
#     session.modified = True
#     return render_template("index.html",
#                            all_data=session["all_data"],
#                            s_list=session["s_list"])

# def add_items():
#     all_orders = db_controls.get_db()
#     if request.method == "POST":
#         thing = request.form["thing"]
#         price = request.form["price"]
#         msg = db_controls.add_order(thing, price)
#         return render_template("my_orders.html", all_orders=all_orders, msg=msg)
#     return render_template("my_orders.html", all_orders=all_orders)