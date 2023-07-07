# Europe Temperature API
The Europe Temperature API provides temperature data for stations in Europe. Users can access the data by inputting the station ID and date or station ID, or station ID and year in the URL.

Endpoints
1. Get Temperature Data by Station ID and Date
Endpoint: /api/v1/<station_id>/<date>/

Returns the temperature data for the specified station and date.

Example: /api/v1/10/2022-07-01/

2. Get Entire Temperature Data for a Station
Endpoint: /api/v1/<station_id>/

Returns the entire temperature data for the specified station.

Example: /api/v1/10/

3. Get Yearly Temperature Data for a Station
Endpoint: /api/v1/annually/<station_id>/<year>/

Returns the yearly temperature data for the specified station and year.

Example: /api/v1/annually/20/2022/

#### Usage
Make a GET request to one of the above endpoints using a web browser, API testing tool, or any HTTP client.
Replace <station_id> with the ID of the desired station (e.g., 56) as displayed in the homepage.
Replace date or year in the url with the desired date or year (e.g., 2022-07-01 or 2022).
#### Installation and Setup
Clone this repository to your local machine.
Install the required dependencies by running pip install -r requirements.txt.
Run the Flask app by executing python app.py.
Access the API endpoints using the provided URLs.
#### Contributing
Contributions to this project are welcome! If you encounter any issues or have suggestions for improvements, please open an issue or submit a pull request.

