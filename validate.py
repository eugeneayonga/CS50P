import re

email = input("Enter your email address: ").strip()

if re.search(r"^\w+@(\w+\.)?\w+\.(edu|com|org|gov)$", email, re.IGNORECASE):
    print("Valid email address")
else:
    print("Invalid email address")