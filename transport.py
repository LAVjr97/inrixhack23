import requests
import apikey

def calcFastestRoute(start_coordinates, end_coordinates):
    url = f"https://api.iq.inrix.com/findRoute?wp_1={start_coordinates}&wp_2={end_coordinates}&format=json"

    payload = {}
    headers = {
    'Authorization': f'Bearer {apikey.TOKEN}'
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    print(response.text)
    return 1

if __name__ == "__main__":
    calcFastestRoute("37.757386%2C-122.490667","37.765297%2C-122.442527")