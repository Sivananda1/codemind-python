s=input()
Vowel=0
Consonants=0
Digits=0
Whitespaces=0
a="aeiou"
n='0123456789'
l=" "
for i in range(len(s)):
    if s[i] in a:
        Vowel+=1
    elif s[i] in n:
        Digits+=1
    elif s[i] in l:
        Whitespaces+=1
    else:
        Consonants+=1
print("Vowels:",Vowel)
print("Consonants:",Consonants)
print("Digits:",Digits)
print("White spaces:",Whitespaces)