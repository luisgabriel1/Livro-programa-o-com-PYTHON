# *** Os print vazios é para pular linha apenas ***
# Aqui estou usando os colchete que serve para saber qual o caracter de acordo com o numero passado entre [] 
# Exemplo abaixo : 
print('Abaixo estou usando o sinal de [] :')
nome = 'Luis'
print(nome[3])
print(nome[0], nome[1], nome[2], nome[3])
print()

# Aqui estou usando Len / oque faz len ?  = len é responsavel por verificar a quantidade do caracter que foi passado dentro de () ou dentro de '''' / A contagem começa no Zero.
# Exemplo abaixo : 
print('Abaixo estou usando a função len :')
print(len(nome))
print(len('Luis'))
print()

# Aqui vou usar o metodo de concatenação/para fazer uma concatenação você pode usar dois jeitos usando o simblo de adição ou usando o simbolo de multiplicação/Os dois tem resultados diferentes.
# Exemplos abaixo:
print('Abaixo estou usando os metodos de concatenação :')
print()
a = '12345'
b = '1'
print(a + '6')
print(b * 3)
print()

# Aqui vou usar o metodo de composição / marcador = %d - numeros inteiros / marcador = %s - strings / marcador = %f - numeros decimais / o numero 3 representa a quantidade de caracter que vai reservar
print('Abaixo estou usando o metodo de composição %d :')
idade = 17
print('Luis tem %d anos' %idade) # Metodo padrão
print('%d' %idade) # Metodo padrão
print('%03d' %idade) # O parametro que vier antes do 3 sera o primeiro a mostrar.
print('%3d' %idade)  # Aqui não foi passado nem um parametro antes do 3 então ficou só o espaço .
print('%-3d' %idade) # Esse jeito é para passar algum parametro depois do 3, no caso não foi passado nenhum parametro.
print()

# Aqui a baixo estou usando o metodo de composição %f / o primeiro numero é para reservar os caracteres antes da virgula / o segundo numero é para reservar os caracteres decimais no caso depois da virgula.
print('Abaixo estou usando o metodo de composição %f :')
valor = (2022)
print('%5f' %valor) # Aqui usei o metodo sem passar quantos decimais vou usar.
print('%5.2f' %valor) # Aqui usei o metodo passando a quantidade de decimais que iria usar.
print()

# Aqui vou usar todos os metodos de composição juntos.
print('Abaixo estarei usando todos os metodos de composição :')
grana = (25.50)
print('%s tem %d anos e apenas R$%2.2f no bolso.' %(nome, idade, grana)) 
print()

# Aqui vou usar o metodo .format
print('Abaixo estarei usando o metodo .format :')
print('{} tem {} anos e apenas R${} no bolso.' .format (nome, idade, grana)) # Aqui estou usando o metodo sem passar nada dentro das chaves {}
print('{} tem {} anos e apenas R${:2.2f} no bolso.' .format (nome, idade, grana)) # Aqui estou usando o metodo passando parametos dento das chaves {}
print()

# Aqui vou usar o metodo de f'strings' / os parametros tem que ser passados dentro das chaves {} / quando você colocar < a configuração sera para a direita do parametro / quando você colocar > a configuração sera para a esquerda do parametro
print('Aqui estarei usando o metodo de f-strings :')
print(f'{nome} tem {idade} anos e apenas R${grana} no bolso.') # Aqui estou usando o metodo sem configurar os parametros.
print(f'{nome:<3} tem {idade:>03} anos e apenas R${grana:5.2f} no bolso.') # Aqui estou usando o metodo configurando os parametros
print()

# Aqui vou ver sequencias e tempo.
print('Abaixo estou usando o metodo de sequencia e tempo')
divida = 0
compra = 100
divida = divida + compra
compra = 200
divida = divida + compra
compra = 300
divida = divida + compra
compra = 0
print(divida)
print()