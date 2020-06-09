# Prompt for a filename
filename = input("Enter file:")
# Use default file when none specified
if len(filename) < 1 : filename = "mbox-short.txt"
# Create a file hander
handle = open(filename)
# Create an empty list
words = list()
# Create an empty dictionary
email_dict = dict()
# Create an email variable
email = 0
# Run a loop throughout the lines of the file
for ln in handle:
    # Split each line into words
    words = ln.split()
    # Skip when a line shorter that 3 words or doesn't start with 'From'
    if len(words) < 3 or words[0] != 'From' : continue
    # Take 2nd word of list, add if non-existing, count +1 if existing
    email_dict[words[1]] = email_dict.get(words[1], 0) + 1
# Initiate variables
bigcount = None
bigword = None
# Run a loop with two variables over items of the dictionary
for key, value in email_dict.items() :
    # If a first iteration or value bigger than current, then set the new values
    if bigcount is None or value > bigcount :
        bigword = key
        bigcount = value
# Print outcomes
print(bigword, bigcount)
