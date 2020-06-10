# Import URLLIB library
from urllib.request import urlopen
# Import BeautifulSoup library
from bs4 import BeautifulSoup
# Import SSL library
import ssl
# Import regex
import re

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


# Prompt for an URL
url = input('Enter URL - ')
# Use default if none specified
if len(url) < 1 : url = 'http://py4e-data.dr-chuck.net/known_by_Colleen.html'
# Number of iterations
iterations = 7
# Initiate iteration variable
it = 0
# Run a loop iterations-time
for it in range(iterations):
    # Increase iteration variable with each iteration
    it = it + 1
    # Print current iteration and URL
    print('Iteration:', it, 'Current URL: ', url)
    # Read the content of the url
    html = urlopen(url, context=ctx).read()
    # Parse the code using Beautiful Soup
    soup = BeautifulSoup(html, "html.parser")
    # Retrieve all of the anchor tags
    tags = soup('a')
    # Iniiate position variable
    position = 0
    # Specify order of the link
    order = 18
    for tag in tags:
        # Increase position number with each iteration
        position = position + 1
        # Skip if wrong order number
        if position != order : continue
        # If order right assign a new URL
        new_url=tag.get('href', None)
        # Print next URL
        print('Next URL:', new_url)
    # Assign new URL
    url = new_url
# Extract the name from the URL
final_name = re.findall('by_(\S+).html', new_url)
# Print the final name
print('Final name:', final_name[0])
