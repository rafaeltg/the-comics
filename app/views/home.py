import random
from flask import render_template
from app import app
from ..marvel_api import MarvelApi


@app.route('/')
def index():
    return show_comic('Deadpool')


@app.route('/<name>')
def index_name(name):
    return show_comic(name)


def show_comic(char_name):
    m = MarvelApi()
    char = m.get_character(char_name)

    if char is None:
        return render_template('error.html', name=char_name), 404

    comic = m.get_comic(random.choice(char.comics))
    return render_template('home.html', comic=comic)