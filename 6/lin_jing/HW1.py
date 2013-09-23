#!/usr/bin/python

#Factorization of Input Number

def main(): 
    try:
        a = int(raw_input("Enter a number: "))
    except ValueError:
        print("That is not a number!")
        return 0
    String = "The Factors of %d are " % (a)
    Counter = int(a**.5)
    for i in range(2, Counter):
        if(a  == (a / i) * i):
            a = a / i
            String += "%d %d" % (a, i)
    print(String)

if __name__ == "__main__":
    main()
