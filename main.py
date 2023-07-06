from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/api/v1/<station_id>/<date>/')
def about(station_id, date):
    return {
        station_id: 10,
        date: 'June',
        'temperature': 90
    }


if __name__ == '__main__':
    app.run(debug=True)
