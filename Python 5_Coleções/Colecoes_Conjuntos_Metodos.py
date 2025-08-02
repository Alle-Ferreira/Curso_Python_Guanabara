# Conjuntos / Set: Métodos

# 3. Operações com SET:

# 3.1. {}.union: agrupa os conjuntos.

conjunto_a = {1, 2}
conjunto_b = {3, 4}

print(conjunto_a.union(conjunto_b))
print()


# 3.2. {}.interserction: identifica os objetos comuns aos conjuntos.

conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

print(conjunto_a.intersection(conjunto_b))
print()


# 3.3. {}.difference
# Identifica os objetos de um conjunto, ausentes noutro conjunto.

conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

print(conjunto_a.difference(conjunto_b)) # {1}
print(conjunto_b.difference(conjunto_a)) # {4}
print()


# 3.4. {}.symmetric_difference
# Identifica as diferenças entre os conjuntos.

conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

print(conjunto_a.symmetric_difference(conjunto_b)) # {1, 4}
print()


# 3.5. {}.issubset: 'está contido'
# Considera a relação de subconjunto

conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4, 1, 5, 6}

print(conjunto_a.issubset(conjunto_b)) # True
print(conjunto_b.issubset(conjunto_a)) # False
print()


# 3.5. {}.issuperset: 'contém'
# Considera a relação de subconjunto

conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4, 1, 5, 6}

print(conjunto_a.issuperset(conjunto_b)) # False
print(conjunto_b.issuperset(conjunto_a)) # True
print()


# 3.6. {}.isdisjoint: 'está separado'
# Considera a separação entre conjuntos diversos.

conjunto_a = {0, 1, 2, 3, 4}
conjunto_b = {5, 6}
conjunto_c = {7, 8, 9, 0}

print(conjunto_a.isdisjoint(conjunto_b)) # True
print(conjunto_a.isdisjoint(conjunto_c)) # False
print()


# 3.7. {}.add: 
# Adiciona apenas quando o objeto NAO existir no set/conjunto.

conjunto_a = {0, 1, 2, 3, 4}

conjunto_a.add(5) # {0, 1, 2, 3, 4, 5}
conjunto_a.add(6) # {0, 1, 2, 3, 4, 5, 6}
conjunto_a.add(1) # {0, 1, 2, 3, 4, 5, 6}
print(conjunto_a)
print()


# 3.8. # {}.discard
# Descarta o objeto e as duplicações do objeto.
# Se o objeto definido como parametro nao existir, ele apenas ignora.

numeros= {0, 1, 2, 3, 4, 0, 1, 2, 0, 1}

print(numeros)
numeros.discard(0) # {1, 2, 3, 4}
print(numeros)
numeros.discard(1) # {2, 3, 4, 2}
print(numeros)
numeros.discard(7) # {2, 3, 4, 2}
print(numeros)
print()


# 3.9. # {}.remove
# Remove o objeto especificado.
# Ao contrário do discard, se não existir o objeto, dará erro.

numeros.remove(2)
print(numeros)
print()


# 3.10. Outros métodos:

numeros= {1, 2, 3, 4, 5, 6, 1, 2}

# Len: 
# Valcula o tamanho do conjunto, ignorando as duplicações.
print(len(numeros)) #6
print()

# In:
# Avalia o pressuposto da existencia.
print(1 in numeros)     # True
print(10 in numeros)    # False
print()

# {}.copy: copia o conjunto todo 
numeros.copy()
print(numeros)
print()

# {}.pop: remove o objeto que estiver na 1a posição do conjunto.
numeros.pop()
print(numeros)
print()

# {}.clear: limpa o conjunto todo
numeros.clear()
print(numeros)
print()