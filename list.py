name=["Sakshi","Anisha","Siddhi"]
grades=[87,79,98]

name.append("vaishanvi")
grades.append(88)
print(name)
print(grades)

if "Sakshi" in name:
    index=name.index("Sakshi")
    grades[index]=90
print(name)
print(grades)    

if "Anisha" in name:
    index=name.index("Anisha")
    name.pop(index)
    grades.pop(index)
print(name)
print(grades)

total=0
for g in grades: 
    total+=g
avg=total/len(grades)
print(f"Average grade:{avg:.2f}")     


highest=grades[0]
lowest=grades[0]

for g in grades:     
    if g>highest:
        highest=g
    if g<lowest:
        lowest=g

print(f"Highest grade:{highest}")
print(f"Lowest grade:{lowest}")
