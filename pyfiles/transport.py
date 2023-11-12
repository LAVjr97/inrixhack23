import requests
import apikeys
import json as js

def calcFastestRoute(start_coordinates, dest_coordinates):
    
    payload = {}
    token_url = f"https://api.iq.inrix.com/auth/v1/appToken?appId={apikeys.APP_ID}&hashToken={apikeys.HASH_TOKEN}"
    token_response = requests.request("GET", token_url, data=payload)
    token_json = js.loads(token_response.text)
    apikeys.TOKEN = token_json["result"]["token"]
    url = f"https://api.iq.inrix.com/findRoute?wp_1=37.770581%2C-122.442550&wp_2=37.765297%2C-122.442527&format=json"
    headers = {
        'Authorization': apikeys.TOKEN
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
<<<<<<< Updated upstream
        'Authorization': f'Bearer {apikeys.TOKEN}'
=======
        'Authorization': f'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhcHBJZCI6Imxlamd5NzNhMTQiLCJ0b2tlbiI6eyJpdiI6IjVhZTA0OGZlYTVkMjU3ZmQ0MTdjMTIyYjNiZGU0MmRkIiwiY29udGVudCI6IjNmZTRlYTYzZjE3NjdjYTgwZjVkNzVlZjUwNTJmZWU0YTVkOGQ5Y2E3YjAyMDY3MGEwZGUyY2JkMWRkMjYzNTUwMjMwNzgwNWYwOTVjMzg5YzFiNTExYzlkNmUzODQzZWE1YjFkMTFmOGM1OWUyMjJjYTZmYzVlYjA3N2JlODYxYzdhNWY2ZGY2NDMzYzM4OTA1ZWYwNTE4MGQxOWY2OTU2NTk5MmMxZjZlZTMxNTJiZGUxMWVkM2U2OWFmOGRmMzhkMzU0OTIzNjE3MDlhYWVlYzFlOThiNzY2MWUzM2FiOGI2MzhiNDZmM2RmYjgzMTExNGY4MThmYmU5YWUwYmQwMmE4MDMzYTk0MTI3NWM2OTg4YzQ0MzM2ZTIwZTFmMmFkYzMzZDMyYmUyMzZkZTA0ZTk5Y2E0ZWJhZDY3NDVjMDBhMjIzYjgxZWRmN2NmODdlMmQzOTk1ZmM3YjNlNzlmZTBlNmVhYzAwMjM2ZmMzMTAwZjVjMzhhODAyY2JlYjk1MWQ3ODcxNTkyYjE2ZDRjN2E5NTlhZTExNWI1ZjYwY2E1NDgxMTdiZWNhZGVkYzAwMmJjYjg5MzI5ZGFkYWY3YjZlMDFiNzdiODNmNWQ2NDZmNTg1ZGJkNTc0Nzk5MjU4NWM1ZjMwMDU1MzRiNWUxNjM5ZTc3Mzk1ZGJhYjEzZTI3MzQ2NDcxODQ5M2M3MDViYzlmM2ZlZmFiNjlhYzIwMDg5MGQ5MTcxZTRiNzQzYTg3YmE3NmI5Y2VjNTY2MGQxOWQ3ZWM0M2I1Yjg4ZTM4OWZiMGUzNDEzMGIxOGVkOGFlYmIxMGVjMWQ2MWE4NTg1YWJmMzE4ZmJkNWUxMGUyZTJjNmZjMDk4YzU3NGYyZWNmNjhiIn0sInNlY3VyaXR5VG9rZW4iOnsiaXYiOiI1YWUwNDhmZWE1ZDI1N2ZkNDE3YzEyMmIzYmRlNDJkZCIsImNvbnRlbnQiOiIwZmQ0Y2E0NmQxNDk3NmYwMzM3MDc3ZGU1MjQxODY5MWEzZTFlOGNjNDgxNjNhMmRmYWNmMWZiOTZkZWYyNDNjNjMwNTY4MDhiNThhOGU4YWZhOWY2ZGY3In0sImp0aSI6ImU5ZjZmZDI3LTA2ZmYtNDg1Yy04ZGQzLWM2ZDZjOWUyODBlZiIsImlhdCI6MTY5OTc2NzY4OCwiZXhwIjoxNjk5NzcxMjg4fQ.o-bTHznRxi2NZrLIjHDgSnY3wxapK_NDWDqhk1skF3g'
>>>>>>> Stashed changes
    }
    

    response = requests.request("GET", url, headers=headers, data=payload)

    route = response.text 
    # STUDENT WORK: customize route so that it gives the fastest route from start to dest 
    # considering total distance and average speed with consideration to safety fast travel
    # and overall efficiency
    return route

<<<<<<< Updated upstream
def calcBestRoute(start_coordinates, dest_coordinates):
    fastest_route = findRouteAPI(start_coordinates, dest_coordinates, 0)
    shortest_route = findRouteAPI(start_coordinates, dest_coordinates, 1)
=======
def calcBestRoute(fastest_route, shortest_route):
    #for route in fastest_route[]:
    return 1
>>>>>>> Stashed changes

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

    for route in fR['result']['trip']['routes']:
        sRTime.append(route['uncongestedTravelTimeMinutes'])
        sRSpeed.append(route['averageSpeed'])
        sRDistance.append(route['totalDistance'])
    
    if():

if __name__ == "__main__":
    start_coordinates = "37.757386%2C-122.490667"
    dest_coordinates = "37.746138%2C-122.395481"
    
    opt_route = calcBestRoute(start_coordinates, dest_coordinates)



    #route = calcFastestRoute()
    #print("route: ", route)



