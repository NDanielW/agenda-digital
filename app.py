from config import settings
from flask import Flask, abort, render_template, jsonify
from dynaconf import FlaskDynaconf
from flask_admin import Admin
from flask_admin.base import AdminIndexView
from flask_admin.contrib import sqla
from flask_simplelogin import SimpleLogin, login_required
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
FlaskDynaconf(app)
@app.route("/")
def index():
    return render_template("index.html") 

if __name__ == "__main__":
    app.run(debug=True)
