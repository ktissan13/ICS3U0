# For loop for strings
# ICS3U0
# Mr Veera
# 16 Nov 2017

vowel=0



phrase=input('Give a word or phrase: ')

for letter in phrase:
    print(letter)
    if letter in 'aeiou':
        vowel+=1

print(vowel)

        
    

        


