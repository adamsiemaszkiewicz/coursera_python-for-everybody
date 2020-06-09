# Prompt for a file name
filename = input("Enter file name: ")
# Use default file when no input
if len(filename) < 1 : filename = "mbox-short.txt"
# Create a file handler
filehandler = open(filename)
count = 0
# Run a for loop throughout the lines of the file
for line in filehandler:
    # Skip lines which don't start with
    if not line.startswith("From ") : continue
    # Split the line into words
    words = line.split()
    # Extract second word as an email address
    email = words[1]
    # Print email address
    print(email)
    # Count number of occurances within the file
    count = count + 1
print("There were", count, "lines in the file with From as the first word")
