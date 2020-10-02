def compute(x, y):
    if x > y:
        smaller = y
    else :
        smaller = x
    for i in range(1, smaller+1):
        if(x%i == 0) and (y%i == 0):
            gcd = i;
    return gcd;

a = input("Enter the first number: ")
b = input("Enter second number: ")
val = compute(a, b)
print(val)
