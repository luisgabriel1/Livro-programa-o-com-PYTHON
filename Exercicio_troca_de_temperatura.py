# Aqui eu tenho que converter de c para f usando a formula 9*c / 5+32 e tambem usando input

# Era para ser feito igual o exemplo abaixo:
# c = int(input('Qual a temperatura em Celsius você gostaria de converter ? '))
# f  = int(9 * c / 5 + 32)
# print(f'A temperatura em fahrenheit é de: {f}')

# Oque eu fiz : 
print()
print('Bem Vindo ao conversor de temperatura')
print()
opitions = input('Você deseja converter Ceusios OU Fahrenheit ? ')
print()
opition_c = 'c'
option_f = 'f'
if opitions == opition_c:
    c = int(input('Qual a temperatura em Celsius ? '))
    print()
    formula = int(9 * c / 5 + 32)
    print(f'A temperatura em Fahrenheit é de : {formula}')
else :
    opitions == option_f
    f = int(input('Qual a temperatura em Fahrenheit ? '))
    formula_1 = int((f - 32 ) * 5 / 9)
    print(f'A temperatura em Celsius é de :  {formula_1}')