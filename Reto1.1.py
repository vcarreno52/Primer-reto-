def operaciones(n1,n2,s):
  n1 = int(input("ingrese el primer numero: "))
  n2 = int(input("ingrese el segundo numero: "))
  s = input("ingrese la operacion: ")
  if s == "+":
    r = (n1 + n2)

  if s == "-":
    r = (n1 - n2)

  if s == "*":
    r = (n1 * n2)

  if s == "/":
    r = (n1 / n2)
  return r

print(operaciones(1,2,3))

