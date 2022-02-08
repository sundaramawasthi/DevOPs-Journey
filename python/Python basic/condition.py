# condition

# function declaration

def main():
    x, y = 10, 100

    # condition use if else elif

    if(x < y):
        st = (" x is less than y")
    elif(x == y):
        st = ("x is same to y ")
    else:
        st = ("x is greater than y")
    print(st)
# conditional statement let you use "a if c"else b

    st = "x is less than y" if(x < y) else "x is greater than or same as y"
    print(st)


if __name__ == "__main__":
    main()
