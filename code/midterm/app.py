from flask import Flask
from flask import Markup
from flask import render_template
import sqlite3
app = Flask(__name__)

@app.route('/')
def chart():
    #import from sqlite db
    #blink_module.collectData()
    db = sqlite3.connect('../../log/motions.db')
    cursor = db.cursor()
    cursor.execute('''SELECT time, motion FROM recorded''')
    motion_readings = []
    times = []
    for row in cursor:
        time_elapsed = row[0]
        #raw_temperature = row[1]
        #print('{0}'.format(raw_temperature[0:4]))
#        motion_readings.append(row[1]))
        times.append(time_elapsed)
    db.close()
    return render_template('main_chart.html', values=motion_readings, labels=times)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
