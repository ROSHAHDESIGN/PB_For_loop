# •	"Facebook" -> 150 лв.
# •	"Instagram" -> 100 лв.
# •	"Reddit" -> 50 лв.

opened_tabs = int(input())  # 4
salary = float(input())

for n in range(opened_tabs):
    current_web_site = input()
    if current_web_site == "Facebook":
        salary -= 150
    elif current_web_site == "Instagram":
        salary -= 100
    elif current_web_site == "Reddit":
        salary -= 50

    if salary <= 0:
        break

if salary <= 0:
    print("You have lost your salary.")
else:
    print(int(salary))
