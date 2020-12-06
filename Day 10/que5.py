import re
string = "VISHAL MANIKRAO Jadhav"

print(*re.findall(r"[A-Z]+",string))