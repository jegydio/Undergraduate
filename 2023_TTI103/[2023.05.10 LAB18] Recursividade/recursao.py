# =============================================================================
# Multiplicação Recursiva (x, y são >= 0)
# =============================================================================
def mult_rec(x, y):
    if x == 0 or y == 0:
        return 0
    return y + mult_rec(x-1, y)

# Testes
print('-- Multiplicação recursiva --')
print(mult_rec(4, 6))
print(mult_rec(5, 1))
print(mult_rec(0, 456))

# =============================================================================
# Imprime asteriscos com recursividade (n >= 0)
# =============================================================================
def imprime_asteriscos(n):
    if n > 1:
        imprime_asteriscos(n-1)
    print('*'*n)

# Testes
print('-- Impressão de asteriscos [recursivo] --')
imprime_asteriscos(10)
imprime_asteriscos(0)

# =============================================================================
# Máximo valor em uma lista
# =============================================================================
def max_valor(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        primeiro = lista[0]
        max_demais = max_valor(lista[1:])
        if max_demais > primeiro:
            return max_demais
        else:
            return primeiro

def max_valor2(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        max_demais = max_valor(lista[1:])
        return max_demais if max_demais > lista[0] else lista[0]
# Testes
print('-- Máximo valor em uma lista [recursiva] --')
print(max_valor([-3, 4, 6, 90, 45]))
print(max_valor([-5]))
print(max_valor2([-3, 4, 6, 90, 45]))
print(max_valor2([-5]))

# =============================================================================
# Soma recursiva dos elementos de uma lista
# =============================================================================
def soma_lista(lista):
    if len(lista) == 0:
        return 0
    else:
        return lista[0] + soma_lista(lista[1:])

def soma_lista2(lista):
    return 0 if len(lista) == 0 else lista[0] + soma_lista(lista[1:])

# Testes
print('-- Soma recursiva de elementos em uma lista --')
print(soma_lista([]))
print(soma_lista([2]))
print(soma_lista([-5, 0, 4, 6]))
print(soma_lista2([]))
print(soma_lista2([2]))
print(soma_lista2([-5, 0, 4, 6]))

# =============================================================================
# Soma recursiva de todos os inteiros até n (n >= 0)
# =============================================================================
def soma_todos(n):
    return 1 if n == 1 else n + soma_todos(n-1)

def soma_todos2(n):
    if n > 1:
        return n + soma_todos2(n-1)
    elif n == 1:
        return 1
    else:
        raise Exception('Número negativo')

# Testes
print('-- Soma recursiva de todos os inteiros até n --')
print(soma_todos(1))
print(soma_todos(10))
print(soma_todos2(50))

# =============================================================================
# Potência recursiva
# =============================================================================
def potencia(x,y):
    if y == 0:
        return 1
    elif y == 1:
        return x
    else:
        return x * potencia(x, y-1)

# Testes
print('-- Potência recursiva --')
print(potencia(3, 0))
print(potencia(4, 1))
print(potencia(3, 4))