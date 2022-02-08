# function

# define the function
def fun1():  # function are define using def keyword then func name then colon that indicate start of function code block.
    print("i am a function")

# function take argumment


def fun2(arg1, arg2):
    print(arg1, " ", arg2)


# function that return the value
def cube(x):
    return x*x*x

# function with default value of argument


def power(num, x=1):
    result = 1
    for i in range(x):
        result = result*num
    return result

# function with variable number of argument


fun1()  # function call by directly
print(fun1())  # function print using print
print(fun1)  # function not call


#fun2(10, 20)
# cube(3)
# print(cube(3))
print(power(2))
print(power(2, 3))
