from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route('/')
def index():
  headline = random.choice(["Hello, world!", "Hi there!", "Good             morning!","goede middag"])
	#return render_template('index.html')
  return render_template("index.html", headline=headline)

@app.route("/Jens")

def david():

    return "Hello, Jens!"

@app.route("/<string:name>") 
def hello(name):
    return f"Hello, {name}!"


app.run('0.0.0.0',8080)