# Regular expressions for extracting email ids

import re
text = """
  hello i want to share this message to these email address - sonidivya157@gmail.com , soni_12@yahoo.com  and   soni_$@gmail.com

"""

list_of_emails=re.findall("[a-z0-9.$_]+@+[a-z0-9]+.[a-z]+",text)
print(list_of_emails)