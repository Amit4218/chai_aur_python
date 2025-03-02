# will open a file, if the file dosen't exit it will create one
# with writing permission 

file = open("file.txt", 'w') 

# opening file with try and catch to catch error if occured
# and writing in it

try:
    file.write("hello world")
finally:
    file.close()

# a better syntax

with open("youtube.txt", 'w') as file:
    file.write("chai aur code")

