import time

waiting_time = 1
retry_count = 0
code = 12345

while True:

    user_input = int(input("Enter your code: "))

    if retry_count < 5:

        if user_input != code:
            retry_count += 1
            print("incorrect code try again after: ", waiting_time)
            time.sleep(waiting_time) 
            waiting_time *= 1               
    else:
        print("max tries reached")
        break


    


