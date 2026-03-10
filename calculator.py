def calculator():
    global a, b
    print("simple calculator")
    print(" Operations : + - * /")

    while True:
        op = input("Enter operation (+, -, *, /) or 'q' to quit: ")

        if op == "q":
            print("Exiting.......")
            break

        if op not in ["*", "-", "/", "+"]:
            print("Invalid operation.....try again !")
            continue

        try:
            a = int(input("Enter first number: "))
            b = int(input("Enter second number: "))
        except ValueError:
            print("Enter actual numbers !!!")

        if op == '+':
            print("result", a + b)

        elif op == '-':
            print("result", a - b)

        elif op == '*':
            print("result", a * b)

        elif op == "/":
            if b == 0:
                print(" Dividing by 0.....seriously")
            else:
                print("result", a / b)

        print()


calculator()
