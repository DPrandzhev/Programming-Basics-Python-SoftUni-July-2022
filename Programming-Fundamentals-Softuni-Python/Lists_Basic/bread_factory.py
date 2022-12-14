events = input().split("|")
total_coins = 100
total_energy = 100
is_open = True
earned_coins = 0

for event in events:
    event_items = event.split("-")
    type_of_event = event_items[0]
    value_of_event = int(event_items[1])

    if type_of_event == "rest":
        current_energy = total_energy
        total_energy += value_of_event
        if total_energy > 100:
            total_energy = 100

        gained_energy = total_energy - current_energy
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {total_energy}.")

    elif type_of_event == "order":
        if total_energy >= 30:
            total_energy -= 30
            total_coins += value_of_event
            print(f"You earned {value_of_event} coins.")
        else:
            total_energy += 50
            print("You had to rest!")
            continue

    else:
        if total_coins >= value_of_event:
            total_coins -= value_of_event
            print(f"You bought {type_of_event}.")

        else:
            print(f"Closed! Cannot afford {type_of_event}.")
            is_open = False
            break

if is_open:
    print("Day completed!")
    print(f"Coins: {total_coins}")
    print(f"Energy: {total_energy}")
