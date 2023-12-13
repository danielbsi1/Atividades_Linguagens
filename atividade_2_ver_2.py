# Sei que a GUI ta feinha mas com o tempo vo dar uma melhorada nela #
from tkinter import *
from tkinter.ttk import Combobox


def cadastrar_album():
    global lancamento
    lancamento = lanc.get()
    resul_cadastro = caixa_cadastro.get()
    resul_ano = caixa_ano.get()
    resul_artista = caixa_artista.get()
    if lancamento == 1:
        lancamento = "Primeiro álbum"
    else:
        lancamento = 'Não foi o primeiro álbum'
    if resul_cadastro == '':
        resul_cadastro = 'Não especificado'
    if resul_ano == '':
        resul_ano = 'Não especificado'
    elif resul_ano != int:
        resul_ano = 'Não especificado'
    if resul_artista == '':
        resul_artista = 'Não especificado'
    arquiva = open('album_cadastro.txt', 'a', encoding='utf-8')
    arquiva.write(f'{resul_cadastro}|{resul_ano}|{resul_artista}'
                  f'|{lancamento}\n')
    # Essa função vai escrever os dados fornecidos no arquivo #


def invocar_cadastros():
    global janela_lista, lista_geral
    janela_lista = Toplevel(janela_cadastro)
    janela_lista.title('Lista de Álbuns')
    janela_lista.geometry('800x800')
    janela_lista.configure(background='light grey')
    # Segunda janela #
    lbl6 = Label(janela_lista, text=f'Álbuns cadastrados:', background='light blue', font=30)
    lbl6.pack()
    lbl6.place(x=0, y=0)
    # Label "principal" da janela
    arquivo_1 = open('album_cadastro.txt', 'r', encoding='utf-8')
    scrollbar1 = Scrollbar(janela_lista)
    scrollbar1.pack()
    scrollbar1.place(x=469, y=50)
    lista_geral = Listbox(janela_lista, yscrollcommand=scrollbar1.set, width=100)
    #
    for linhas in arquivo_1:
        lista_geral.insert(END, str(linhas))
    lista_geral.pack()
    lista_geral.place(x=0, y=50)
    scrollbar1.config(command=lista_geral.yview)
    arquivo_1.close()
    # demorei um tempo vergonhoso pra fazer essa listbox #
    janela_lista.mainloop()


def mostrar_lista_nome():
    global lista_albuns_artista, lista_artista, lista_ano, album_cadastrados
    arquivo_2 = open('album_cadastro.txt', 'r', encoding='utf-8')
    #
    scrollbar_albuns = Scrollbar(janela_nome)
    scrollbar_albuns.pack()
    scrollbar_albuns.place(x=469, y=50)
    lista_albuns_artista = Listbox(janela_nome, yscrollcommand=scrollbar_albuns.set, width=100)
    #
    nome_procurado = caixa_procura_nome.get().lower().strip()
    if nome_procurado == '':
        pass
    #
    albuns_cadastrados = []
    #
    lbl_nome_procurado = Label(janela_nome, text=f'Álbuns de {caixa_procura_nome.get().capitalize()}',
                               background='light blue')
    lbl_nome_procurado.pack()
    lbl_nome_procurado.place(x=0, y=20)
    #
    for linhas in arquivo_2:
        albuns_cadastrados.append(linhas.split('|'))
    for linhas in albuns_cadastrados:
        if nome_procurado in linhas[2].lower():
            lista_albuns_artista.insert(END, linhas[0])
    #
    lista_albuns_artista.pack()
    lista_albuns_artista.place(x=0, y=50)
    scrollbar_albuns.config(command=lista_albuns_artista.yview)
    arquivo_2.close()


def invocar_nome():
    global janela_nome, caixa_procura_nome
    janela_nome = Toplevel(janela_cadastro)
    janela_nome.title('Busca por nome')
    janela_nome.geometry('800x800')
    janela_nome.configure(background='light grey')
    #
    lbl7 = Label(janela_nome, text="Digite o nome do artista/banda autor/a deste álbum:", font=30, background='light '
                                                                                                              'blue')
    lbl7.pack()
    lbl7.place(x=0, y=0)
    #
    caixa_procura_nome = Entry(janela_nome, bd=5, width=30)
    caixa_procura_nome.pack()
    caixa_procura_nome.place(x=0, y=50)
    #
    btn_mostrar_lista = Button(janela_nome, text='Confirmar nome', command=mostrar_lista_nome)
    btn_mostrar_lista.pack()
    btn_mostrar_lista.place(x=200, y=50)
    janela_nome.mainloop()


def mostrar_lista_ano():
    ano_procurado = caixa_procura_ano.get()
    #
    scrollbar_ano = Scrollbar(janela_ano)
    scrollbar_ano.pack()
    scrollbar_ano.place(x=10, y=150)
    lista_albuns_ano = Listbox(janela_ano, yscrollcommand=scrollbar_ano.set, width=100)
    #
    albuns_cadastrados_3 = []
    arquivo_4 = open('album_cadastro.txt', 'r', encoding='utf-8')
    for linhas in arquivo_4:
        albuns_cadastrados_3.append(linhas.split('|'))
    #
    if periodo.get() == 0:
        for linhas in albuns_cadastrados_3:
            if ano_procurado in linhas[1]:
                lista_albuns_ano.insert(END, linhas[0])
    elif periodo.get() == 1:
        for linhas in albuns_cadastrados_3:
            if ano_procurado >= linhas[1]:
                lista_albuns_ano.insert(END, linhas[0])
    elif periodo.get() == 2:
        for linhas in albuns_cadastrados_3:
            if ano_procurado <= linhas[1]:
                lista_albuns_ano.insert(END, linhas[0])
    #
    lista_albuns_ano.pack()
    lista_albuns_ano.place(x=10, y=150)
    scrollbar_ano.config(command=lista_albuns_ano.yview)
    arquivo_4.close()
    #
    lbl10 = Label(janela_ano, text='Álbuns encontrados nesta faixa de anos:', background='light grey')
    lbl10.pack()
    lbl10.place(x=0, y=120)


