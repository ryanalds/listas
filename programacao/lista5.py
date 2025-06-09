# Corrida:

# c1, distância1, velocidade1 = map(int,input().split())
# c2, distância2, velocidade2 = map(int,input().split())
# tempo1 = distância1/velocidade1
# tempo2 = distância2/velocidade2

# if tempo1 < tempo2:
#     print (c1)
# else:
#     print (c2)

#--------------------------------------------------------------------------------------------------------------------------

# Interceptando informações:

# n1, n2, n3, n4, n5, n6, n7, n8 = map(int,input().split())

# if n1==9 or n2==9 or n3==9 or n4==9 or n5==9 or n6==9 or n7==9 or n8==9:
#     print("F")
# else: 
#     print("S")

#--------------------------------------------------------------------------------------------------------------------------

# Piloto automático:

# a = int(input())
# b = int(input())
# c = int(input())

# if b-a < c-b:
#     print(1)
# elif c-b < b-a:
#     print(-1)
# else:
#     print (0)

#--------------------------------------------------------------------------------------------------------------------------

# A idade da Dona Monica:

# idade_monica = int(input())
# idade_f1 = int(input())
# idade_f2 = int(input())
# idade_f3 = idade_monica - (idade_f1+idade_f2)

# list = idade_f1, idade_f2, idade_f3
# maior = idade_f3
# for item in list:
#     if item > maior:
#         maior = item
# print(maior)

#--------------------------------------------------------------------------------------------------------------------------

# Conta de água:

# consumo_m3 = int(input())

# if consumo_m3 <= 10:
#     consumo_final = 7

# elif consumo_m3 > 10 and  consumo_m3 <= 30:
#     consumo_final = 7+((consumo_m3-10)*1)

# elif consumo_m3 > 30 and consumo_m3 <= 100:
#     consumo_final = 27+((consumo_m3-30)*2)

# elif consumo_m3 > 100:
#     consumo_final = 167+((consumo_m3-100)*5)

# print (consumo_final)

#--------------------------------------------------------------------------------------------------------------------------

# Escolha difícil:

# refeições_f, refeições_b, refeições_m = map(int,input().split())
# pedido_f, pedido_b, pedido_m = map(int,input().split())

# if pedido_f > refeições_f:
#     sobra_f = pedido_f-refeições_f
# elif pedido_f <= refeições_f:
#     sobra_f = 0 

# if pedido_b > refeições_b:
#     sobra_b = pedido_b-refeições_b
# elif pedido_b <= refeições_b:
#     sobra_b = 0 

# if pedido_m > refeições_m:
#     sobra_m = pedido_m-refeições_m
# elif pedido_m <= refeições_m:
#     sobra_m = 0 

# print (sobra_f+sobra_b+sobra_m)

#--------------------------------------------------------------------------------------------------------------------------

# Andando no tempo:

# a, b, c = map(int, input().split())
# creditos = [a, b, c]

# if a == 0 or b == 0 or c == 0:
#     print("S")
#     exit()

# if a + b == 0 or a - b == 0 or -a + b == 0 or -a - b == 0:
#     print("S")
#     exit()

# if a + c == 0 or a - c == 0 or -a + c == 0 or -a - c == 0:
#     print("S")
#     exit()

# if b + c == 0 or b - c == 0 or -b + c == 0 or -b - c == 0:
#     print("S")
#     exit()


# sinais = [-1, 1]

# for s1 in sinais:
#     for s2 in sinais:
#         for s3 in sinais:
#             soma = s1 * a + s2 * b + s3 * c
#             if soma == 0:
#                 print("S")
#                 exit()

# print("N")

#--------------------------------------------------------------------------------------------------------------------------

# Dupla de Tênis:

# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())

# lista = [a,b,c,d]
# maior = lista[0]
# menor = lista[0]

# for item in lista:
#     if item > maior:
#         maior = item
# for item in lista:
#     if item < menor:
#         menor = item
# lista.remove(maior)
# lista.remove(menor)
# x,y = map(int, lista)

# diferença_1 = abs((maior+menor)-(x+y))
# diferença_2 = abs((maior+x)-(menor+y))
# diferença_3 = abs((maior+y)-(menor+x))

# print(min(diferença_1, diferença_2, diferença_3))

#--------------------------------------------------------------------------------------------------------------------------

# Máquina de café:

# anda_1 = int(input())
# anda_2 = int(input())
# anda_3 = int(input())

# tempo_no_1 = 0 * anda_1 + 2 * anda_2 + 4 * anda_3
# tempo_no_2 = 2 * anda_1 + 0 * anda_2 + 2 * anda_3
# tempo_no_3 = 4 * anda_1 + 2 * anda_2 + 0 * anda_3

# print(min(tempo_no_1, tempo_no_2, tempo_no_3))

#--------------------------------------------------------------------------------------------------------------------------

# Capital:

# from itertools import permutations

# areas = list(map(int, input().split()))

# for p in permutations(areas):
#     a1, a2, a3, a4 = p
#     if a1 * a4 == a2 * a3:
#         print("S")
#         break
# else:
#     print("N")
