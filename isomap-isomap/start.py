import googlemaps

import time
import json
MAPS_KEY = 'AIzaSyCGRGw4ROCRy-A3VOfNYOlDA5L3qj9DQ2o'#AIzaSyDTwPj1UDZ3ghD0qz7cfN-FMgOoJMnby_8'
gmaps = googlemaps.Client(key=MAPS_KEY)
user_location = None
full_address = None
import isochrone
address = "Comsity Moscow"
gmaps_resp = gmaps.geocode(address)
full_address = gmaps_resp[0]['formatted_address']
user_location = gmaps_resp[0]['geometry']['location']
isochrone, filename = isochrone.generate_isochrone_map(full_address, 60, number_of_angles=12)
