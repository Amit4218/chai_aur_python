def chai_order():

    print("Welcome ! what chai would you like?")

    order = yield

    while True:
        print(f"Serving: {order}")

        order = yield   # Actually stops its from going to infinite looping


order = chai_order()

order.send