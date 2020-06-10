# Prompt for a name
filename = input("Enter file:")
# Use default file when non specified
if len(filename) < 1 : filename = "mbox-short.txt"
# Create a file handler
handler = open(filename)
# Initiate time list
time = list()
# Initiate hours list
hours = list()
# Initiate hours count dictionary
hours_count = dict()
# Run a loop through lines of file
for ln in handler :
    # Clear right whitespaces in each line
    ln = ln.rstrip()
    # Split lines into words
    words = ln.split()
    # Skip if line does not start with 'From'
    if len(words) < 3 or words[0] != 'From' : continue
    # Add 6th word to 'time' list
    time.append(words[5])
# Run a loop through the time list
for h in time :
    # Split the h,m,s using colon
    hour = h.split(':')
    # Insert values into dictionary and count occurances
    hours_count[hour[0]] = hours_count.get(hour[0], 0) + 1
# Run a loop through sorted items of the dictionary
for k,v in sorted(hours_count.items()) :
    # Print keys and values
    print(k,v)
