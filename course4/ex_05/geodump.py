# Import SQLITE library
import sqlite3
# Import JSON library
import json
# Import codecs library
import codecs

# Establish a connection with the database or create a new database file
conn = sqlite3.connect('geodata.sqlite')
# Create a database cursor
cur = conn.cursor()

# Select all columns from Locations table
cur.execute('SELECT * FROM Locations')
# Create a file handle from JS file with UFT-8 encoding
fhand = codecs.open('where.js', 'w', "utf-8")
# Write the beginning to the file
fhand.write("myData = [\n")

# Set counter to 0
count = 0
# Run a loop through the rows of the database
for row in cur :

    # Decode each row's second position, covert it to strip and assign to data
    data = str(row[1].decode())

    # Load JSON data into js an covert it to string, if fails - skip
    try: js = json.loads(str(data))
    except: continue
    # Skip if status is not OK
    if not('status' in js and js['status'] == 'OK') : continue

    # Set lattitude and longitude from the geodata column
    lat = js["results"][0]["geometry"]["location"]["lat"]
    lng = js["results"][0]["geometry"]["location"]["lng"]
    # Skip if lattitude or longitude empty
    if lat == 0 or lng == 0 : continue

    # Assign formatted address into where variable
    where = js['results'][0]['formatted_address']
    # Clear '
    where = where.replace("'", "")
    try :
        # Print assigned data
        print(where, lat, lng)
        # Add a iteration count
        count = count + 1
        # If not first iteration insert a new line
        if count > 1 : fhand.write(",\n")
        # Create an output strings
        output = "["+str(lat)+","+str(lng)+", '"+where+"']"
        # Write output into the file
        fhand.write(output)
    except:
        continue

# Insert an ending code
fhand.write("\n];\n")
# Close the database connection
cur.close()
# Close the file connection
fhand.close()
# Print out how many records were written into the JS file
print(count, "records written to where.js")
print("Open where.html to view the data in a browser")
