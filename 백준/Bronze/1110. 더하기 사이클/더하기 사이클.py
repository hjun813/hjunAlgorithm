n = int(input())
count = 0


def cycle(a):

    global count
    if a != n:

        if a < 10:
            count +=1
            cycle(a * 10 + a)
        else:
            count +=1
            cycle(((a % 10) * 10) + (((a // 10) + (a % 10)) % 10))


if n==0:
    count = 0
if n < 10:
    cycle(n * 10 + n)
else:
    cycle(((n % 10) * 10) + (((n // 10) + (n % 10)) % 10))



print(count+1)

