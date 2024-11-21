def numeros():
    l = input("Ingrese números separados por comas: ")
    lista = l.split(",")
    numeros = [int(x) for x in lista]
    return numeros

def sumas(numeros):
    r = []
    for i in range(len(numeros) - 1):
        r.append(numeros[i] + numeros[i + 1])
    return r

def mayor_que(r):
  m=0
  for i in range(len(r)):
    if r[i]>m:
      m=r[i]
  return m

lista = numeros()

r=sumas(lista)
print(r)
print(mayor_que(r))