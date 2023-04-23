num = input().split()

count = 0
pow = 2 ** int(num[1])
strpow = str(pow)
for i in range(pow, int(num[0]) + 1):
    if strpow in str(i):
        print(str(i))
        count += 1

print(count)
