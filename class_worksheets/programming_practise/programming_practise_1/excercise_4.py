print("Enter String")
inputString = input()
a = 0
e = 0
i = 0
o = 0
u = 0
import string
for char in inputString.lower:
   if char == 'a':
       a += 1
   elif char == 'e':
       e += 1
   elif char == 'i':
       i += 1
   elif char == 'o':
       o += 1
   elif char == 'u':
       u += 1
print(a,e,i,o,u)
