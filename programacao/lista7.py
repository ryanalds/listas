# Tabuada de N:

# n = int(input())

# for x in range(1,11):
#     print(f"{x} x {n} = {x*n}")

# -----------------------------------------------------------------------------------------------------------------------------------------------

#  Somatorio:

# n = int(input())

# soma= 0
# for i in range(1,n+1):
#     soma += 1/i 
 
# print(f"{soma:.4f}")

# -----------------------------------------------------------------------------------------------------------------------------------------------

# Multiplos I:

# a, b = map(int, input().split())


# for i in range(1, b+1):
#         multiplos = a*i
#         if multiplos <= b:
#             print(multiplos, end=" ")

# -----------------------------------------------------------------------------------------------------------------------------------------------

# Divisores: 

# n = int(input())

# for i in range(1,n+1):
#      if n%i == 0:
#             print (i, end= " ")


# -----------------------------------------------------------------------------------------------------------------------------------------------

#  Media:

# n = int(input())
# lista = list(map(int,input().split()))

# soma = 0
# quant_maior =  0
# quant_menor = 0
# for i in lista:
#     soma += i
#     media = soma/n

# for i in lista:
#     if (i < media):
#         quant_menor = quant_menor + 1
#     elif (i >= media):
#         quant_maior = quant_maior + 1


# print(f"{media:.1f}")
# print (quant_menor)
# print (quant_maior)

# -----------------------------------------------------------------------------------------------------------------------------------------------

# Primo facil:

# n = int(input())

# divisores = 0
# for i in range(1,n+1):
#     if n%i == 0:
#         divisores += 1

# if divisores == 2:
#     print("Sim")
# else:
#     print("Nao")

# ---------------------------------------------------------------------------------------------------------------------------------------------

# Media II:

# n = int(input())
# lista = list(map(int, input().split()))

# media = 0
# soma = 0
# quant_maior = []
# quant_menor = []
# for i in lista:
#     soma += i
#     media = soma/n
    
# print(f"{media:.1f}")

# for i in lista:
#     if i < media:
#         quant_menor.append(i)
 
#     elif i >= media:
#         quant_maior.append(i)
   

# print(len(quant_menor), *quant_menor)
# print(len(quant_maior), *quant_maior)

# -----------------------------------------------------------------------------------------------------------------------------------------------

#  Game show:

# n_caixas = int(input())

# caixas = []
# for i in range(n_caixas):
#     valor = (int(input()))
#     caixas.append(valor)

# for i in range(len(caixas)-1):
#     soma = caixas[i] + caixas[i+1]
#     caixas[i+1] = soma

# if max (caixas) + 100 >= 100:
#     print(max(caixas)+100)
# else: 
#     print(100)

# -----------------------------------------------------------------------------------------------------------------------------------------------
    
#  Desvendando monte Hall:

# n = int(input())
# porta_carro = []
# acerto = n
 
# for i in range(n):
#     porta = int(input())
#     porta_carro.append(porta)
#     if porta == 1:
#         acerto -= 1
# print(acerto)
   
# -----------------------------------------------------------------------------------------------------------------------------------------------

# n = int(input())
# coluna = []
# sequencia = n
 
# for i in range(n):
#     num = int(input())
#     coluna.append(num)
 
# for j in range(len(coluna)-1):
#     if coluna[j] == coluna[j+1]:
#         sequencia -= 1
#     else:
#         continue
# print(sequencia)