def add_25():
    return lambda a: a + 25


fun = add_25()

n = int(input("Enter a number: "))
print("Addition of 25 in this number is: ", fun(n))
