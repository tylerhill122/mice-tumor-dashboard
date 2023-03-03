from flask import Flask, render_template, redirect, jsonify
import data

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", data=data)

@app.route("/barchart_data")
def barchart_data():
    return data.barchart()

@app.route("/piechart_data")
def piechart_data():
    return data.pie()

@app.route("/line_data")
def line_data():
    return data.line()

if __name__ == "__main__":
    app.run(debug=True)