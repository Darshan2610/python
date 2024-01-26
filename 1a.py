t1 = int(input("test 1 "))
t2 = int(input("test 2 "))
t3 = int(input("test 3 "))

avg1 = (t1 + t2) / 2
avg2 = (t2 + t3) / 2
avg3 = (t1 + t3) / 2

res = max(avg1, avg2, avg3)
print(res)
