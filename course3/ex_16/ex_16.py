# import URLLIB library
import urllib.request, urllib.parse, urllib.error
# import JSON library
import json
# import SSL library
import ssl

# set an empty api key variable
api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

# if api key non-existent use dr-chuck.net
if api_key is False:
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Run a fotever-loop
while True:
    # Prompt for a location name
    address = input('Enter location name: ')
    # Stop if none specified
    if len(address) < 1: break

    # Set a parameter dictionary
    parms = dict()
    # Append address to 'address' key
    parms['address'] = address
    # Append api_key to 'key' key
    if api_key is not False: parms['key'] = api_key
    # Create a final url
    url = serviceurl + urllib.parse.urlencode(parms)

    # Print retrieving monit
    print('Retrieving', url)
    # Create a URL handle
    uh = urllib.request.urlopen(url, context=ctx)
    # Read an decode data from URL handle
    data = uh.read().decode()
    # Print retrieved monit
    print('Retrieved', len(data), 'characters')

    # Load JSON data into js
    try:
        js = json.loads(data)
    except:
        js = None

    # Monit and skip if no data or status not OK
    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    # Print JSON data with indent 4
    print(json.dumps(js, indent=4))

    # Retrieve place ID
    place_id = js['results'][0]['place_id']
    # Print place ID
    print('Place id', place_id)
