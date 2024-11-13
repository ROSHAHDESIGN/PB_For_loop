import sys

n = int(input())
max_num = - sys.maxsize
sum_all = 0

for i in range(n):
    new_number = int(input())
    if new_number > max_num:
        max_num = new_number

    sum_all += new_number

if max_num == sum_all - max_num:
    print("Yes")
    print(f"Sum = {max_num}")
else:
    diff = max_num - (sum_all - max_num)
    print("No")
    print(f"Diff = {abs(diff)}")
