name_actor = input()
academy_points = float(input())
evaluative_people_quantity = int(input())

total_points = academy_points #stojnostta TOTAL_POINTS se prezapisva,ZA DA SE DOBAVI kym ACADEMY _POINTS

for _ in range(evaluative_people_quantity):
    evaluative_person = input()
    evaluative_person_points = float(input())

    points = ((len(evaluative_person) * evaluative_person_points) / 2)
    total_points += points
    if total_points > 1250.5:
        break

if total_points <= 1250.5:
    print(f"Sorry, {name_actor} you need {1250.5 - total_points :.1f} more!")
else:
    print(f"Congratulations, {name_actor} got a nominee for leading role with {total_points:.1f}!")
