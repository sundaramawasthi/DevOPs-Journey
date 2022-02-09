# Loop

def main():
    x = 1
# while loop
    while(x < 5):
        print(x)
        x += 1


# For loop
for x in range(5, 10):
    print(x)
    x += 1


# uses a for loop over  a collection
day = ['mon', 'twe', 'wed']
for d in day:
    print(d)

# use break and contineoous
for x in range(5, 10):
    # if(x == 7):
    # break
    if(x % 2 == 0):
        continue
    print(x)

#

day = ['mon', 'twe', 'wed']
for i, d in enumerate(day):
    print(i, d)

if __name__ == "__main__":
    main()
