numbers = list(map(int,input().strip().split(" ")))
how_many_numbers_to_remove = int(input())

for n in range(how_many_numbers_to_remove):
    numbers.remove(min(numbers))
count = 1
for o in numbers:
    if count != (len(numbers)):
        print(f"{o},", end=" ")

    else:
        print(f"{o}")
    count += 1

#
# numbers = input().split(" ")
# amount_to_remove = int(input())
#
# for i in range(1, amount_to_remove + 1):
#     numbers.remove(min(numbers))
#
# print(numbers)