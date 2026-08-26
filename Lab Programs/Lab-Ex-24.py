def dialog_act(sentence):
    s = sentence.lower()

    if any(w in s for w in ["hello", "hi", "hey"]):
        return "Greeting"

    elif "?" in sentence or any(w in s for w in ["what", "why", "how", "where"]):
        return "Question"

    elif any(w in s for w in ["please", "can you", "could you"]):
        return "Request"

    elif any(w in s for w in ["bye", "goodbye", "see you"]):
        return "Goodbye"

    elif any(w in s for w in ["yes", "no", "okay"]):
        return "Answer"

    else:
        return "Statement"


text = input("Enter dialog: ")

print("\nDialog Act:")
print(text, "->", dialog_act(text))
