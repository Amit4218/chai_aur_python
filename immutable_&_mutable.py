"""
There are two types of Data-Types in python.

# Note: Every thing in python is a object. 

1. Mutable => a type which can be changed.

2. Immutable => a type which cannot be changed.

# Mutables types are:                    

1. list  
2. set 
3. dictionary 
4. Bytearray 
5. Array 

# Immutabe types are:

1. integer 
2. Float 
3. Boolean 
5. String 
6. Tuples 
7. Frozen set 
8. Bytes 


# In python dataTypes cannot be changes once its created,
  
# For Example: 

  # Example 1:

  If you create a variable x and assign it a value of 10,
  a reference will be create in memory.

  x = 10   ==> here now x will be referencing 10 which is in the memory.Now if we create a new variable y and assign,
  y = x        it x, it will also be referencing from the same memory address.


 # Example 2:

  Now if we assign x a value and change it to another value, there will be two memory spaces created 
  one for the first value and second for the second value, because we are passing an immutable value,
  that why there will be two memory spaces created

  x = 10
  x = 15

  Since, there is no value refrencing to the value 10 python garbage collection will remove or delete the memory refrence,
  and free the space.

"""



