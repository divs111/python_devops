import re

text = " i am calm and i trust the divine plan, divine together"
pattern = r"divine"

search = re.search(pattern , text)
if search:
    print(f"pattern found: {search.group()}")
else:
    print(f"pattern not found")