# OpenStreetMap-flask-example
* This project is a simple example of how to use OpenStreetMap with Flask.
  
## Installation

```bash
git clone https://github.com/MucahidAydin/OpenStreetMap-flask-example.git
cd OpenStreetMap-flask-example
pip install -r requirements.txt
```
## Usage
To run the application, use the following command:
```bash
flask run
```
Once the application is running, open the following URL in your browser, replacing `<longitude>`, `<latitude>` and `<zoom_level>` with your desired values:
```
http://127.0.0.1:5000/geo/location?center_x=41.0082&center_y=28.9784&zoom=10
```