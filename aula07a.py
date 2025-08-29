# Operadores Aritméticos
# EX: + (Adição), - (Subtração), * (Multiplicação), / (Divisão), ** (Exponenciação), // (Divisão inteira), % (Módulo ou resto da divisão)
# EX: Adição| 5+2 == 7 | Subtração: 5-2 == 3 | Multiplicação: 5*2 == 10 | Divisão: 5/2 == 2.5 | Exponenciação: 5**2 == 25 | Divisão Inteira: 5//2 == 2 | Módulo: 5%2 == 1 
# Ordem de precedência: 1° ( ) | 2° ** | 3° * / // % | 4° + -

n1 = int(input('Digite um valor:'))
n2 = int(input('Digite outro valor:'))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é: {}, o produto é: {} e a divisão é: {:.3f}'.format(s, m, d), end = ' ')
print('A divisaõ inteira é: {} e a potẽncia é: {}'.format(di, e))

# Para quebrar a linha no print, é só usar \n
# Para continuar na mesma linha usando dois prints, é só usar end = ' ' no rpimeiro print
# Para limitar o número de casas decimais na divisão é so usar {:.3f}, onde 3 é o número de casas decimais

