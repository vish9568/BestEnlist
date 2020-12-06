import re
string = "Vishal56 Amisha57 c3"

print(*re.findall(r"[0-9]+",string))