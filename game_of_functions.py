def sum_of_the_numbers(lst):
    s = 0
    for el in lst:
        s += int(el)

    print("Expected Output7: ", s)


sum_of_the_numbers(input("Sample List: ").replace(' ', '').split(','))
