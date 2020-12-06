import re
text=input("Enter text")
pattern=re.compile("[a-zA-Z0-9]+")
if pattern.fullmatch(text) is None:
    print("It contains special characters")
else:
    print("It has only certain characters")
