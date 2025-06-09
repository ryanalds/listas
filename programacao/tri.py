a,b,c = map(int, input().split())
lista = [a,b,c]
lista.sort()
x,y,z = map(int, lista)
if x + y > z:
    print ("fecha")
else:
    print ("nao fecha")