# Maior de 5:
# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# e = int(input())
# maior = a
# valores = [a,b,c,d,e]
# for item in valores:
#     if item >= maior:
#         maior = item

# print (maior)

# ---------------------------------------------------------------------------------------------------------------------------------------

# Tanque de combustivel:
# consumo = int(input())
# distancia = int(input())
# gasolina_no_tanque = int(input())

# compra_gasolina = (distancia/consumo)

# if gasolina_no_tanque >= (compra_gasolina):
#         print(0.0)
# elif gasolina_no_tanque < (compra_gasolina):
#         compra_gasolina = (distancia/consumo)-gasolina_no_tanque   
#         print(f"{compra_gasolina:.1f}")

# ---------------------------------------------------------------------------------------------------------------------------------------

# Xadrez:
# a = int(input())
# b = int(input())
# casa = a*b

# if a%2 == 0 and b%2 == 0:
#     casa_nova = casa+1
#     if casa_nova%2 == 0:
#         print (0)
#     else:
#         print(1)

# elif a%2 != 0 or b%2 != 0:
#     casa_nova = casa
#     if casa_nova%2 == 0:
#         print (0)
#     else:
#         print(1)

# ----------------------------------------------------------------------------------------------------------------------------------------

# Maior media ponderada:
# a11, a21 = map(int, input() .split())
# a12, a22 = map(int, input() .split())
# p1, p2 = map(int, input() .split())

# media_1 = ((a11*p1)+(a21*p2))//(p1 + p2)
# media_2 = ((a12*p1)+(a22*p2))//(p1 + p2)

# if media_1 >= media_2:
#     print (1)
# else:
#     print (2)

# ----------------------------------------------------------------------------------------------------------------------------------------

# Idade de Camila:

# idade_1 = int(input())
# idade_2 = int(input())
# idade_3 = int(input())

# if (idade_1 <= idade_2 and idade_1 >= idade_3) or (idade_1 <= idade_3 and idade_1 >= idade_2):
#     print(idade_1)
# elif (idade_2 <= idade_1 and idade_2 >= idade_3) or (idade_2 <= idade_3 and idade_2 >= idade_1):
#     print (idade_2)
# elif (idade_3 <= idade_1 and idade_3 >= idade_2) or (idade_3 <= idade_2 and idade_3 >= idade_1):
#     print (idade_3)
# else: 
#     print(idade_1)

# ----------------------------------------------------------------------------------------------------------------------------------------

# Teleférico:

# capacidade = int(input())
# n_alunos = int(input())

# viagens = n_alunos / (capacidade-1)

# if viagens == int(viagens):
#     print(int(viagens))
# else:
#     viagens_1 = int(viagens + 1)
#     print(viagens_1)

# ----------------------------------------------------------------------------------------------------------------------------------------

# Triângulos:

# valores = list(map(int, input().split()))
# valores.sort()

# a, b, c = valores  

# if a + b <= c:
#     print('n')
# else:
#     a2, b2, c2 = a**2, b**2, c**2
#     if a2 + b2 == c2:
#         print('r')
#     elif a2 + b2 > c2:
#         print('a')
#     else:
#         print('o')

# ----------------------------------------------------------------------------------------------------------------------------------------
