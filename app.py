from flask import Flask, render_template, request, redirect, url_for
import logging
from app_route.add_dev import create_dev
from app_route.add_engine import create_engine
from app_route.add_game import get_options, create_game
from app_route.delete import delete_game
from app_route.home import get_home
from app_route.update import update_game, get_update_data
from create_engine import engine, table_uri
from sqlalchemy_db import db


logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = table_uri
db.init_app(app)


@app.route('/')
def home():

    (games_by_developer, games, developers)=get_home(engine, db)
    return render_template("index.html", games=games, developers=developers, df=games_by_developer)


@app.route("/add_game", methods=["GET", "POST"])
def add_game():
    if request.method == "POST":
        # CREATE RECORD
        create_game(db)
        return redirect(url_for('home'))

    (developers, engines) = get_options(db)
    return render_template("add_game.html", developers=developers, engines=engines)


@app.route("/add_dev", methods=["GET", "POST"])
def add_dev():
    if request.method == "POST":
        # CREATE RECORD
        create_dev(db)
        return redirect(url_for('home'))
    return render_template("add_dev.html")


@app.route("/add_engine", methods=["GET", "POST"])
def add_engine():
    if request.method == "POST":
        # CREATE RECORD
        create_engine(db)
        return redirect(url_for('home'))
    return render_template("add_engine.html")


@app.route("/update", methods=["GET", "POST"])
def update():

    if request.method == "POST":
        update_game(db)
        return redirect(url_for('home'))
    #GETS DATA FOR THE SPECIFIC GAME TO SHOW BY DEFAULT IN THE HTML INPUT
    (game_selected, developers, engines) = get_update_data(db)
    return render_template("update.html", game=game_selected, developers=developers, engines=engines)


@app.route("/delete")
def delete():
    # DELETE RECORD
    delete_game(db)
    return redirect(url_for('home'))


if __name__ == "__main__":
    app.run(host='localhost', port=3000, debug=True)
