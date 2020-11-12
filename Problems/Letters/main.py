word = input()  # the input word
letter_set = set()
for letter in word:
    letter_set.add(letter)
print(len(letter_set))
