math_problem = input("Type some simple math problem: ")

try:
    x, y, z = math_problem.split(" ")
    x = float(x)
    z = float(z)

    if y == "+":
        result = x + z
    elif y == "-":
        result = x - z
    elif y == "*":
        result = x * z
    elif y == "/":
        result = x / z
    else:
        print("Invalid operator. Please use +, -, *, or /.")
        exit()

    print(f"{x} {y} {z} = {result}")

except ValueError:
    print("Invalid input. Please enter in the format: number operator number.")