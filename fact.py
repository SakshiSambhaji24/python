n=int(input("Enter the number:"))

print("\nFactorial of a Number:")
fact = 1
i = 1
while i <= n:
    fact *= i
    i += 1
print("Factorial:", fact)

print("\nFibonacci Series:")
a = 0
b = 1
while a<=n:
    print(a, end=" ")
    a,b=b,a+b      