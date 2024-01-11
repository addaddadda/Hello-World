# A hello world program in python
print("Hello World!")

import turtle

turtle.write("Hello World!")
turtle.done()
# A demo of catching an error
try:
    a = int(input("Enter a number: "))
except ValueError:
    print("Invalid")
finally:
    print("Goodbye")
