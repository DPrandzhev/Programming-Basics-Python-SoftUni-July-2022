number = int(input())

for current_number in range(1111, 9999 + 1):
    current_num_is_special = True
    current_num_as_string = str(current_number)
    for current_digit in current_num_as_string:
        if int(current_digit) == 0 or number % int(current_digit) != 0:
            current_num_is_special = False
            break

    if current_num_is_special:
        print(current_num_as_string, end = " ")