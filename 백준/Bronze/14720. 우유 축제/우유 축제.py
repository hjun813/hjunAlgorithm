import sys
input = sys.stdin.readline

N = int(input())
store = list(map(int, input().split()))

# print(store)

beforeDrink = 0
drink = 0

for milk in store:
    if milk == beforeDrink:
        beforeDrink += 1
        beforeDrink = beforeDrink % 3
        drink += 1

print(drink)