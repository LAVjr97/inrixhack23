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

def findRouteAPI(start_coordinates, dest_coordinates, route_type):
    TOKEN = generate_token()

    url = f"https://api.iq.inrix.com/findRoute?wp_1={start_coordinates}&wp_2={dest_coordinates}&maxAlternates=2&routeType={route_type}&format=json"

    payload = {}
    headers = {
        'Authorization': f'Bearer {TOKEN}'
    }

    try:
        response = requests.request("GET", url, headers=headers, data=payload)
    except requests.exceptions.RequestException as e:
        print(e)
    if response.text == "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJhcHBJZCI6Imxlamd5NzNhMTQiLCJ0b2tlbiI6eyJpdiI6ImMzYmJiMDkxNmI2MGM0ODY2Mjc3ZTEyMTlhMmZiNzcyIiwiY29udGVudCI6ImJkOTBlNzI5Njk0MWU5NzM2Y2YzYTg3NTliOWFlMjhhNjYzNzA3OTMyMmMxOWY4NzkyNjE4YTRkOTZlMzA5OWQwNGRiOTIyYjQ5YTY1ZTAzZjdlNmU1NGFhZDRjMDkyZDAwZTYxNDI1YjMwNDgxMDhiNzllN2NhYjQ5NTNhOGQ2M2I2ODIxMzkwYjI4OGM4NDU3Y2VjYmM5YjI2OWEzMTc0YTQyMDdlNTAwMWZjNmQ1NDFlZjdhMGI4MmZhOTNiOTQ2ZWM4Y2Y3MzRkYzljY2QxNGI4Y2NhNDZmY2NiZDNhMTRmZDYzYTFkNzQ1MjJjZGJiZTE0M2M4Mzk4YTM4MjFmOGY5OTI4ZDZhMThkM2RmNzY2OThkZWQ3MDExMDA5Yzc5NmVlZDc5ODc0ZjNkZDY1NmFmZGQxMzhjNTBjODlkNmRlNzUyZTYwMmQyZTEyMjM3Zjk4MGY2NDU0ODNjNGY4MzljNTMwZmEwODRlOTk4MjA3ZTU1OThmODE3ZTYyZDY4M2Y5MTFhZDkzMWY5MGE4N2FjNDIwMzQ2Yzk2MGZkOTE2YTVmMTM5NmExNjZhM2VmZGQ1YWMyMTVlYTc0YjhkOTk2MzYyNWZiZDZhMzQwOGU1YjY2YjQxYTk5YWNjY2I2MGEzNzI2Y2NhZDMwNTRhNWE4MWE3ODc4MTQ4Y2VjOTYzYWZiMDc2MTQ1YmQzMWZlY2RiNGQxMmM5ZTM2ZDViODI3MWQyMjI1ZGRkYThhYTYzOTI3NTY4YzJmZmEwYzNiMzYxOWY0YmY0YTdmODUzYWUzNzA1MjFmY2MxZDdiOWY3NTUyOWRiZWIzYWZhNzQzYjZjODdkNWVjMzljZTI4MWIzODZiNTMyMmE2Y2Y5MTMyMzMyIn0sInNlY3VyaXR5VG9rZW4iOnsiaXYiOiJjM2JiYjA5MTZiNjBjNDg2NjI3N2UxMjE5YTJmYjc3MiIsImNvbnRlbnQiOiJhOWE3ZWUwNjUxNmRiOTViNzBmNzk0NjVhNGE0OWNlYzdkMGEwYmE4MDA5YTk5ZGZjNjQ5OTczZWFlZjI0ZTgzMzFjMjlhMjIwYjk0MGQyMWY5Y2VmODc0In0sImp0aSI6IjhjZjQxNzM4LWZiZTgtNDZjNC04ZWYzLWJkODcwNmFjMzg4NCIsImlhdCI6MTY5OTc3MTEyMSwiZXhwIjoxNjk5Nzc0NzIxfQ.XbVafqw3ZJa0q53K3jB9sjwwTcbsFcYOPBd67qyuqiI":
        print("same")
    else:
        print("Not Same")

    response = requests.request("GET", url, headers=headers, data=payload) 

    route = response.text 

    return route

def calcBestRoute(start_coords_1, start_coords_2, dest_coords_1, dest_coords_2):
    start_coordinates = start_coords_1 + "%2C" + start_coords_2
    dest_coordinates = dest_coords_1 + "%2C" + dest_coords_2
    fastest_route = findRouteAPI(start_coordinates, dest_coordinates, 0)
    shortest_route = findRouteAPI(start_coordinates, dest_coordinates, 1)

    fR = js.loads(fastest_route) 
    sR = js.loads(shortest_route)

    fRTime = [] 
    fRSpeed = [] 
    fRDistance = [] 
    fRSG = [] 

    sRTime = []
    sRSpeed = []
    sRDistance = []
    sRSG = []

    for route in fR['result']['trip']['routes']:
        fRTime.append(route['travelTimeMinutes']) 
        fRSpeed.append(route['averageSpeed']) 
        fRDistance.append(route['totalDistance']) 
        fRSG.append(len(route['summary']['roads']))

    
    for route in sR['result']['trip']['routes']:
        sRTime.append(route['travelTimeMinutes']) 
        sRSpeed.append(route['averageSpeed'])
        sRDistance.append(route['totalDistance'])
        sRSG.append(len(route['summary']['roads'])) 

    # print("frtime: ", fRTime)
    # print("srtime: ", sRTime)
    # print("frspeed: ", fRSpeed)
    # print("srspeed: ", sRSpeed)
    # print("frdistance: ", fRDistance)
    # print("srdistance: ", sRDistance)
    # print("fSG len: ", fRSG)
    # print("sSG len: ", sRSG)

    Index_sRSG = sRSG.index(min(sRSG))

    Index_sRDist = sRDistance.index(min(sRDistance))

    Index_sRTm = sRTime.index(min(sRTime))

    Index_fRSG = fRSG.index(min(fRSG))

    Index_fRDist = fRDistance.index(min(fRDistance))

    oR = []

    if(sRSG[Index_sRSG] <= fRSG[Index_fRSG]):
        if(fRTime[0] + (.2 * sRTime[Index_sRSG]) < sRTime[Index_sRSG]):
            print("fRTime")
            oR = fR['result']['trip']['routes'][0]['summary']['text']
        
        elif(float(fRDistance[Index_fRDist]) + (.4 * float(sRDistance[Index_sRSG])) < float(sRDistance[Index_sRSG])):
            print("fRDistance")
            return  fR['result']['trip']['routes'][Index_sRDist]['summary']['text']

    return sR['result']['trip']['routes'][Index_sRSG]['summary']['text']
    


    
if __name__ == "__main__":
    start_coordinates = "37.7266508%2C-122.4761966"
    dest_coordinates = "37.7689373%2C-122.4278765"#, "37.732906%2C-122.391005"]
    opt_route = []

    #opt_route = calcBestRoute(start_coordinates, dest_coordinates)
    # for dest in dest_coordinates:
    #     if(start_coordinates == dest):
    #         continue
    
    #     opt_route.append(calcBestRoute(start_coordinates, dest))
    #     start_coordinates = dest 
    
    print(opt_route)

