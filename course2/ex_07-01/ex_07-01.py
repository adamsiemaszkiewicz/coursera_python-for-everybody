# Prompt for a filename
fname = input("Enter file name: ")
# Create file gandle
fh = open(fname)
# Read file contents
text = fh.read()
# Convert to all caps
text_caps = text.upper()
# Strip whitespaces
text_final = text_caps.rstrip()
# Print all caps
print(text_final)
