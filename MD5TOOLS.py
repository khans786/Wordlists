import hashlib

def MD5encryptor():
  print("""*****MD5 Encryptor*****""")
  print("Coded and created by SHAHVEZ KHAN!!\n")
  
  print()
  print()
  
  try:
    input("Press enter to continue\n")
    print()
    print()
  except SyntaxError:
    pass
    
  phrase = input("Enter a phrase to find the MD5 value of it:\n")
  
  phrasemd5 = hashlib.md5(phrase.encode()) 
  hexval = phrasemd5.hexdigest()
  
  print()
  
  print("The hexadecimal value equivalent to that MD5 hash is:",(hexval))
  print()

  cont = input("Would you like to continue? If yes, press y else press n\n")

  if cont == "y":
    MD5encryptor()
  else:
    menu()
  return 0


def MD5decryptor():
  print("""*****MD5 Decryptor*****""")
  print("Coded and created by SHAHVEZ KHAN!!\n")
  
  print()
  print()
  
  try:
    input("Press enter to continue\n")
    print()
    print()
  except SyntaxError:
    pass

  counter = 1
  md5entered = input("MD5 hash here:")
  wrdlist = open("wordlist.txt","r")
  
  for password in wrdlist:
    filemd5 = hashlib.md5(password.strip().encode('utf-8')).hexdigest()
    print()
   
    print("Trying password ",(counter),":", (password.strip()))
     
    counter += 1
    
    if md5entered == filemd5:
        print("\nPassword found!!!")
        print("Password is:",password)
    else:
        print("\nPassword not found")

  print()

  cont = input("Would you like to continue? If yes, press y else press n\n")

  if cont == "y":
   MD5decryptor()
  else:
   print()
   menu()
  return 0
  

def menu():
  userinp = input("Hello, For MD5 encryptor press 1, For MD5 decryptor press 2, Else press q to exit this program:\n")
  if userinp == "1":
    MD5encryptor()
  elif userinp == "2":
    MD5decryptor()
  elif userinp == "q":
    quit()
  else:
    print("Invaid entry, Please choose option 1 or 2.")
    menu()
  return 0

if __name__ == "__main__":
  menu()




