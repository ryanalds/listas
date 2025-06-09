# Soma Simples:

# def soma(a,b):
#     c = a+b
#     return c

#------------------------------------------------------------------------------------------------------------------

# Média:

# def media(a,b):
#     c = (a+b)//2
#     return c

#------------------------------------------------------------------------------------------------------------------

# Maior de 2:

# def maior2(a,b):
#     if a>b:
#         return a
#     else: 
#         return b

#------------------------------------------------------------------------------------------------------------------

# Maior de 5:

# def maior5(a,b,c,d,e):
#     lista = [a,b,c,d,e]
#     lista.sort()
#     maior = lista[4]
#     return maior
    
#------------------------------------------------------------------------------------------------------------------

# Dia da Semana:

# def dia_da_semana(h,d):
#     dias_da_semana = [ "Domingo", "Segunda-feira", "Terca-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sabado"]
#     indice_atual = dias_da_semana.index(h)
#     novo_indice = ( indice_atual + d) % len(dias_da_semana)
#     return dias_da_semana[novo_indice]

#------------------------------------------------------------------------------------------------------------------

#  Media Ponderada:

# def media_ponderada(v1, p1, v2, p2):
#     media = ((v1*p1)+(v2*p2))/(p1+p2)
#     return media

#------------------------------------------------------------------------------------------------------------------

# Dia por extenso:

# def dia(dia, mes, ano):
#     mesr = (f"{mes:02}")
#     dias = (f"{dia:02}")
#     if mesr == "01" and dia <= 31:
#         return (f"{dias} de janeiro de {ano}")
#     elif mesr == "02" and dia <= 28:
#         return (f"{dias} de fevereiro de {ano}")
#     elif mesr == "03" and dia <= 31:
#         return (f"{dias} de marco de {ano}")
#     elif mesr == "04" and dia <= 30:
#         return (f"{dias} de abril de {ano}")
#     elif mesr == "05" and dia <= 31:
#         return (f"{dias} de maio de {ano}")
#     elif mesr == "06" and dia <= 30:
#         return (f"{dias} de junho de {ano}")
#     elif mesr == "07" and dia <= 31:
#         return (f"{dias} de julho de {ano}")
#     elif mesr == "08" and dia <= 31:
#         return (f"{dias} de agosto de {ano}")
#     elif mesr == "09" and dia <= 30:
#         return (f"{dias} de setembro de {ano}")
#     elif mesr == "10" and dia <= 31:
#         return (f"{dias} de outubro de {ano}")
#     elif mesr == "11" and dia <= 30:
#         return (f"{dias} de novembro de {ano}")
#     elif mesr == "12" and dia <= 31:
#         return (f"{dias} de dezembro de {ano}")
#     else:
#         return ("Data Invalida")

#------------------------------------------------------------------------------------------------------------------

# Media:

# def media_lista(lista):
#     numero = len(lista)
#     soma = sum(lista)
#     media = int(soma / numero)
#     return media

#------------------------------------------------------------------------------------------------------------------

# Troca do menor:

# def lista_troca_menor_primeiro(lista):
#     if not lista:
#         return 0 
#     menor_valor = min(lista)
#     indice_menor = lista.index(menor_valor)
#     if indice_menor == 0:
#         return 0  
#     lista[0], lista[indice_menor] = lista[indice_menor], lista[0]
#     return 1

#------------------------------------------------------------------------------------------------------------------

# Remover menor:

# def sublista_sem_menor(lista):
#     menor_valor = min(lista)
#     nova_lista = lista.copy()
#     nova_lista.remove(menor_valor)
#     return nova_lista

