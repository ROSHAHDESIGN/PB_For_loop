age = int(input())
washing_machine = float(input())
toy_price = int(input())

total_money = 0
total_toys = 0

for birth_day in range(1,age +1):

    if birth_day % 2 == 0:
        total_money += (birth_day * 5)
        total_money -= 1
    else:
       total_toys += 1

total_toys_money = total_toys * toy_price
total_saved_money = total_toys_money + total_money

if total_saved_money >= washing_machine:
    diff = total_saved_money - washing_machine
    print(f"Yes! {diff:.2f}")
else:
    money_needed = washing_machine - total_saved_money
    print(f"No! {abs(money_needed):.2f}")

