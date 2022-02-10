from flask_app.templates import app
from flask import render_template, redirect, request, session, flash
from flask_app.models.burger import Burger


@app.route('/')
def index():
    return redirect('/users')
