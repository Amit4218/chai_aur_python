import time


timer = int(input("Enter the time in seconds: "))

if timer < 1:
    print("Please enter a valid time")

for seconds in range(timer, 0, -1):
    mins, secs = divmod(seconds, 60)
    print(f"{mins:02}:{secs:02}", end="\r")
    time.sleep(1)

print("time up")
print("\a")
