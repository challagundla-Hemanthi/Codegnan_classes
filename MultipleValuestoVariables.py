# Assign Multiple Values to Variables

x, y, z = "Orange", "Banana", "Cherry"
# remember that the number of variables must be equal to the number of values, or else you will get an error
print(x)
print(y)
print(z)


x = y = z = "orange"# this is called chaining assignment, where all three variables are assigned the same value
print(x)
print(y)
print(z)



fruits = ["apple", "banana", "cherry"]
x, y, z = fruits # this is called unpacking, where the values in the list are unpacked into the variables
print(x)
print(y)
print(z)