# Import URLLIB library
from urllib.request import urlopen
# Import BeautifulSoup library
from bs4 import BeautifulSoup
# Import SSL library
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Prompt for an URL
url = input('Enter URL - ')
# Use default if none specified
if len(url) < 1 : url = 'http://py4e-data.dr-chuck.net/comments_42.html'
# Read the content of the url
html = urlopen(url, context=ctx).read()
# Parse the code using Beautiful Soup
soup = BeautifulSoup(html, "html.parser")

# Initiate sum variable
sum = 0
# Retrieve all of the anchor tags
spans = soup('span')
# Run a loop throughout the list of spans
for tag in spans:
    # Sum up the integer-converted contents of spans
    sum = sum + int(tag.contents[0])
# Print the overall sum
print(sum)