def invocar_ano():
    global janela_ano, caixa_procura_ano, periodo
    janela_ano = Toplevel(janela_cadastro)
    janela_ano.title('Busca por ano')
    janela_ano.geometry('800x800')
    janela_ano.configure(background='light grey')
    #
    lbl8 = Label(janela_ano, text='Digite o ano de lançamento desejado:', font=30, background='light blue')
    lbl8.pack()
    lbl8.place(x=0, y=0)
    #
    caixa_procura_ano = Entry(janela_ano, bd=5, width=10)
    caixa_procura_ano.pack()
    caixa_procura_ano.place(x=100, y=50)
    #
    btn_mostrar_anos = Button(janela_ano, text='Confirmar ano', command=mostrar_lista_ano)
    btn_mostrar_anos.pack()
    btn_mostrar_anos.place(x=180, y=50)
    #
    periodo = IntVar()
    periodo.set(1)
    anterior = Radiobutton(janela_ano, text='Anterior a', variable=periodo, value=1, background='light gray')
    igual = Radiobutton(janela_ano, text='Igual a', variable=periodo, value=0, background='light gray')
    posterior = Radiobutton(janela_ano, text='Posterior a', variable=periodo, value=2, background='light grey')
    anterior.place(x=0, y=30)
    igual.place(x=0, y=50)
    posterior.place(x=0, y=70)
    #
    albuns_cadastrados_2 = []
    lista_anos = []
    arquivo_3 = open('album_cadastro.txt', 'r', encoding='utf-8')
    for linhas in arquivo_3:
        albuns_cadastrados_2.append(linhas.split('|'))
    for linhas in albuns_cadastrados_2:
        lista_anos.append(linhas[1])
    #
    combo = Combobox(janela_ano, values=lista_anos)
    combo.pack()
    combo.place(x=400, y=50)
    #
    lbl9 = Label(janela_ano, text='Anos já cadastrados:', background='light grey')
    lbl9.pack()
    lbl9.place(x=280, y=50)
    #
    janela_ano.mainloop()


def main():
    global lanc, caixa_cadastro, caixa_ano, caixa_artista, caixa_cadastro, janela_cadastro
    janela_cadastro = Tk()
    janela_cadastro.title('Tela de Cadastro')
    janela_cadastro.geometry('500x500')
    janela_cadastro.configure(background='light grey')
    janela_cadastro.resizable(width=TRUE, height=TRUE)
    # primeira janela #
    lbl1 = Label(janela_cadastro, text='Bem vindo ao Musicat', font=30, background='light blue')
    lbl1.pack()
    # Label de boas vindas 1 #
    lbl2 = Label(janela_cadastro, text='Qual é o nome do álbum que será cadastrado?', background='light grey')
    lbl2.place(x=0, y=100)
    caixa_cadastro = Entry(janela_cadastro, bd=5)
    caixa_cadastro.pack()
    caixa_cadastro.place(x=0, y=125)
    # Caixa para cadastrar álbuns #
    lbl3 = Label(janela_cadastro, text='Qual é o ano de lançamento desse álbum? (em numerais)', background='light grey')
    lbl3.place(x=0, y=200)
    caixa_ano = Entry(janela_cadastro, bd=5)
    caixa_ano.pack()
    caixa_ano.place(x=0, y=225)
    # Caixa para cadastrar ano de lançamento #
    lbl4 = Label(janela_cadastro, text='Qual o nome do artista/banda que fez este belo álbum?', background='light grey')
    lbl4.place(x=0, y=300)
    caixa_artista = Entry(janela_cadastro, bd=5)
    caixa_artista.pack()
    caixa_artista.place(x=0, y=325)
    # Caixa para cadastrar o nome do artista/banda #
    lbl5 = Label(janela_cadastro, text="Esse foi o álbum de lançamento do artista?", background='light grey')
    lbl5.place(x=0, y=400)
    lanc = IntVar()
    lanc.set(1)
    op1 = Radiobutton(janela_cadastro, text='SIM', variable=lanc, value=1, background='light gray')
    op2 = Radiobutton(janela_cadastro, text='NÃO', variable=lanc, value=0, background='light gray')
    op1.place(x=0, y=425)
    op2.place(x=50, y=425)
    # Opção se foi o álbum de lançamento ou não #
    btn_confirmar = Button(janela_cadastro, text='Confirmar dados do álbum', command=cadastrar_album)
    btn_confirmar.pack()
    btn_confirmar.place(x=250, y=450)
    # botão para confirmar dados cadastrados #
    btn_abrir_janela = Button(janela_cadastro, text='Mostrar álbuns cadastrados', command=invocar_cadastros)
    btn_abrir_janela.pack()
    btn_abrir_janela.place(x=450, y=450)
    # botão que leva a função que abre a segunda janela #
    btn_invocar_nome = Button(janela_cadastro, text='Busca de álbuns por nome', command=invocar_nome)
    btn_invocar_nome.pack()
    btn_invocar_nome.place(x=650, y=450)
    # botão que leva a função que abtr a terceira janela #
    btn_invocar_ano = Button(janela_cadastro, text='Busca de álbuns por ano', command=invocar_ano)
    btn_invocar_ano.pack()
    btn_invocar_ano.place(x=650, y=490)
    janela_cadastro.mainloop()


if __name__ == '__main__':
    main()
