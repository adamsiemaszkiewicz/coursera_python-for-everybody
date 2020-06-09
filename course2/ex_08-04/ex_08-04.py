# Prompt for a file name
fname = input("Enter file name: ")
# Create a file handler
filehandler = open(fname)
# Create an empty list
lst = list()
# Run a loop through the file
for line in filehandler:
    # Split each line into words
    words = line.split()
    # Check the number of words in the line
    line_length = len(words)
    # Create the range for the loop
    line_range = range(line_length)
    # Run a loop throughout the words
    for word in line_range:
        # Skip if word already exists in the list
        if words[word] in lst : continue
        # Append word to the list otherwise
        lst.append(words[word])
# Sort the list alphabetically
lst.sort()
# Print the list
print(lst)
