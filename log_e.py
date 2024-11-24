import math

def calculate_log(expression):
    """Calculate the logarithm based on user input."""
    try:
        inputs = expression.strip("log()").split(",")
        base = float(inputs[0])
        number = float(inputs[1])
        return "Logarithm Result: " + str(math.log(number, base))
    except (ValueError, IndexError):
        return "Error: Invalid format for log. Please use 'log(base, number)'."

def calculate_exp(expression):
    """Calculate the exponential based on user input."""
    try:
        number = float(expression.strip("e^()"))
        return "Exponential Result: " + str(math.exp(number))
    except ValueError:
        return "Error: Invalid format for exp. Please use 'e^(number)'."

print("Enter the expression you want to calculate or type 'x' to exit.")
print("Supported functions:")
print("1. Logarithm: log(base, number) (e.g., log(2, 8))")
print("2. Exponential: e^(number) (e.g., e^(2))")

e = ""
while e != "x":
    e = input("Enter your expression (or 'x' to exit): ")
    if e == "x":
        break

    if e.startswith("log"):
        print(calculate_log(e))
    elif e.startswith("e^"):
        print(calculate_exp(e))
    else:
        print("Invalid format. Please use 'log(base, number)' or 'e^(number)'.")
else:
    print("Exited")