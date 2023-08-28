def calculate_upper_and_lower_characters(st):
    count_upper_case = 0
    count_lower_case = 0
    for ch in st:
        if ch.isupper():
            count_upper_case += 1
        elif ch.islower():
            count_lower_case += 1
        else:
            pass
    print("Expected Output: ")
    print("No. of Upper case characters: ", count_upper_case)
    print("No. of Lower case characters: ", count_lower_case)


s = input("Sample String: ")
calculate_upper_and_lower_characters(s)
