# Generate a Function with yield
# write a generator function that yeilds even number
#  up to a specified limit

def even_generator(limit):
    for i in range(2, limit + 1, 2):
        yield i

for num in even_generator(10):
    print(num)



# yield help us keep track of our number in our memory