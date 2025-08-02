'''I - Tratamento e de Textos'''

import unicodedata
import string


'''1. Remoção de Acentos: normaliza os caracteres e remove os acentos
Converte caracteres como "á", "é", "ç" para "a", "e", "c".'''

def remover_acentos(texto):
   
    return ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    )


'''2. Remoção de Pontuação: retira vírgulas e pontos'''

def remover_pontuacao(texto):
    return ''.join(c for c in texto if c not in string.punctuation)


'''3. Remoção de espaços, pontuação, e acentuação + Padronização do tamanho das letras'''

def remover_acentos(texto):                                 # Remoção de Acentos
    return ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    )

def remover_pontuacao(texto):                               # Remoção de Pontuação
    return ''.join(c for c in texto if c not in string.punctuation)


'''Main Program Example:

frase = 'colocar a frase a ser tratata aqui'
frase_tratada = remover_acentos(frase.replace(" ", ""))     # Chamada função + 'Replace' (remove caracteres vazios)
frase = input("Digite uma frase: ").strip().lower()         # Remove espaços antes/depois; coloca td minusculo
frase_tratada = frase.replace(" ", "")                      # remove espaços entre as palavras
frase_tratada = remover_acentos(frase_tratada)              # chama def remove acentos
frase_tratada = remover_pontuacao(frase_tratada)            # chama def remove pontuação
'''