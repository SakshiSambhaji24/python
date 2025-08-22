n=int(input("Enter n:"))

print("Natural Number:")
i=1
while i<=n:
    print(i,end=" ")
    i+=1

print("\nEven Number:")
i=0
while i<=n:
    print(i,end=" ")
    i+=2   

print("\nodd Number:")
i=1
while i<=n:
    print(i,end=" ")
    i+=2   

print("\nSum of Natural Number:")
i=1
sum=0
while i<=n:
    sum+=i
    i+=1
print("sum:",sum)  

i=1
sum=0
while i<=n:
    sum+=i
    i+=2
print("Sum of odd numbers:",sum)

i=0
sum=0
while i<=n:
    sum+=i
    i+=2
print("Sum of even numbers:",sum)

print("\nReverse Number:")
while n>=1:
    print(n,end=" ")
    n-=1 

