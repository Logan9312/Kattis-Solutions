import math

max, power = input().split()
pow_num = int(power)
pow_len = len(str(pow_num))
max_len = len(max)
max = int(max)


total = 0
difference = max_len - pow_len
if max_len == pow_len:
    if pow_num < max:
        total = 1
elif difference == 1:
    total = 10 * 2  # AX, XA
    total -= 1  # AA
elif difference == 2:
    total = 100 * 3  # AXX, XAX, XXA
    total -= 10 * 3  # AAX, AXA, XAA
    total += 1  # AAA
elif difference == 3:
    total = 1000 * 4  # AXXX, XAXX, XXAX, XXXA
    total -= 100 * 6  # AXXA, AXAX, XAAX, XAXA, XXAA, AAXX
    total += 10 * 4  # AAAX, AAXA, AXAA, XAAA
    total -= 1  # AAAA
elif difference == 4:
    total = 10000 * math.comb(5, 5)  # AXXXX, XAXXX, XXAXX, XXXAX, XXXXA
    total -= 1000 * math.comb(5, 2)  # AXXXA, AXXAX, AXAXX, XAXXA, XAAXX, XXAAX, AAXXX, XAXAX, XXAXA, XXXAA
    total += 100 * math.comb(5, 3)  # AAAXX, AAXAX, AXAAX, XAAA, AXXAA, AXAXA, XAAXA, XXAAA, AAXAA, XAAAX
    total -= 10 * math.comb(5, 4)  # AAAAX, AAAXA, AAXAA, AXAAA, XAAAA
    total += 1 * math.comb(5, 5)  # AAAAA
elif difference == 5:
    total = 100000 * 6
    total -= 10000 * 15
    total += 1000 * 20
    total -= 100 * 15
    total += 10 * 6
    total -= 1
elif difference == 6:
    total = 1000000 * 7
    total -= 100000 * 21
    total += 10000 * 35
    total -= 1000 * 21
    total += 100 * 7
    total -= 1
elif difference == 7:
    total = 10000000 * 8
    total -= 1000000 * 28
    total += 100000 * 56
    total -= 10000 * 70
    total += 1000 * 56
    total -= 100 * 28
    total += 10 * 8
    total -= 1
elif difference == 8:
    total = 100000000 * 9
    total -= 10000000 * 36
    total += 1000000 * 84
    total -= 100000 * 126
    total += 10000 * 126
    total -= 1000 * 84
    total += 100 * 36
    total -= 10 * 9
    total += 1
elif difference == 9:
    total = 1000000000 * 10
    total -= 100000000 * 45
    total += 10000000 * 120
    total -= 1000000 * 210
    total += 100000 * 252
    total -= 10000 * 210
    total += 1000 * 120
    total -= 100 * 45
    total += 10 * 10
    total -= 1

elif difference == 10:
    total = 10000000000 * 11
    total -= 1000000000 * 55
    total += 100000000 * 220
    total -= 10000000 * 495
    total += 1000000 * 792
    total -= 100000 * 924
    total += 10000 * 792
    total -= 1000 * 495
    total += 100 * 220
    total -= 10 * 55
    total += 1

elif difference == 11:
    total = 100000000000 * 12
    total -= 10000000000 * 66
    total += 1000000000 * 286
    total -= 100000000 * 715
    total += 10000000 * 1287
    total -= 1000000 * 1716
    total += 100000 * 1716
    total -= 10000 * 1287
    total += 1000 * 715
    total -= 100 * 286
    total += 10 * 66
    total -= 1

elif difference == 12:
    total = 1000000000000 * 13
    total -= 100000000000 * 78
    total += 10000000000 * 364
    total -= 1000000000 * 1001
    total += 100000000 * 2002
    total -= 10000000 * 3003
    total += 1000000 * 3432
    total -= 100000 * 3003
    total += 10000 * 2002
    total -= 1000 * 1001
    total += 100 * 364
    total -= 10 * 78
    total += 1

elif difference == 13:
    total = 10000000000000 * 14
    total -= 1000000000000 * 91
    total += 100000000000 * 455
    total -= 10000000000 * 1365
    total += 1000000000 * 3003
    total -= 100000000 * 5005
    total += 10000000 * 6435
    total -= 1000000 * 6435
    total += 100000 * 5005
    total -= 10000 * 3003
    total += 1000 * 1365
    total -= 100 * 455
    total += 10 * 91
    total -= 1

elif difference == 14:
    total = 100000000000000 * 15
    total -= 10000000000000 * 105
    total += 1000000000000 * 560
    total -= 100000000000 * 1820
    total += 10000000000 * 4368
    total -= 1000000000 * 8008
    total += 100000000 * 8008
    total -= 10000000 * 6435
    total += 1000000 * 4368
    total -= 100000 * 2380
    total += 10000 * 1050
    total -= 1000 * 384
    total += 10 * 15
    total -= 1

elif difference == 15:
    total = 1000000000000000 * 16
    total -= 100000000000000 * 120
    total += 10000000000000 * 680
    total -= 1000000000000 * 2380
    total += 100000000000 * 6188
    total -= 10000000000 * 12376
    total += 1000000000 * 19448
    total -= 100000000 * 24310
    total += 10000000 * 24310
    total -= 1000000 * 19448
    total += 100000 * 12376
    total -= 10000 * 6188
    total += 1000 * 2380
    total -= 100 * 680
    total += 10 * 120
    total -= 1

elif difference == 16:
    total = 10000000000000000 * 17
    total -= 1000000000000000 * 136
    total += 100000000000000 * 816
    total -= 10000000000000 * 3060
    total += 1000000000000 * 8568
    total -= 100000000000 * 18564
    total += 10000000000 * 31824
    total -= 1000000000 * 43758
    total += 100000000 * 48620
    total -= 10000000 * 43758
    total += 1000000 * 31824
    total -= 100000 * 18564
    total += 10000 * 8568
    total -= 1000 * 3060
    total += 100 * 816
    total -= 10 * 136
    total += 1

elif difference == 17:
    total = 100000000000000000 * 18
    total -= 10000000000000000 * 153
    total += 1000000000000000 * 969
    total -= 100000000000000 * 3876
    total += 10000000000000 * 11628
    total -= 1000000000000 * 27132
    total += 100000000000 * 50388
    total -= 10000000000 * 75582
    total += 1000000000 * 92378
    total -= 100000000 * 92378
    total += 10000000 * 75582
    total -= 1000000 * 50388
    total += 100000 * 27132
    total -= 10000 * 11628
    total += 1000 * 3876
    total -= 100 * 969
    total += 10 * 153
    total -= 1

elif difference == 18:
    total = 10000000000000000000 * 20
    total -= 1000000000000000000 * 190
    total += 100000000000000000 * 1140
    total -= 10000000000000000 * 4845
    total += 1000000000000000 * 15504
    total -= 100000000000000 * 38760
    total += 10000000000000 * 77520
    total -= 1000000000000 * 125970
    total += 100000000000 * 167960
    total -= 10000000000 * 184756
    total += 1000000000 * 167960
    total -= 100000000 * 125970
    total += 10000000 * 77520
    total -= 1000000 * 38760
    total += 100000 * 15504
    total -= 10000 * 4845
    total += 1000 * 1140
    total -= 100 * 190
    total += 10 * 20
    total -= 1


print(total)
