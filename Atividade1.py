lista_m = []
lista_f = []
lista_i = []
lista_sexo = []
lista_nome = []
lista_idade = []
lista_tel = []
achar = ''
nome = ''


def busca_usuario_nome(part_nome):
    """
    Função buscará na lista de nomes o nome digitado, e nomes que tem o que foi digitado  como parte, e mostrará os dados cadastrados desse nome.
    """
    print('-' * 30)
    print('As pessoas com esse nome/parte de nome cadastrado são: ')
    for c in range(0, len(lista_nome)):
        if part_nome in lista_nome[c]:
            print(f'Nome: {lista_nome[c]}\nIdade: {lista_idade[c]}\nSexo: {lista_sexo[c]}\nTelefone: {lista_tel[c]}')
            print('-' * 30)
    print('-' * 30)


def form():
    global nome, idade, sexo, tel, achar
    nome = 1
    achar = 7
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
    achar = str(input('Quer achar qual nome cadastrado?? ')).capitalize()
    print('Dados armazenados')


def ler_dados():
    """
    Função serve para ler os dados de maneira organizada
    """
    print('-' * 30)
    for c in range(0, len(lista_nome)):
        print(f'Nome: {lista_nome[c]}\nIdade: {lista_idade[c]}\nSexo: {lista_sexo[c]}\nTelefone: {lista_tel[c]}')
        print('-' * 30)


def busca_usuario_pelo_sexo():
    """
    Função serve para encontrar todos os nomes cadastrados com sexo Masculino ou Feminino
    """
    ver_lista = input("quer ver a lista de qual sexo? M/F/ ").lower()
    if ver_lista == 'm':
        print('-' * 30)
        print(f'O nome das pessoas do sexo masculino cadastrados são: {lista_m}')
    elif ver_lista == 'f':
        print('-' * 30)
        print(f'O nome das pessoas de sexo feminino cadastrado são: {lista_f}')
    else:
        print('Sexo não cadastrado')


form()
busca_usuario_pelo_sexo()
ler_dados()
busca_usuario_nome(achar)
