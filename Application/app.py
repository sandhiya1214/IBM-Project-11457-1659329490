from routes import auth, dashboard  # , expenses, budgets, categories, reports, account
import db
from flask import Flask, render_template, redirect
from helpers import login_required, rupees, percent

import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")

# Custom filter
app.jinja_env.filters["rupees"] = rupees
app.jinja_env.filters["percent"] = percent


@app.route("/")
@login_required
def index():
    return redirect("/dashboard")


@app.route("/design")
def design():
    return render_template("view_payer.html", page="reports")


@app.errorhandler(404)
def not_found():
    return redirect("/dashboard")


db.init_app(app)
app.register_blueprint(auth.bp)
app.register_blueprint(dashboard.bp)
# app.register_blueprint(expenses.bp)
# app.register_blueprint(budgets.bp)
# app.register_blueprint(categories.bp)
# app.register_blueprint(reports.bp)
# app.register_blueprint(account.bp)
