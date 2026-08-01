def porter_stem(word):
    """
    Simplified Porter Stemmer for 'relational', 'relation', 'relate'.
    Rules are applied ONE AFTER ANOTHER (sequential, conditional logic):
      Step 2  -> replaces a derivational suffix with 'ate'
      Step 5a -> removes a silent final 'e'
    The output of Step 2 becomes the input to Step 5a.
    """
    steps = [word]      # keeps a history of the word after each rule
    rule = []            # keeps a history of which rule fired
 
    # ---- Step 2: (m>0) ATIONAL -> ATE   |  (m>0) ATION -> ATE ----
    # "ational" is 7 letters long, so word[:-7] removes it, then "ate" is appended
    if word.endswith("ational"):
        word = word[:-7] + "ate"          # relational -> relate
        rule.append("ATIONAL->ATE")
        steps.append(word)
    # "ation" is 5 letters long, so word[:-5] removes it, then "ate" is appended
    elif word.endswith("ation"):
        word = word[:-5] + "ate"          # relation -> relate
        rule.append("ATION->ATE")
        steps.append(word)
 
    # ---- Step 5a: (m>1) E ->  (remove silent final 'e') ----
    # runs on whatever the word looks like AFTER Step 2 (or the original
    # word, if Step 2 did not apply, e.g. "relate")
    if word.endswith("e"):
        word = word[:-1]                  # relate -> relat
        rule.append("E->removed")
        steps.append(word)
 
    return steps, rule
 
 
words = ["relational", "relation", "relate"]
 
print(f"{'Word':<12}{'Rule(s) Applied':<28}{'Steps'}")
print("-" * 65)
for w in words:
    steps, rule = porter_stem(w)
    print(f"{w:<12}{', '.join(rule):<28}{' -> '.join(steps)}")
 
print()
print(f"{'Word':<12}{'Final Stem'}")
print("-" * 24)
for w in words:
    steps, rule = porter_stem(w)
    print(f"{w:<12}{steps[-1]}")
