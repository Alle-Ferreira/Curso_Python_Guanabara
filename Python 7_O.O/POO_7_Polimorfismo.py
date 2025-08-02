'''
Conceitos de POO:

3. Polimorfismo: 

Permite que objetos de diferentes classes sejam tratados como objetos da mesma classe base.
- É alcançado através da sobrescrita de métodos.
- Permite que uma mesma operação tenha comportamentos diferentes em classes diferentes.

Exemplo:
len('python')        considera cada caracter da string
len([10, 20, 20])    considera cada elemento da lista


3.1. Polimorfismo com Herança:

Na herança, a classe filho herdará os métodos da classe pai. E o polimorfismo adaptará o método à classe filho.

Leitura prioritária: 
filho, depois pai.
neto, filho, depois pai.
'''

class Ave:
   def voar(self):
      pass                 # função propositadamente não especificada.

class Pardal(Ave):
   def voar(self):
      print('Pardal voa')

class Avestruz(Ave):
   def voar(self):
      print('Avestruz não voa')

class Aviao:
   def voar(self):
      print('Aviao decolando...')

def plano_voo(objeto):     # função com polimorfismo, fora das classes
   objeto.voar()

passaro_1 = Pardal()
passaro_2 = Avestruz()
aviao_1 = Aviao()

plano_voo(passaro_1)
plano_voo(passaro_2)
plano_voo(aviao_1)
print()
plano_voo(Pardal())
plano_voo(Avestruz())
plano_voo(Aviao())
print()