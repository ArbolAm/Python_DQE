import sqlite3


city_data = [
    ('moscow', 55.7558, 37.6173),
    ('new york', 40.7128, -74.0060),
    ('los angeles', 34.0522, -118.2437),
    ('chicago', 41.8781, -87.6298),
    ('houston', 29.7604, -95.3698),
    ('phoenix', 33.4484, -112.0740),
    ('philadelphia', 39.9526, -75.1652),
    ('san antonio', 29.4241, -98.4936),
    ('san diego', 32.7157, -117.1611),
    ('dallas', 32.7767, -96.7970),
    ('san jose', 37.7749, -122.4194),
    ('austin', 30.2672, -97.7431),
    ('jacksonville', 30.3322, -81.6557),
    ('fort worth', 32.7555, -97.3308),
    ('columbus', 39.9612, -82.9988),
    ('indianapolis', 39.7684, -86.1580),
    ('charlotte', 35.2271, -80.8431),
    ('seattle', 47.6062, -122.3321),
    ('denver', 39.7392, -104.9903),
    ('washington', 38.9072, -77.0369),
    ('boston', 42.3601, -71.0589),
    ('el paso', 31.7619, -106.4850),
    ('nashville', 36.1627, -86.7816),
    ('detroit', 42.3314, -83.0458),
    ('memphis', 35.1495, -90.0490),
    ('portland', 45.5051, -122.6750),
    ('oklahoma city', 35.4676, -97.5164),
    ('las vegas', 36.1699, -115.1398),
    ('louisville', 38.2527, -85.7585),
    ('baltimore', 39.2904, -76.6122),
    ('milwaukee', 43.0389, -87.9065),
    ('albuquerque', 35.0841, -106.6504),
    ('tucson', 32.2226, -110.9747),
    ('fresno', 36.7378, -119.7871),
    ('sacramento', 38.5816, -121.4944),
    ('kansas city', 39.0997, -94.5786),
    ('long beach', 33.7683, -118.1950),
    ('mesa', 33.4152, -111.8315),
    ('atlanta', 33.7490, -84.3880),
    ('colorado springs', 38.8339, -104.8214),
    ('raleigh', 35.7796, -78.6382),
    ('miami', 25.7617, -80.1918),
    ('omaha', 41.2565, -95.9345),
    ('oakland', 37.8044, -122.2711),
    ('minneapolis', 44.9778, -93.2650),
    ('tulsa', 36.1539, -95.9928),
    ('arlington', 32.7357, -97.1081),
    ('new orleans', 29.9511, -90.0715),
    ('wichita', 37.6872, -97.3301),
    ('cleveland', 41.4993, -81.6944),
    ('bakersfield', 35.3733, -119.0187),
    ('aurora', 39.7296, -104.8319)
]

DATABASE = 'city_coordinates.db'


def create_db():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS cities
                 (name TEXT PRIMARY KEY, latitude REAL, longitude REAL)''')
    conn.commit()
    conn.close()


# Generating the SQL Insert Statements
def city_ingestion():
    try:

        conn = sqlite3.connect(DATABASE)
        c = conn.cursor()
        for city, lat, lon in city_data:
            c.execute('INSERT INTO cities (name, latitude, longitude) VALUES (?, ?, ?)',
                      (city.lower(), lat, lon))
        conn.commit()
        conn.close()

        return 'success'

    except:

        return 'fail'


def retrieve_cities():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('SELECT * FROM cities')
    rows = c.fetchall()

    for row in rows:
        print(f"City: {row[0]}, Latitude: {row[1]}, Longitude: {row[2]}")

    conn.close()


def main():

    create_db()
    # city_ingestion()
    retrieve_cities()


if __name__ == "__main__":
    main()
