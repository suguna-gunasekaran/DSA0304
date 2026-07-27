sentence = input("Enter sentence: ").split()

if sentence == ["John", "runs"]:
    print("Parse Tree")
    print("""
        S
      /   \\
    NP     VP
    |       |
  John    runs
    """)
else:
    print("Sentence not found in grammar")
