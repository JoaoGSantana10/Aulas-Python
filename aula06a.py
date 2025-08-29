# Aula 06 - Tipos de Primitivos e Saída de Dados

# int = números inteiros, EX: 7, -4, 0, 9875
# float = números com ponto flutuante (números decimais), EX: 4.5, 0.076, -15.223, 7.0
# bool = valores lógicos (True/False), EX: True, False
# str = textos (string), EX: 'Olá', '7.5', ''

n1 = int(input('Digite um número:'))
n2 = int(input('Digite outro número:'))
s = n1 + n2
# Para mostrar o valor da soma sem ficar com muita vírgula desse jeito: print('A soma entre,',n1, 'e', n2, 'vale: {}'.format(s))

# uma forma mais simples de fazer isso é:
print('A soma entre {} e {} vale: {}'.format(n1, n2, s))

# Para ver o tipo da Váriavel que esta sendo lida só fazer: print(type(n1))
