# Senha de acesso:

# while True:
#     senha = int(input())
#     if senha == 9842:
#         print("Acesso Permitido.")
#         break
#     else:
#         print("Senha Invalida!")

# -------------------------------------------------------------------------------------------------------------------

# Meia Vida:

# s, m = map(int, input().split())

# tempo = 0 
# while True:
#     if m < 0.5:
#         break
       
#     else:
#         m = m/2
#         tempo = tempo + s


# horas = tempo // 3600
# dias = horas//24
# if horas >= 24:
#     horas = horas % 24
# minutos = (tempo % 3600) // 60
# segundos = tempo % 60

# print(f"{dias} dias {horas:02}:{minutos:02}:{segundos:02}")

# -------------------------------------------------------------------------------------------------------------------

# Pula sapo:

# p, n = map(int,input().split())
# h_canos = list(map(int,input().split()))
# diferenças = []
 
# for i in range (len(h_canos)-1):
#     y = h_canos[i] - h_canos[i+1]
#     diferenças.append(y)
 
# for i in diferenças:
#     if i > p or i < -p:
#         print("GAME OVER")
#         break
 
# else:
#     print("YOU WIN")

# -------------------------------------------------------------------------------------------------------------------

# Primos:

# n = int(input())
# divisores= []
# def eh_primo(n):
#     if n < 2:
#         return False
#     for i in range(2, n-1):
#         if n % i == 0:
#             return False
#     return True
 
# while True:
#     if eh_primo(n+1):
#         print(n+1)
#         break
#     else:
#         n = n+1

# -------------------------------------------------------------------------------------------------------------------

# 