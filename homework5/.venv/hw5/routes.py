from flask import render_template, request, redirect, url_for
from hw5 import site

@site.route("/")
def functionname():
    return render_template('filbert.html')

@site.route("/robert")
def robertname():
    return render_template('robert.html')

