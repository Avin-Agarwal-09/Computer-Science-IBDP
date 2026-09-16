print("Enter a word")
word = input()
OppWord = ""
for i in range(0, len(word)):
   OppWord = OppWord + word[len(word) - i - 1]
print(OppWord)
if OppWord.lower() == word.lower():
   print("Yes")
else:
   print("No")
