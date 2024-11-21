def palindromo():
  p = str(input("Ingrese una palabra"))
  for i in range(len(p)):
    if p[i]!=p[(len(p)-1)-i]:
      return False
  return True

print(palindromo())

