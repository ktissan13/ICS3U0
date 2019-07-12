# coder
# Tissan Kugathas
# ICS 3U0
# May 5 2019

string = input("Enter a string: ").split()
new_string = ''

for word in string:
    for letter in word:
        if letter == 'x':
            new_string=new_string+'a'
        elif letter == 'y':
            new_string=new_string+'b'
        elif letter == 'X':
            new_string=new_string+'A'
        elif letter == 'y':
            new_string=new_string+'B'
        else:
            new_string=new_string+chr(ord(letter)+2)
    new_string=new_string+' '

print('Encoded Message: 'new_string)
        
