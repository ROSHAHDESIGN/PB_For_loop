import sys

smallest = sys.maxsize
biggest = - sys.maxsize

n = int(input())
for i in range(0,n):
    num = int(input())
    if num < smallest:
        smallest = num
    elif num > biggest:
        biggest = num
print(smallest)
print(biggest)
