print("Sum: ")


def jam(a, b):
    javab = a + b
    return javab


Number_first = 12
number_second = 15
x = jam(Number_first, number_second)

print(x)


print("Peyment: ")


hour = int(input("enter your work hour: "))
cost_per_hour = int(input("Enter your peyment per hour: "))


def salary(hour, cost_per_hour):
    if hour < 50:
        return "Sorry! less than work basic"

    elif 120 > hour > 70:
        print("Wow you are one of the top A employee")
        peyment_top = hour * cost_per_hour
        return peyment_top

    elif hour > 120:
        return "So much work, Thanks"
    else:
        peyment = hour * cost_per_hour
        return peyment


print(salary(hour, cost_per_hour))
