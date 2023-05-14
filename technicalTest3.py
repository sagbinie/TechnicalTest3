import googlemaps
from dotenv import load_dotenv
import os
load_dotenv()
API_KEY = os.getenv("API_KEY")

address = '1300 SE Stark Street, Portland, OR 97214'
gmaps = googlemaps.Client(key = API_KEY)
geocode_result = gmaps.geocode(address)
location = geocode_result[0]['geometry']['location']
address_components=geocode_result[0]['address_components']
neighborhood=[address_component for address_component in address_components if 'neighborhood' in address_component['types']][0]["long_name"]

def find_different_neighborhood(address, neighborhood):
    street_number = int(address.split()[0])
    incremented_address = address.replace(str(street_number), str(street_number + 100))
    geocode_result = gmaps.geocode(incremented_address)
    address_components=geocode_result[0]['address_components']
    new_neighborhood = [component for component in address_components if 'neighborhood' in component['types']][0]["long_name"]    
    if new_neighborhood != neighborhood:
        return incremented_address, new_neighborhood
    else:
        return find_different_neighborhood(incremented_address, new_neighborhood)

different_address, different_neighborhood = find_different_neighborhood(address, neighborhood)
print("Address with different neighborhood:", different_address)
print("Different neighborhood:", different_neighborhood)
