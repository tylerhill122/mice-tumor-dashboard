from flask import Flask, render_template, redirect, jsonify
import data

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", data=data)

@app.route("/barchart_data")
def barchart_data():
    timepoint = data.df['Drug Regimen'].value_counts()
    data_instance = {'drug': [],'value': []}
    for index, value in timepoint.items():
        data_instance['drug'].append(index)
        data_instance['value'].append(value)
    return data_instance

if __name__ == "__main__":
    app.run(debug=True)