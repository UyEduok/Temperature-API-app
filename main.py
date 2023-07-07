from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

# Read the stations data
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
    # Render the home.html template with the new_stations DataFrame converted to HTML
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


@app.route('/api/v1/<station_id>/')
def all_years(station_id):
    # Generate the file path based on the station_id
    path = 'data/TG_STAID' + str(station_id).zfill(6) + '.txt'

    # Read the CSV file into a DataFrame
    df = pd.read_csv(path, skiprows=20, parse_dates=['    DATE'])

    # Convert the DataFrame to a dictionary
    result = df.to_dict(orient='records')
    return result


@app.route('/api/v1/annually/<station_id>/<year>/')
def yearly(station_id, year):
    # Generate the file path based on the station_id
    path = 'data/TG_STAID' + str(station_id).zfill(6) + '.txt'

    # Read the CSV file into a DataFrame
    df = pd.read_csv(path, skiprows=20)

    # Convert the 'DATE' column to string for filtering
    df['    DATE'] = df['    DATE'].astype(str)

    # Filter the DataFrame based on the year and retrieve the data
    result = df[df['    DATE'].str.startswith(str(year))]
    result = result.to_dict(orient='records')
    return result


if __name__ == '__main__':
    # Run the Flask app in debug mode on port 5001
    app.run(debug=True, port=5001)
