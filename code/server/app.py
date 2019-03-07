from flask import Flask
from flask import Markup
from flask import render_template
app = Flask(__name__)

@app.route('/')
def chart():
    labels = ["Jan", "Feb", "Mar", "Apr", "May", "June", "Jul", "Aug"]
    #import from sqlite db
    values = [10,9,8,7,6,4,7,8]
    return render_template('main_chart.html', values=values, labels=labels)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)