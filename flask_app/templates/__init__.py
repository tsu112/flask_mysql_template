# __init__.py
from flask import Flask, redirect, session, request, render_template
app = Flask(__name__)
app.secret_key = "shhhhhh"
