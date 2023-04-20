import math

max, power = input().split()
pow_num = int(power)
pow_len = len(str(pow_num))
max_len = len(max)
max = int(max)


total = 0
difference = max_len - pow_len

sign = 1
for i in range(difference + 1):
    total += sign * (10 ** (difference - i) * math.comb(difference + 1, difference - i))
    sign *= -1

print(total)
