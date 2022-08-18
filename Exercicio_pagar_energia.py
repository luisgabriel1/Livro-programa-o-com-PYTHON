# Aqui tenho que calcular o kWh e saber quanto a pessoa vai pagar de acordo com as respostas.
#- Residencia até 500 kWh = R$0,40 / acima de 500 kWh = R$0,65
#- Comercio até 1000 kWh = R$0,55 / acima de 1000 kWh = R$0,60
#- Industria até 5000 kWh = R$0,55 / aicima de 5000 kWh = R$0,60

# Abaixo está as variaveis:
residencial = 500
valor_r = 0.40
valor_r1 = 0.65
comercial = 1000
industrial = 5000
valor_c_i = 0.55
valor_c1_i1 = 0.60
residencia =  'r'
comercio = 'c'
industria = 'i'
# Abaixo os inputs
print()
print()
nome_cliente = input('Qual o seu nome ?  ')
print()
escolha_estabelecimentos = input('Qual você quer calcular/ Para residencia envie: r / Para comercio envie: c / Para industria envie: i   ')
print()
# Abaixo as condições
if escolha_estabelecimentos == residencia:
    kWh_residencia = int(input(f'{nome_cliente} qual o gasto de Kwh você tem ?  '))
    print()
    if kWh_residencia <= residencial:
        print(f'{nome_cliente} você tem que pagar: R${kWh_residencia * valor_r}')
    else:
        kWh_residencia > residencial
        print(f'{nome_cliente} você tem que pagar: R${kWh_residencia * valor_r1}')
if escolha_estabelecimentos == comercio:
    kWh_comerio = int(input(f'{nome_cliente} qual o gasto de Kwh você tem ?  '))
    print()
    if kWh_comerio <= comercial:
        print(f'{nome_cliente} você tem que pagar: R${kWh_comerio * valor_c_i}')
    else:
        kWh_comerio > comercial
        print(f'{nome_cliente} você tem que pagar: R${kWh_comerio * valor_c1_i1}')
if escolha_estabelecimentos == industria:
    kWh_industria = int(input(f'{nome_cliente} qual o gasto de kWh você tem ? '))
    if kWh_industria <= industrial:
        print(f'{nome_cliente} você tem que pagar: R${kWh_industria * valor_c_i}')
    else:
        kWh_industria > industrial
        print(f'{nome_cliente} voce tem que pagar: R${kWh_industria * valor_c1_i1}')