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

#Blobs:

# n = int(input())
# lista = []
# dias = 0
# total_dias = []
# for i in range(n):
#     lista.append(float(input()))

# for i in range(len(lista)):
#     dias = 0
#     while not lista[i] <= 1:
#         lista [i] = lista[i] / 2
#         dias += 1
#     total_dias.append(dias)
    
# for i in total_dias:
#     print(i,'dias')
#------------------------------------------------------------------------------------------------
#Alarme despertador:

# lista_tempo = []
 
# while True:
#     h_1,m_1,h_2,m_2 = map(int,input().split())
#     if h_1 != 0 or h_2 != 0 or m_1 != 0 or m_2 != 0:
#         if h_1 < h_2:
#             lista_tempo.append((((h_2 - h_1) * 60)+ m_2 - m_1))
#         if h_1 > h_2:
#                 lista_tempo.append((((23 + h_2 - h_1)* 60)+ (60- m_1 + m_2)))
#         if h_1 == h_2:
#             if m_1 > m_2:
#                 lista_tempo.append(1380 + (60- m_1 + m_2))
#             else:
#                 lista_tempo.append(m_2 - m_1)
 
#     else:
#         for i in lista_tempo:
#             print(i)
#         break
#------------------------------------------------------------------------------------------------------

#Troco:

# casos_teste = int(input())
# troco = []
# troco_max = []
# for i in range(casos_teste):
#     valor,marca = map(int,input().split())
#     precos = list(map(float,input().split()))[:marca]
#     for i in range(len(precos)):
#         if valor >= precos[i] and precos[i] != 0:
#             troco.append(valor%precos[i])
#         else:
#             continue
#     if troco:
#         troco_max.append(max(troco))
#         troco.clear()
#     else: 
#         troco_max.append(0.0)
# for j in troco_max:
#     print(f'{j:.2f}')

#------------------------------------------------------------------------------------------------------

# Loop musical:

# def loop(num):

#     lista_frequencias = list(map(int, input().split()))[:num]

#     picos = 0

#     lista_frequencias.insert(0, lista_frequencias[-1])
#     lista_frequencias.append(lista_frequencias[1])

#     for i in range(0, len(lista_frequencias)-2):

#         if lista_frequencias[i] > lista_frequencias[i+1] < lista_frequencias[i+2]:
#             picos += 1

#         if lista_frequencias[i] < lista_frequencias[i+1] > lista_frequencias[i+2]:
#             picos += 1

#     return picos

# lista_picos = []

# while True:
#     numero = int(input())
#     if numero == 0:
#         break
#     else:
#         lista_picos.append(loop(numero))

# for valor in lista_picos:
#     print(valor) 

#------------------------------------------------------------------------------------------------------

# Senha:

# def senha():

#     num = int(input())
#     lista_oleosidade = list(map(float, input().split()))
#     lista_indice = []
#     i = 0

#     while i < num:

#         maior = lista_oleosidade.index(max(lista_oleosidade))
#         lista_oleosidade[maior] = 0
#         lista_indice.append(maior)

#         i += 1

#     return lista_indice

# senhas = []

# while True:
#     try:
#         senhas.append(senha())
#     except EOFError:
#         break

# for i in range(len(senhas)):
#     print(f'Caso {i+1}: {"".join(map(str, senhas[i]))}')

#------------------------------------------------------------------------------------------------------

# Mergulho:

# a, b = map(int, input().split())

# lista_voltaram = list(map(int, input().split()))

# lista_mergulhadores = []

# lista_morreram = []

# mortos = ''

# for i in range(1, a + 1):
#     lista_mergulhadores.append(i)

# for mergulhador in lista_mergulhadores:
#     if mergulhador not in lista_voltaram:
#         mortos += str(mergulhador ) +' '

# if len(lista_voltaram) == len(lista_mergulhadores):
#     print('*')
# else:
#     print(mortos) 
