# e)
sentence = input("Enter a sentence: ")

word_count = len(sentence.split())
digit_count = sum(char.isdigit() for char in sentence)
uppercase_count = sum(char.isupper() for char in sentence)
lowercase_count = sum(char.islower() for char in sentence)

print(f"Word count: {word_count}")
print(f"Digit count: {digit_count}")
print(f"Uppercase count: {uppercase_count}")
print(f"Lowercase count: {lowercase_count}")
words=digits=lower=upper=0
for c in sentence:
    if c.isdigit():
        digits += 1
    elif c.islower():
        lower+=1
    elif c.isupper():
        upper+=1

print(word_count)
print(digits)
print(lower)
print(upper)
