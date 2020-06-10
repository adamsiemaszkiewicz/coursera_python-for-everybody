# Import regex module
import re
# Prompt for a filename
filename = input("Enter the filename: ")
# If none specified used the default file
if len(filename) < 1 : filename = 'regex_sum_639259.txt'
# Create a file handler
filehandler = open(filename)
# Read the content of the file
content = filehandler.read()
# Extract all numbers in the content
numbers = re.findall('[0-9]+', content)
# Initiate the sum variable
sum = 0
# Run a loop throughout the numbers
for n in numbers :
    # Convert numbers into integers
    n = int(n)
    # Sum up the number
    sum = sum + n
# Print overall sum
print(sum)
