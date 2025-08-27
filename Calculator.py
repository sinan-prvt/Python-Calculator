def run_calc():
    while True:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        op = input("Enter operation (+, -, *, / or exit): ")
        if op == "exit": break
        elif op == "+": print("Result:", a+b)
        elif op == "-": print("Result:", a-b)
        elif op == "*": print("Result:", a*b)
        elif op == "/": print("Result:", a/b if b!=0 else "Error")
        else: print("Invalid operation!")

run_calc()
