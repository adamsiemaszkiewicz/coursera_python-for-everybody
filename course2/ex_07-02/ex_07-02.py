# Prompt for filename
filename = input("Enter file name: ")
# Create a file handler
filehandler = open(filename)
# Create zero variables for the loop
overall = 0
count = 0
# Run a for loop throughout filehandler
for line in filehandler:
    # Skip lines which don't start with
    if not line.startswith("X-DSPAM-Confidence:") : continue
    # Find position of colon
    colon_position=line.find(':')
    # Extract number from line
    number = line[colon_position+1:]
    # Strip whitespaces and covert to float
    number = float(number.strip())
    # Sum outcomes
    overall = overall + number
    # Sum number of elements
    count = count + 1
# Count average
average = overall/count
# Print average
print('Average spam confidence:', average)
