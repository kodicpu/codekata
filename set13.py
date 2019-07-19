a=input()
vowels=['a','e','i','o','u','A','E','I','O','U']
if a.isalpha() == True:
    if a in vowels:
        print ("Vowel")
    else:
        print ("Consonant")
else:
    print ("invalid")
