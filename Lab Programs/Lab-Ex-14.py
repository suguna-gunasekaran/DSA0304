subject = input("Enter Subject: ")
verb = input("Enter Verb: ")

singular = ["He", "She", "John"]
plural = ["They", "We"]

if subject in singular and verb == "runs":
    print("Agreement Correct")

elif subject in plural and verb == "run":
    print("Agreement Correct")

else:
    print("Agreement Incorrect")
