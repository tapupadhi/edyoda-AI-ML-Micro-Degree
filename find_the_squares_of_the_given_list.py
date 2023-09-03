lst = input("Enter a sample list: ").replace(" ", "").replace("[", "").replace("]", "").split(",")

print("Square of the given list is: ", list(map(lambda n: int(n) * int(n), lst)))
