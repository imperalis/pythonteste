n1 = int(0)
n2 = int(1)
n3 = int(0)
print ('•' *42)
print (' ' *3, 'Consulta da Sequência de Fibonacci')
print ('•' *42)
Valor = int(input('Digite um número: '))
while Valor > n3:
    n3 = n1 + n2
    n1 = n2
    n2 = n3
if Valor == 0 or Valor == 1:
    print ('O número faz parte da sequência de Fibonacci.')
elif Valor == n3:
    print ('O número faz parte da sequência de Fibonacci.')
else:
    print ('O número digitado não faz parte da sequência de Fibonacci.')