numbers = input()


def all_sum(num):
    even_total = 0

    odd_total = 0
    for i in num:
        i = int(i)
        if i % 2 == 0:
            even_total += i
        else:
            odd_total += i
    return f"Odd sum = {odd_total}, Even sum = {even_total}"


print(all_sum(numbers))
