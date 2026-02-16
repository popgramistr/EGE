import re

text = open('Пример 1.txt').read()
print(len(re.findall(r'ро', text)))