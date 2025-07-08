# 1) Função para contar número de divisores:

def conta_divisores_rec(n, d):
    if d == 1:
        return 1
    else:
        if n % d == 0:
            return 1 + conta_divisores_rec(n, d-1)
        else:
            return 0 + conta_divisores_rec(n, d-1)
        
def cont_divisores(n):
    return conta_divisores_rec(n, n)
    

a = int(input())
quant_divisores = cont_divisores(a)
print (quant_divisores)

# -------------------------------------------------------------------------------------------------------------------

# 2) Função para indentificar primo:

def conta_divisores_rec(n, d):
    if d == 1:
        return 1
    else:
        if n % d == 0:
            return 1 + conta_divisores_rec(n, d-1)
        else:
            return 0 + conta_divisores_rec(n, d-1)
        
def primo(n):

    if conta_divisores_rec (n,n) == 2:
        return "É primo"
    else:
        return "Não é primo"
    
a = int(input())
resultado = primo(a)
print (resultado)

# -------------------------------------------------------------------------------------------------------------------

# 3) Função para calcular a média so quando o maior valro for x:

def f(x,y):
    if (x>=y):
        return (x+y)/2
    else:
        return f(f(x+2,y-1),f(x+1,y-2))
    
a = 1
b = 8
resultado = f(a,b)
print (resultado)

# f(1,8)
# 1>=8 (falso)
# f(f(1+2, 8-1)),f(1+1, 8-2)  (isso vaiacontecer ater chegar nos valores x = 5 e y = 4)
# logo sera calulado a média
# 5+4/2
# 4.5

# a função calcula a média dos dois números, porém so quando o maior número estiver na variavel x

# -------------------------------------------------------------------------------------------------------------------

# 4) Função conta algarismos:

def conta_algarismos(n):
    if n < 10:
        return 1
    else:
         return 1 + conta_algarismos(n//10)

a = int(input())
n_algarismos = conta_algarismos(a)
print (n_algarismos)

# -------------------------------------------------------------------------------------------------------------------

# 5) Função conta algarismos (binarios):

def conta_bits(n):
    if n < 2:
        return 1
    else:
         return 1 + conta_bits(n//2)

a = int(input())
n_algarismos = conta_bits(a)
print (n_algarismos)

# -------------------------------------------------------------------------------------------------------------------

# 6) 

# -------------------------------------------------------------------------------------------------------------------

# 7) Função lista de divisores:

def divisores(n, k=1, lista=[]):
    if n == k:
         lista.append(k)
         return lista
    else:
        if n % k == 0:
            lista.append(k)
            return divisores(n,k+1, lista)
        elif n % k != 0:
            return divisores(n, k+1,lista)
        

a = int(input())
resultado = divisores(a)
print (resultado)

# -------------------------------------------------------------------------------------------------------------------

# 8) Função indice maior elemento:   

def indice_do_maior(lista):
     def indice_recursiva(indice_atual=len(lista)-1, indice_maior=len(lista)-1):
        if indice_atual < 0:
            return indice_maior
        
        if lista[indice_atual] > lista[indice_maior]:
            indice_maior = indice_atual
        
        return indice_recursiva(indice_atual - 1, indice_maior)
     return indice_recursiva()
        
lista = list(map(int, input(). split()))
resultado = indice_do_maior(lista)
print (resultado)
            
# -------------------------------------------------------------------------------------------------------------------

# 9) Função soma pares:   

def soma_pares(lista): 
    if len(lista) == 0: 
        return 0 
    if lista[-1] % 2 == 0: 
        return lista[-1] + soma_pares(lista[:-1]) 
    else: 
        return soma_pares(lista[:-1]) 
    
lista = list(map(int, input(). split()))
resultado = soma_pares(lista)
print (resultado)

# -------------------------------------------------------------------------------------------------------------------

# 10) Função ordenar:  

def ordenada(lista, trocas = 0): 
    if len(lista) == 1: 
        if trocas == 0: 
            return True 
        if trocas > 0: 
            return False 
    if lista[-1] > lista[-2]: 
        return ordenada(lista[:-1], trocas) 
    else: 
        return ordenada(lista[:-1], trocas + 1) 

# -------------------------------------------------------------------------------------------------------------------

# 11) Função primos:  

def primos(lista, lista_primo = []): 
    if len(lista) == 0: 
        return lista_primo 
    if primos(lista[-1]) is True: 
        lista_primo.append(lista[-1]) 
        return primos(lista[:-1], lista_primo) 
    else: 
        return primos(lista[:-1], lista_primo)

# -------------------------------------------------------------------------------------------------------------------

# 12) Função ocorrencias:

def ocorrencias(lista, x): 
    if len(lista) == 0: 
        return 0 
    if lista[-1] == x: 
        return 1 + ocorrencias(lista[:-1], x) 
    else: 
        return 0 + ocorrencias(lista[:-1], x) 

# -------------------------------------------------------------------------------------------------------------------

# 13) Função inverter lista:

def inverter_lista(lista, i = 0): 
    if i == len(lista)//2: 
        return lista 
    else: 
        lista[i], lista[-1 - i] = lista[-1 - i], lista[i] 
        return inverter_lista(lista, i + 1)

# -------------------------------------------------------------------------------------------------------------------

# 14) Função polidromo:

def palindromo(s, i = 0): 
    if i == len(s)//2: 
        return True 
    if s[i] != s[-1 -i]: 
        return False 
    if s[i] == s[-1 -i]: 
        return palindromo(s, i + 1)


