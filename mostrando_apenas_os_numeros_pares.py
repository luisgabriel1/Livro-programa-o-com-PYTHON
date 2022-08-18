# Aqui usando o metodo de while vou fazer com que me mostre apenas os numeros pares entre 0 e o numero escolhido no input
# Na parte que coloco x % 2 == 0 estou dizendo que os numeros entre os escolhido que o resto da divisão entre ele e 2 for igual a 0 ele me mostra.


# Exemplo 1:
fim = (int(input('Escolha um numero:   ')))
x = 0
while x <= fim :
    if x % 2 == 0:
        print(x)
    x = x + 1
    
# Exemplo 2:
# Aqui estou falando para que o x adicione de 2 em 2 ou seja os numero automaticamento serão pares 
while x <= fim:
    print(x)
    x = x + 2