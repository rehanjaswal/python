s = input("enter a string: ").lower()
vowel = 0
consonant = 0
for ch in s:
    if ch in "aeiou":
        vowel+=1
    elif ch.isalpha():
        consonant+=1

print(f"vowels = {vowel}")
print(f"consonants = {consonant}")