import math

max, power = input().split()
pow_num = 2 ** int(power)
pow_len = len(str(pow_num))
max_len = len(max)
max = int(max)


total = 0
difference = max_len - pow_len

sign = 1


for i in range(difference + 1):
    # Build case when position is larger than power

    total += sign * (10 ** (difference - i) * math.comb(difference + 1, difference - i))
    sign *= -1

print(total)


# Experimenting with non 999 numbers
# number = 2
# find = 30
# ntotal = 0

# ntotal += 10 + 3  # 2X, X2
# ntotal -= 1  # 22
# print(ntotal)


# number = 2
# find = 300
# ntotal = 0

# ntotal += 100 + 3 * 10 + 3 * 10  # 2XX, X2X, XX2
# ntotal -= 10 + 10 + 3  # 22X, 2X2, X22
# ntotal += 1  # 222
# print(ntotal)


# number = 2
# find = 123
# ntotal = 0

# ntotal += 0 + (10 + 4) + (10 + 3)  # 2XX, X2X, XX2
# ntotal -= 0 + 0 + 2  # 22X, 2X2, X22
# ntotal += 0  # 222

# print(ntotal)

# number= 16
# find = 1234
# ntotal = 0

# ntotal += 0 + (10 * 2) + (10 + 3) # 16XX, X16X, XX16
# ntotal -= 0 # 1616
