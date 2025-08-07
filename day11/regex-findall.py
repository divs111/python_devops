import re
text = "i am calm and i trust the divine plan , divine together"
pattern = r"divine"

find = re.findall(pattern , text)
if find:
    print(f"pattern found {len(find)} times: {find}")
else:
    print("pattern not found")