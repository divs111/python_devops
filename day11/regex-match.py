import re

text = "i am calm and i trust the divine plan , divine together"
pattern = r"divine"

match = re.match(pattern , text)
if match:
    print("match found:", match.group())
else:
    print("match not found")