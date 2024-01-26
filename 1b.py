num = int(input("enter nu : "))
nums = str(num)

if nums == nums[::-1]:
    print("palindrome")
else:
    print("not palindrome")

# digit_counts = {}
# for digit in nums:
#     digit_counts[digit] = digit_counts.get(digit, 0) + 1
# print(digit_counts)

for i in range(10):
    if nums.count(str(i)) > 0:
        print(str(i),"appears", nums.count(str(i)), "times")


