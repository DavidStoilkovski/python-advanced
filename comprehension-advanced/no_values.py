text = input()

vowels = {'a', 'e', 'i', 'o', 'u'}
vowels_upper = {el.upper() for el in vowels}
vowels = vowels_upper.union(vowels)


no_vowels = [ch for ch in text if ch not in vowels]

print(''.join(no_vowels))