word = input('Enter word: ')
print('original string: ',word)

x = list(word)
for i in x[0::2]:
    print(i)