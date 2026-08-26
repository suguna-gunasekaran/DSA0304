import re

def parse_fopc(expression):
    print("Expression:", expression)

    # Find quantifiers
    if "forall" in expression.lower():
        print("Quantifier: Universal (∀)")
    elif "exists" in expression.lower():
        print("Quantifier: Existential (∃)")

    # Find predicates
    predicates = re.findall(r'([A-Za-z]+)\(([^)]*)\)', expression)

    print("Predicates:")
    for name, args in predicates:
        print(" ", name, "->", args.split(","))

    # Logical operators
    for op in ["AND", "OR", "NOT", "IMPLIES"]:
        if op in expression.upper():
            print("Operator:", op)

expr = input("Enter FOPC expression: ")
parse_fopc(expr)
