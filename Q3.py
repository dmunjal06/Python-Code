string=input("STRING:")
vowel=['a','e','i','o','u','A','E','I','O','U']
result=''
for i in range(len(string)):
    if string[i] not in vowel:
       result=result+string[i]
print("After Removing Vowels:",result)
