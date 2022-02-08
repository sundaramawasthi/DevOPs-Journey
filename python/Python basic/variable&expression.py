#   Variable

# Declare the variable
f = 0
# print(f)

# redeclare the variable
#f = "abc"
# print(f)

# error : variable of different type can't be combine
# print("this is a string" + 123)  # show the type error


# Convert to string
#print("convert to string using str" + str(123))


# global and local variable in function

def somefunction():  # declare function def whose name is somefunction
    global f
    f = "def"  # declare variable f =def in function
    print(f)     # print the f value


somefunction()   # call the somefunction
print(f)         # print the f value

del(f)  # the del variable delete the difinition of variable f that are privious declare
print(f)
