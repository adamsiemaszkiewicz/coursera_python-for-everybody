text = "X-DSPAM-Confidence:    0.8475";
# find position of colom
colpos = text.find(':')
# extract number
num = text[colpos+1:]
# clear whitespace
num = num.strip()
# convert to float
num = float(num)
# print number
print(num)
