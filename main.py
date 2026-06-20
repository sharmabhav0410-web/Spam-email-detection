emails = [
    "Congratulations! You won a prize",
    "Meeting scheduled for tomorrow",
    "Claim your free gift now"
]

for email in emails:
    if "free" in email.lower() or "won" in email.lower():
        print(email, "-> Spam")
    else:
        print(email, "-> Not Spam")
