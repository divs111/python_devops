import re

text = " i am calm and i trust the divine plan , divine together"
pattern = r"trust"

replacement = "totallytrust"

new_text = re.sub(pattern , replacement , text)
print(f"Replaced text is {new_text}")