i = 0
word = input("wort: ")
for char in word:
    if char not in word[i+1 : len(word)] and char not in word[0 : i]:
        print(char)
        break
    i = i+1
