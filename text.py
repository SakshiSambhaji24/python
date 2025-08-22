text="Python is fun.Python is easy to learn. python is powerful."

text=text.lower()
print(text)

text=text.replace(".","")
print(text)

words=text.split()#splits the text and put in list called word
print("Total number of words:",len(words))

freq={}
for word in words:
    if word in freq:
        freq[word]+=1
    else:
        freq[word]=1

print("\nWord Frequencies:")
for word in freq:
    print(word+":",freq[word])            


vowels="aeiou"
vowel_count=0
for char in text:
    if char in vowels:
        vowel_count+=1

print("\nTotal number of vowels:",vowel_count)        