n=int(input("Enter n"))
for i in range(1,n+1):#row
    for j in range(65,65+i):#alphabets in rows
        print(chr(j),end="")#chr convert ASCII number to character
    print()    


print()
for i in range(n,0,-1):
    for j in range(65,65+i):
        print(chr(j),end="")
    print()    

print()
for i in range(1,n+1):
    for j in range(1,1+i):
        print(j,end="")
    print()     

print()
for i in range(n,0,-1):
    for j in range(1,1+i):
        print(j,end="")
    print()     

    