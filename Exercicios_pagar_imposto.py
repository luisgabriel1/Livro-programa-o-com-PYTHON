# Aqui vou escrever uma expressão para determinar se a pessoa vai ou não pagar o imposto / só paga o imposto quem tem salario maior que R$ 1.200,00.
# Fiz um upgrade do que realmente precisava.
# Oque era para ser feito : 

# imposto = 1200
# Luis = 2000
# Alan = 1500
# Maria_Eduarda = 300
# Juslene = 5300
# print(Luis <= imposto)
# print(Luis > imposto)
# print(Alan <= imposto)
# print(Alan > imposto)
# print(Juslene <= imposto)
# print(Juslene > imposto)
# print(Maria_Eduarda <= imposto)
# print(Maria_Eduarda > Imposto)



# Oque foi feito:
# Aqui são as Variaveis
cobrar = 1200
# Aqui são os inputs
print ('*Bem vindo há Receita Federal*')
print()
nome = input('Qual o seu nome ? ')
print()
data = input('Envie sua data de nascimento, exemplo 22/02/2005 :  ')
print()
contato = int(input('Digite seu numero para contato:  '))
cpf = str(input('Digite seu CPF:  '))
salario = int(input('Qual o seu salario ? '))
print()
calcular_imposto = float(salario * 0.1)
Total = salario * 0.9


if salario > cobrar:
    print('Você tem que pagar R$', calcular_imposto, 'de imposto')
    print()
    Claro = ('S')
    Jamais = ('N')
    pagar = input('Você deseja pagar o imposto ?  S/N  ')
    if pagar == Jamais:
        print('Não se esqueça de pagar depois, em nosso site ')
    print()
    if pagar == Claro :
        pagamento = input ('Para pagar envie Pix:  ')
        tipo_pagar = ('Pix')
        print()
        if pagamento == tipo_pagar:
            print()
            cpf_pix = '455.013.968-40'
            print ('CPF:  ',  cpf_pix)
            pagou = input('Se você ja pagou envie Paguei:  ')
            fazer_pix = ('Paguei')
            print()
            if pagou == fazer_pix:
                print('Você pagou: R$ ',calcular_imposto,'muito Obrigado Sr', nome)
                print()
                print()
                print('Informações coletadas')
                print()
                print('Nome: ', nome) 
                print('Data: ', data) 
                print('Numero de Celular: ', contato)
                print('CPF: ', cpf)
                print('Salario: R$', salario)
                print('Total salario: R$', Total)
                      
else:
    salario <= cobrar
    print('Você não paga imposto')
    print()