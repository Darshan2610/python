def fn(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fn(n-1) + fn(n-2)
n = int(input("Enter a number : "))
fn(n)
if n > 0:
    print("fn(", n, ") = ",fn(n) , sep ="")
else:
    print("Error in input")