
climbing_groups_number = int(input())

# •	Група до 5 човека – изкачват Мусала
# •	Група от 6 до 12 човека – изкачват Монблан
# •	Група от 13 до 25 човека – изкачват Килиманджаро
# •	Група от 26 до 40 човека –  изкачват К2
# •	Група от 41 или повече човека – изкачват Еверест
mussala_count = 0
montblanc_count = 0
kilimanjaro_count = 0
k2_count = 0
everest_count = 0

for _ in range(climbing_groups_number):
    climbing_members = int(input())

    if climbing_members <= 5:
        mussala_count += climbing_members
    elif climbing_members <= 12:
        montblanc_count += climbing_members
    elif climbing_members <=25:
        kilimanjaro_count += climbing_members
    elif climbing_members <= 40:
        k2_count += climbing_members
    elif climbing_members > 40:
        everest_count += climbing_members

total_count = mussala_count + montblanc_count + kilimanjaro_count +k2_count + everest_count

mussala_percent = mussala_count / total_count * 100
montblanc_percent = montblanc_count / total_count * 100
kilimanjaro_percent = kilimanjaro_count / total_count * 100
k2_percent = k2_count / total_count * 100
everest_percent = everest_count / total_count * 100

print(f"{mussala_percent :.2f}%")
print(f"{montblanc_percent :.2f}%")
print(f"{kilimanjaro_percent :.2f}%")
print(f"{k2_percent :.2f}%")
print(f"{everest_percent :.2f}%")

