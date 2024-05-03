# String Validators

if __name__ == '__main__':
  s = input()
  
  hasAlnum = False
  hasAlpha = False
  hasDigit = False
  hasLower = False
  hasUpper = False
  
  for i in range(len(s)):
    if s[i].isalnum():
      hasAlnum = True
      if s[i].isalpha():
        hasAlpha = True
        if s[i].islower():
          hasLower = True
        else:
          hasUpper = True
      else:
        hasDigit = True
    if hasAlnum and hasAlpha and hasDigit and hasLower and hasUpper:
      break
    
  print(hasAlnum)
  print(hasAlpha)
  print(hasDigit)
  print(hasLower)
  print(hasUpper)
