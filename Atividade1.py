# ele quer nome idade sexo telefone #
lista_f = []
lista_m = []
lista_nomes = []
lista_idades = []
lista_sexo = []
lista_tel = []


def form():
    while nome != '0':
        nome = str(input('Ola, qual é o seu nome?? ')).capitalize()
        sexo = str(input('Qual é o seu sexo? M/F'))
        idade = int(input('Quantos anos você tem?? '))
        tel = int(input('Qual é o seu número de telefone?? '))
        arquivo = open('atv1.txt', 'a', encoding='utf-8')
        arquivo.write(f'|Seu nome é {nome}|seu sexo é {sexo}|Sua idade é {idade}|Seu telefone é {tel}\n')


form()