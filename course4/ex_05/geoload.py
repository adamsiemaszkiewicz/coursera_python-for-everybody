# Import URLLIB library
import urllib.request, urllib.parse, urllib.error
# Import HTTP library
import http
# Import SQLITE library
import sqlite3
# Import JSON library
import json
# Import TIME library
import time
# Import SSL library
import ssl
# Import sys library
import sys

# Set api_key variable to empty
api_key = False
# If api_key empty use the default Dr Chuck server
if api_key is False:
    api_key = 42
    serviceurl = "http://py4e-data.dr-chuck.net/json?"
# Else use provided key to fetch google.com JSON
else :
    serviceurl = "https://maps.googleapis.com/maps/api/geocode/json?"

# Additional detail for urllib
# http.client.HTTPConnection.debuglevel = 1

# Establish a connection with the database file or create a new one
conn = sqlite3.connect('geodata.sqlite')
# Create a connection curson with the database file
cur = conn.cursor()

# Create Locations table if doesn't exists with two columns
cur.execute('''
CREATE TABLE IF NOT EXISTS Locations (address TEXT, geodata TEXT)''')

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Create a file handle for a data file
fh = open("where.data")
# Set count variable to 0
count = 0
# Run a loop through the data file entries
for line in fh:
    # If more that 200 entries retireved stop the program and display monit
    if count > 200 :
        print('Retrieved 200 locations, restart to retrieve more')
        break

    # Strip the entry into words and assign it to address variable
    address = line.strip()
    print('')
    # Select geodata enty from Locations table where address is address
    cur.execute("SELECT geodata FROM Locations WHERE address= ?",
        # Set encoded address in place of placeholder
        (memoryview(address.encode()), ))

    try:
        # Fetch a single record from the curson
        data = cur.fetchone()[0]
        # Print out the monit
        print("Found in database ",address)
        # Continue the program
        continue
    except:
        pass

    # Create parameter dictionary
    parms = dict()
    # Set the address as a value of an 'address' key
    parms["address"] = address
    # If api_key not empty set api_key as a value of a 'key' key
    if api_key is not False: parms['key'] = api_key
    # Create an URL combining the service url with encoded parameter-ed suffix
    url = serviceurl + urllib.parse.urlencode(parms)

    # Print which URL is now being retrieved
    print('Retrieving', url)
    # Create an URL handle
    uh = urllib.request.urlopen(url, context=ctx)
    # Read and decode the URL
    data = uh.read().decode()
    # Print out retrieved data length and a snippet
    print('Retrieved', len(data), 'characters', data[:20].replace('\n', ' '))
    # Add iteration count
    count = count + 1

    # Load JSON data
    try:
        js = json.loads(data)
    except:
        # skip and print in case unicode causes an error
        print(data)
        continue

    # If status is not OK print failure monit, print data and stop the program
    if 'status' not in js or (js['status'] != 'OK' and js['status'] != 'ZERO_RESULTS') :
        print('==== Failure To Retrieve ====')
        print(data)
        break

    # Insert retrieved and encoded data into Locations table
    cur.execute('''INSERT INTO Locations (address, geodata)
            VALUES ( ?, ? )''', (memoryview(address.encode()), memoryview(data.encode()) ) )
    # Commit data
    conn.commit()
    # Put the program to 5-seconds sleep each 10th iteration
    if count % 10 == 0 :
        print('Pausing for a bit...')
        time.sleep(5)

print("Run geodump.py to read the data from the database so you can vizualize it on a map.")
