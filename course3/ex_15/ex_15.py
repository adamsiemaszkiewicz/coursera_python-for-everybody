# Import URLLIB library
import urllib.request, urllib.parse, urllib.error
# Import JSON library
import json
# Import SSL library
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Prompt for a file location
address = input('Enter file location: ')
# Use the default address if non specified
if len(address) < 1 :
    address='http://py4e-data.dr-chuck.net/comments_639264.json'
# Print address
print('Retrieving ', address)

# Create an URL handle
uh = urllib.request.urlopen(address, context=ctx)
# Read, decode and store JSON contents
data = uh.read().decode()
# Print lendth of the cocument
print ('Retrieved', len(data), 'characters')
# Load JSON-data
j_data = json.loads(data)
# Print JSON_data
# print(json.dumps(j_data, indent=2))

# Initiate sum variable
sum = 0
# Run a loop throughout the JSON data
for person in j_data['comments']:
    # Convert comment number to integer
    comment_no = int(person['count'])
    # Add comment number to overall sum
    sum = sum + comment_no

# Print position count
print('Count: ', len(j_data['comments']))
# Print overall sum
print('Sum: ', sum)
