
string = "56 57 5657 I love Python"

print(*re.findall(r"\d{1,3}",string))