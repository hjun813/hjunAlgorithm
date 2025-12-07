num = int(input())
word = []
sortedWord = []
finalWord = []

for i in range(num):
    word.append(input())

sortedWord = set(word)
finalWord = sorted(sortedWord, key=lambda x: (len(x), x))


for w in finalWord:
     print(w)