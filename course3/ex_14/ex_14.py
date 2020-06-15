# Import URLLIB library
import urllib.request, urllib.parse, urllib.error
# Import XML library with ET as an alias
import xml.etree.ElementTree as ET
# Import SSL library
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

# If google maps api_key not specified use dr-chuk.net service url
if api_key is False :
    api_key = 42
    serviceurl = 'http://py4e-data.dr-chuck.net/xml?'
else :
    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/xml?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


# Prompt for a file location
address = input('Enter file location: ')
# Use the default address if non specified
if len(address) < 1 :
    address='http://py4e-data.dr-chuck.net/comments_639263.xml'

# Initiate a dictionary to store XML parameters for retrieval
parms = dict()
# Append specified address value into 'address' key
parms['address'] = address
# If api_key exists append the api_key value into 'key' key
if api_key is not False: parms['key'] = api_key
# Combine url from service url and encoded parameters
# url = serviceurl + urllib.parse.urlencode(parms)
# Print Retrieving information
print('Retrieving', address)
# Create an url handle
uh = urllib.request.urlopen(address, context=ctx)

# Read data from XML file
data = uh.read().decode()
# Print length of the retrieved file
print('Retrieved', len(data), 'characters')
# Print decoded XML data
# print('Data:', data.decode())
# Create a tree from XML data
tree = ET.fromstring(data)
# Find all count elements in the entire tree
counts = tree.findall('.//count')
# Print number of elements found
print('Counts:', len(counts))
# Initiate sum variable
sum = 0
# Run a loop throughout elements of counts
for item in counts :
    # Convert strings to integers and sum all elements
    sum = sum + int(item.text)
# Print out the overall sum
print('Sum:', sum)
