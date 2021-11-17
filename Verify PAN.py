import re
s = "ABCDE1234A"
r = re.compile("^[A-Z]{5}[0-9]{4}[A-Z]$")
p = re.findall(r, s)
print("Valid PAN", p)
