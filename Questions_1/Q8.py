password = "120495"

if len(password) < 6:
    print("weak password")
elif len(password) <= 10:
    print("medium password")
else:
    print("strong password")