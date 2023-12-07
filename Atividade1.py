lista_m = []
lista_f = []
lista_i = []
lista_sexo = []
lista_nome = []
lista_idade = []
lista_tel = []


def form():
    global nome, idade, sexo, tel
    nome = 1
    while nome != '0':
        nome = input('Olá, qual é o seu nome? ').capitalize()
        lista_nome.append(nome)
        idade = input('Quantos anos você tem? ')
        lista_idade.append(idade)
        sexo = input('Qual é o seu sexo? M/F ').lower()
        if sexo == 'm':
            sexo = 'Masculino'
            lista_m.append(nome)
        elif sexo == 'f':
            sexo = 'Feminino'
            lista_f.append(nome)
        else:
            sexo = 'não especificado'
        lista_sexo.append(sexo)
        try:
            tel = int(input('Qual é o seu número de telefone? '))
        except ValueError:
            tel = 'número invalido'
        lista_tel.append(tel)
        arquivo = open('uga.txt', 'a', encoding='utf-8')
        arquivo.write(f'|Seu nome é {nome}|Tem {idade} anos|Seu Sexo é {sexo}|Número de telefone: {tel}|\n')
        continuar = input('Quer adicionar outro nome? S/N').lower()
        if continuar == 'n':
            break
    print('Dados armazenados')


def lerdados():
    print('-' * 30)
    for c in range(0, len(lista_nome)):
        print(f'Nome: {lista_nome[c]}\nIdade: {lista_idade[c]}\nSexo: {lista_sexo[c]}\nTelefone: {lista_tel[c]}')
    print('-' * 30)

def busca_usuario_pelo_sexo():
    ver = input("quer ver a lista de qual sexo? M/F/ ").lower()
    if ver == 'm':
        print(f'O nome das pessoas do sexo masculino cadastrados são: {lista_m}')
    elif ver == 'f':
        print(f'O nome das pessoas de sexo feminino cadastrado são: {lista_f}')


form()
busca_usuario_pelo_sexo()
lerdados()
