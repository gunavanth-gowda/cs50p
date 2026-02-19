expression = input("Expression: ").strip()

x = float(expression.split()[0])
y = expression.split()[1]
z = float(expression.split()[2])

match y:
    case "+":
        print(round(x + z, 1))
    case "-":
        print(round(x - z, 1))
    case "*":
        print(round(x * z, 1))
    case "/":
        print(round(x / z, 1))
