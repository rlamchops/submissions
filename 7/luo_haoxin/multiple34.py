#!/usr/bin/python

#sum of all multiples of 3 or 5 below n

def main():
    n = raw_input("Enter something: ")
    sum = 0
    for i in range(1, int(n)):
        if (i<n) and (i%3 == 0):
            sum+= i
        elif (i%5 == 0):
            sum+= i
    print(sum)


if __name__ == "__main__":
    main()
