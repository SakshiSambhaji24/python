num=int(input("Enter the number:"))

print("natural numbers")
for i in range(1,num+1):
    print(i,end=" ")

print("\nEven numbers")
for i in range(0,num+1):
    if i%2==0:
        print(i,end=" " )

print("\nodd numbers")
for i in range(0,num+1):
    if i%2!=0:
        print(i,end=" ")
     
print("\nSum of natural ",num,"number")
sum=0
for i in range(1,num+1):
    sum=sum+num
print(sum)

print("/nSquare of numbers")
for i in range(1,num+1):
    print(i*i,end=" ")
    