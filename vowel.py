x=input()
a=['a','e','i','o','u','A','E','I','O','U']
if ((x>='a' and x<='z') or (x>='A' and x<='Z')):
  if x in a:
    print("vowel")
  else:
    print("consonant")
  else:
    print("invalid")
   
