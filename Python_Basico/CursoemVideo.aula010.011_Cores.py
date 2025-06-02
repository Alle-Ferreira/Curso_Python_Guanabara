'''
Aula 010: Estrutura Condicional Simples
if / else

Aula 011: Cores

1. Cores com ANSI Escape Sequance: 
O código melhor compatível com Python é o 033:

Sintaxe padrão:     \033[Style;Texto;Backm
                    \033[0;33;44m

Style:
[1] bold (negrito)
[4] underline (sublinhado)
[7] negative (inverte as configuarações letra/fundo)

Texto:
[30] Branco
[31] Vermelho
[32] Verde
[33] Amarelo
[34] Azul
[35] Roxo
[36] Ciano
[37] Cinza

Back:
[40] Branco
[41] Vermelho
[42] Verde
[43] Amarelo
[44] Azul
[45] Roxo
[46] Ciano
[47] Cinza

Padrão '\033[m': fundo preto; letra cinza
Inversao '\033[7:30m' :  7 inverte o fundo preto p/ branco, da letra selecionada (30)
'''

print('\033[36mOla, Mundo!')

# colore no inicio, retorna para o padrão no final:
print('\033[1;31;43mOlá, Mundo!\033[m') 


'''
2. Cores com Biblioteca

'''
