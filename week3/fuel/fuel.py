while True:
    fraction = input("Fraction: ")
    try:
        x,y = fraction.split("/")
        x = int(x)
        y = int(y)
        if y == 0:
            raise ZeroDivisionError
        elif x > y:
            raise ValueError
        elif (x < 0 < y) or (x > 0 > y):
            raise ValueError
    except ValueError:
        continue
    except ZeroDivisionError:
        continue
    else:
        fuel_percentage = float(x/y)
        if fuel_percentage <= 0.01:
            print("E")
        elif fuel_percentage >= 0.99:
            print("F")
        else:
            print(f"{round(fuel_percentage*100)}%")
    break
