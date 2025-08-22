a=float(input("Enter first number:"))
b=float(input("Enter second number:"))
c=float(input("Enter third number:"))

if a>=b and a>=c:
    print(a,"is largest number")
elif b>=a and b>=c:
    print(b,"is largest number")
else:
    print(c,"is largest number")

if a<=b and a<=c:
    print(a,"is smallest number")
elif b<=a and b<=c:
    print(b,"is smallest number")
else:
    print(c,"is smallest number")