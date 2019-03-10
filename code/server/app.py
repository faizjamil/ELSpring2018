from flask import Flask
from flask import Markup
from flask import render_template
import sqlite3
app = Flask(__name__)

@app.route('/')
def chart():
    #import from sqlite db
    db = sqlite3.connect('../../log/temperatures.db')
    cursor = db.cursor()
    cursor.execute('''SELECT temperature FROM recorded''')
    values = []
    for row in cursor:
        raw_temperature = row[0]
        #print('{0}'.format(raw_temperature[0:4]))
        values.append(float(raw_temperature[0:4]))
    #labels = ["Jan", "Feb", "Mar", "Apr", "May", "June", "Jul", "Aug"]
    return render_template('main_chart.html', values=values)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)