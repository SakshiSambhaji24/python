n=int(input("Enter number:"))

reverse=0
while n>0:
    lastdigit=n%10
    reverse=reverse*10+lastdigit
    n//=10

print("Reversed number:",reverse)    

