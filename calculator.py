from flask import Flask, render_template, template_rendered
from logging import FileHandler,WARNING

Flask_App=Flask(__name__)

@Flask_App.route("/")

def calculate():
    return render_template("index.html",template_folder="template")