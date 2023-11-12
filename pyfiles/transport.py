import requests
import apikeys
import json as js

def generate_token():
    payload={}
    token_url = f"https://api.iq.inrix.com/auth/v1/appToken?appId={apikeys.APP_ID}&hashToken={apikeys.HASH_TOKEN}"
    token_response = requests.request("GET", token_url, data=payload)
    token_json = js.loads(token_response.text)
    return token_json["result"]["token"]

TOKEN = generate_token()

def calcFastestRoute(start_coordinates, dest_coordinates):
    
    payload = {}
    
    url = f"https://api.iq.inrix.com/findRoute?wp_1={start_coordinates}&wp_2={dest_coordinates}&format=json"
    headers = {
        'Authorization': f"Bearer {TOKEN}"
    }
    try:
        response = requests.request("GET", url, headers=headers, data=payload)
    except requests.exceptions.RequestException as e:
        print(e)
    
    response_json = js.loads(response.text) 
        
    # STUDENT WORK: customize route so that it gives the fastest route from start to dest 
    # considering total distance and average speed with consideration to safety fast travel
    # and overall efficiency
    return response_json


def findRouteAPI(start_coordinates, dest_coordinates, route_type):
    url = f"https://api.iq.inrix.com/findRoute?wp_1={start_coordinates}&wp_2={dest_coordinates}&maxAlternates=2&routeType={route_type}&format=json"

    payload = {}

    headers = {
        'Authorization': f'Bearer {TOKEN}'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    route = response.text 
    print("response without apikeys.TOKEN", route)
    # STUDENT WORK: customize route so that it gives the fastest route from start to dest 
    # considering total distance and average speed with consideration to safety fast travel
    # and overall efficiency
    print("findroute: ", route)
    return route

def calcBestRoute(start_coordinates, dest_coordinates):
    fastest_route = findRouteAPI(start_coordinates, dest_coordinates, 0)
    shortest_route = findRouteAPI(start_coordinates, dest_coordinates, 1)

    fR = js.loads(fastest_route)
    sR = js.loads(shortest_route)
    fRTime = []
    fRSpeed = []
    fRDistance = []

    sRTime = []
    sRSpeed = []
    sRDistance = []

    for route in fR['result']['trip']['routes']:
        fRTime.append(route['uncongestedTravelTimeMinutes'])
        fRSpeed.append(route['averageSpeed'])
        fRDistance.append(route['totalDistance'])

    for route in sR['result']['trip']['routes']:
        sRTime.append(route['uncongestedTravelTimeMinutes'])
        sRSpeed.append(route['averageSpeed'])
        sRDistance.append(route['totalDistance'])

if __name__ == "__main__":
    start_coordinates = "37.757386%2C-122.490667"
    dest_coordinates = "37.746138%2C-122.395481"
    
    opt_route = calcBestRoute(start_coordinates, dest_coordinates)


    route = calcFastestRoute(start_coordinates, dest_coordinates)
    print("route: ", route)



