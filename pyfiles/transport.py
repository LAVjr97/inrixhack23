import requests
import apikeys
import json as js

def calcFastestRoute(start_coordinates, dest_coordinates):
    
    payload = {}
    token_url = f"https://api.iq.inrix.com/auth/v1/appToken?appId={apikeys.APP_ID}&hashToken={apikeys.HASH_TOKEN}"
    token_response = requests.request("GET", token_url, data=payload)
    token_json = js.loads(token_response.text)
    
    url = f"https://api.iq.inrix.com/findRoute?wp_1={start_coordinates}&wp_2={dest_coordinates}&format=json"
    headers = {
        'Authorization': token_json["result"]["token"]
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

if __name__ == "__main__":
    start_coordinates = "37.757386%2C-122.490667"
    dest_coordinates = "37.746138%2C-122.395481"
    route = calcFastestRoute(start_coordinates, dest_coordinates)
    print("route: ", route)