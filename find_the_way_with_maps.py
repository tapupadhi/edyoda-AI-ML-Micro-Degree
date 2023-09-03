lst = input("Enter a sample list: ").replace(" ", "").replace("[", "").replace("]", "").split(",")

print("Triple of all the  elements: ", list(map(lambda n: int(n) * 3, lst)))
