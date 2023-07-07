from flask import Flask, render_template
import pandas as pd
from collections import OrderedDict

app = Flask(__name__)

stations = pd.read_csv('data/stations.txt', skiprows=17)

# Create a new DataFrame with desired column names
new_columns = ['Station Id', 'Station Name']
new_stations = pd.DataFrame(columns=new_columns)

# Assign values from 'stations' DataFrame to 'new_stations' DataFrame
new_stations[['Station Id',
              'Station Name']] = \
    stations[['STAID',
              'STANAME                                 ']]
new_stations = new_stations[:92]


@app.route('/')
def home():
    return render_template('home.html', data=new_stations.to_html())


@app.route('/api/v1/<station_id>/<date>/')
def about(station_id, date):
    # Generate the file path based on the station_id
    path = 'data/TG_STAID' + str(station_id).zfill(6) + '.txt'

    # Read the CSV file into a DataFrame
    df = pd.read_csv(path, skiprows=20, parse_dates=['    DATE'])

    # Filter the DataFrame based on the date and retrieve the temperature
    temp = df.loc[df['    DATE'] == date]['   TG'].squeeze() / 10

    # Return a JSON response with the station_id, date, and temperature
    return {'StationId': station_id,
            'Date': date,
            'Temperature': temp
            }


if __name__ == '__main__':
    # Run the Flask app in debug mode on port 5001
    app.run(debug=True, port=5001)
