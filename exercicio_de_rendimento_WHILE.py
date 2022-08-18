# Escreva um programa que pergunte o deposito inicial e a taxa de juros da poupança.
# Exiba os valores mês a mês para os 24 primeiros meses.
# Escreva o total de ganhos com juros no periodo.
nome = input('Qual o seu nome ? \n')    
deposito = int(input('Qual a quantia que deseja depositar: \n'))
juros = float(input('Qual a taxa juros você vai aplicar: \n'))
#juros = 0.01
#deposito = 100
x = 1 # Contador
# Acumulador = m
while x <= 3:
    m = float(deposito*(1 + juros)**3)
    print(f'Mês {x} foi :  R${m}')
    m = m + juros
    x = x + 1
print(f'{nome} O seu rendimento total em 24 meses foi de :  R${m}')  