vowels = ['a', 'e', 'i', 'o', 'u']
text = input()

for char in text:
    if char in vowels:
        print('vowel')
    elif 'a' <= char <= 'z':
        print('consonant')
    else:
        break
