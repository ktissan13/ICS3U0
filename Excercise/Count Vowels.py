# Count Vowels
# Tissan Kugathas
# ICS 3U0
# April 12 2019

text = str(input("Enter text: "))
vowels = text.count("a") + text.count("e") + text.count("i") + text.count("o") + text.count("u")
vowels = vowels + text.count("A") + text.count("E") + text.count("I") + text.count("O") + text.count("U")
print("The number of vowels in", text, "is", vowels)
