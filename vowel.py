char=input("Enter a single alphabet:")

if len(char)==1 and char.isalpha():#character must be letter
    char=char.lower()#convert into lowercase i.e A=>a

    if char in 'aeiou':
        print("It is a vowel")
    else:
        print("It is a consonant")  

else:
    print("Invalid input")          