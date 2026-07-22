def plural(noun):
    if noun.endswith(("s", "x", "z", "ch", "sh")):
        return noun + "es"
    else:
        return noun + "s"

word = input("Enter a noun: ")

print("Plural Form:", plural(word))
