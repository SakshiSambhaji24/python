n=int(input("Enter a Number:"))
i=2
is_prime=True

if n<=1:
    is_prime=False
else:    
    while i<=n // 2:
        if n%i==0:
           is_prime=False
           break
        i+=1

if is_prime:
    print("Prime Number")
else:
    print("Not a Prime Number")    


digitsum=0
while n>0:
    digitsum+=n%10 
    n//=10
print("Sum of digit:",digitsum)

