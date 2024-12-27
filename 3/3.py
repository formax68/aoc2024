import re

input = "input3.txt"

with open(input, 'r') as file:
    memory = file.read()
    doings = re.split(r'do\(\)', memory)

match = []
for doing in doings:
    match.append(re.split(r"don't\(\)", doing, maxsplit=1)[0])
match_string = ''.join(match)
match_do = re.findall(r'mul\(\d+,\d+\)', match_string)

mul = lambda x, y: x * y
result = 0
for function in match_do:
    x, y = map(int, re.findall(r'\d+', function))
    result += mul(x, y)
print(result)
