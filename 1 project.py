while True:
    print("\n--- Python Calculator ---")
    
    # 1. Ask the user what they want to do
    print("Enter 'q' to quit or any other key to continue.")
    choice = input("Choice: ").lower()
    
    if choice == 'q':
        print("Exiting calculator. Goodbye!")
        break  # This stops the loop
    
    # 2. Get the numbers and operator
    try:
        num1 = float(input("Enter first number: "))
        op = input("Enter operator (+, -, *, /): ")
        num2 = float(input("Enter second number: "))

        # 3. Calculation Logic
        if op == '+':
            print(f"Result: {num1 + num2}")
        elif op == '-':
            print(f"Result: {num1 - num2}")
        elif op == '*':
            print(f"Result: {num1 * num2}")
        elif op == '/':
            if num2 != 0:
                print(f"Result: {num1 / num2}")
            else:
                print("Error: Cannot divide by zero!")
        else:
            print("Invalid operator!")
            
    except ValueError:
        print("Error: Please enter valid numbers.")
5
