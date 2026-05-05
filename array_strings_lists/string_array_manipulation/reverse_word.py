#Write a function reverseWords(sentence) that takes a string sentence and returns a new string where each individual word is reversed, 
# but the word order remains the same.

def reverseWords(sentence):
    stack = []
    result = ""

    for i in range(len(sentence)):
        char = sentence[i]
        if char != " ":
            stack.append(char)
        else:
            reversed = ""
            while stack:
                reversed += stack.pop()
            result += reversed + " "
    
    reversed = ""
    while stack:
        reversed += stack.pop()
    result += reversed


    return result

sentence = "IB Computer Science"
print(reverseWords(sentence))

# hello world
# olleh dlorw