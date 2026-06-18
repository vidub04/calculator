def main():
    print("Welcome to Calculator App")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

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
        print("Bye")
    else:
        print("Invalid Input")
        main()

def add():
    n=int(input("Enter First Number"))
    m=int(input("Enter Second Number"))

    print("Sum is:",n+m)

    main()

def subtract():
    n=int(input("Enter First Number"))
    m=int(input("Enter Second Number"))

    print("Difference is:",n-m)

    main()

def multiply():
    n=int(input("Enter First Number"))
    m=int(input("Enter Second Number"))

    print("Product is:",n*m)

    main()

def divide():
    n=int(input("Enter First Number"))
    m=int(input("Enter Second Number"))

    if m==0:
        print("Division by 0 is invalid")
        main()

    print("Quotient is:",n/m)

    main()

main()



