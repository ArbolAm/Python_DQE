import sqlite3
import math

DATABASE = 'city_coordinates.db'


def haversine(lat1, lon1, lat2, lon2):
    R = 6371  # Radius of the Earth in kilometers
    phi1 = math.radians(lat1)
    phi2 = math.radians(lat2)
    delta_phi = math.radians(lat2 - lat1)
    delta_lambda = math.radians(lon2 - lon1)

    a = math.sin(delta_phi / 2) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(delta_lambda / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = R * c  # Distance in kilometers
    return distance


# Function to create or connect to the database
def create_db():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS cities
                 (name TEXT PRIMARY KEY, latitude REAL, longitude REAL)''')
    conn.commit()
    conn.close()


# Function to get city coordinates from the database
def get_coordinates(city):
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('SELECT latitude, longitude FROM cities WHERE name = ?', (city.lower(),))
    result = c.fetchone()
    conn.close()
    return result


# Function to store city coordinates into the database
def store_coordinates(city, lat, lon):
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('INSERT INTO cities (name, latitude, longitude) VALUES (?, ?, ?)',
              (city, lat, lon))
    conn.commit()
    conn.close()


def calculate_distance(city1, city2):
    cords1 = get_coordinates(city1)
    cords2 = get_coordinates(city2)

    if cords1 is None:
        print(f"Coordinates for {city1} not found. Please enter them manually.")
        lat1 = float(input("Enter latitude for " + city1 + ": "))
        lon1 = float(input("Enter longitude for " + city1 + ": "))
        store_coordinates(city1, lat1, lon1)
        cords1 = (lat1, lon1)

    if cords2 is None:
        print(f"Coordinates for {city2} not found. Please enter them manually.")
        lat2 = float(input("Enter latitude for " + city2 + ": "))
        lon2 = float(input("Enter longitude for " + city2 + ": "))
        store_coordinates(city2, lat2, lon2)
        cords2 = (lat2, lon2)

    lat1, lon1 = cords1
    lat2, lon2 = cords2

    distance = haversine(lat1, lon1, lat2, lon2)
    print(
        f"The straight-line distance between {city1} and {city2} is: {distance:.2f} kms")


def main():
    create_db()

    city1 = input("Enter the name of the first city: ")
    city2 = input("Enter the name of the second city: ")

    calculate_distance(city1, city2)


if __name__ == "__main__":
    main()
