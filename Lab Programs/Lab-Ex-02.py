def ends_with_ab(string):
    if string.endswith("ab"):
        return True
    return False

text = input("Enter a string: ")

if ends_with_ab(text):
    print("Accepted")
else:
    print("Rejected")
