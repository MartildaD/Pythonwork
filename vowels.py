word = input("Enter a word: ")
vowels = 0
for characters in word: 
    if characters in "aeiouAeiou":
        vowels += 1
print("Number of vowels:", vowels)
