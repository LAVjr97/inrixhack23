import requests
import pyfiles.apikey as apikey

def calcFastestRoute(start_coordinates, dest_coordinates):
    url = f"https://api.iq.inrix.com/findRoute?wp_1={start_coordinates}&wp_2={dest_coordinates}&format=json"

    payload = {}
    headers = {
        'Authorization': f'Bearer {apikey.TOKEN}'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    route = response.text
    # STUDENT WORK: customize route so that it gives the fastest route from start to dest 
    # considering total distance and average speed with consideration to safety fast travel
    # and overall efficiency
    return route

if __name__ == "__main__":
    start_coordinates = "37.757386%2C-122.490667"
    dest_coordinates = "37.746138%2C-122.395481"
    route = calcFastestRoute(start_coordinates, dest_coordinates)
    print("route: ", route)