import re

text = input("Enter text: ")
pattern = input("Enter pattern: ")

match = re.search(pattern, text)

if match:
    print("Pattern found!")
    print("Matched Text:", match.group())
else:
    print("Pattern not found.")
