def main():
    print("Welcome to Calculator App")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Square Root")
    print("7. Modulus")
    print("8. Exit")

    a=int(input("Choose function:"))

    if a==1:
        add()
    elif a==2:
        subtract()
    elif a==3:
        multiply()
    elif a==4:
        divide()
    elif a==5:
        power()
    elif a==6:
        sqrt()
    elif a==7:
        modulus()
    
    elif a==8:
        print("Bye")
    else:
        print("Invalid Input")
        main()

def add():
    n=float(input("Enter First Number"))
    m=float(input("Enter Second Number"))

    print("Sum is:",n+m)

    main()

def subtract():
    n=float(input("Enter First Number"))
    m=float(input("Enter Second Number"))

    print("Difference is:",n-m)

    main()

def multiply():
    n=float(input("Enter First Number"))
    m=float(input("Enter Second Number"))

    print("Product is:",n*m)

    main()

def divide():
    n=float(input("Enter First Number"))
    m=float(input("Enter Second Number"))

    if m==0:
        print("Division by 0 is invalid")
        main()

    print("Quotient is:",n/m)

    main()

def power():
    n=float(input("Enter First Number"))
    m=float(input("Enter Second Number"))


    print("Result is:",n**m)

    main()

def sqrt():
    n=float(input("Enter First Number"))
    m=float(input("Enter Second Number"))


    print("Result is:",n**0.5)

    main()

def modulus():
    n=float(input("Enter First Number"))
    m=float(input("Enter Second Number"))

    if m==0:
        print("Division by 0 is invalid")
        main()

    print("Modulus is:",n%m)

    main()

main()



