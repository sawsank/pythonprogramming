##sum of a series of a number up to n terms

terms = 5
num = 2

sum_seq = 0

for i in range(0, terms):
    print(num, end="+")
    sum_seq += num
    num = num * 10 + 2
print("\nSum of above series is", sum_seq)