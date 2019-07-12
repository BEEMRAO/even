x=input()
a=['a','e','i','o','u','A','E','I','O','U']
if ((x>='a' and x<='z') or (x>='A' and x<='Z')):
  if x in a:
    print("Vowel")
  else:
    print("Consonant")
  else:
    print("invalid")
   
