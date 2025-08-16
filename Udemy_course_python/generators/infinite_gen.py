def serve_refills():

    count = 1

    while True:
        yield f"Tea Refilled: {count}"
        count += 1


usr_1 = serve_refills()

for _ in range(5):
    print(next(usr_1))
