# Média escolar usando WHILE
x = 1 # Contador
soma = 0 # Acumulador
while x <= 5:
    n = int(input(f'{x} Digite o numero: '))
    soma = soma + n 
    x = x + 1
print(f'Média: {soma / 5:5.2f}')