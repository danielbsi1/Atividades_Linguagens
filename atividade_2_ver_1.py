# Criar uma tela de cadastro de informações do álbum. As seguintesinformações são necessárias: nome do álbum, #
# ano de lançamento,nome da banda/artista, álbum lançamento do artista (sim/não); #
# • Criar uma tela que liste todos os álbuns cadastrados na sua base de dados. #
from tkinter import *

lancamento = ''


def cadastrar_album():
    global lancamento
    lancamento = lanc.get()
    resul_cadastro = caixa_cadastro.get()
    resul_ano = caixa_ano.get()
    resul_artista = caixa_artista.get()
    if lancamento == 1:
        lancamento = "Foi"
    else:
        lancamento = 'Não foi'
    if resul_cadastro == '':
        resul_cadastro = 'Não especificado'
    if resul_ano == '':
        resul_ano = 'Não especificado'
    if resul_artista == '':
        resul_artista = 'Não especificado'
    arquiva = open('album_cadastro.txt', 'a', encoding='utf-8')
    arquiva.write(f'Álbum: {resul_cadastro}|Lançado em: {resul_ano}|Pela banda/artista: {resul_artista}'
                  f'|{lancamento} o album de lançamento dessa banda.\n')
    # Essa função vai escrever os dados fornecidos no arquivo #


def mostrar_janela():
    global janela_lista
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
    scrollbar = Scrollbar(janela_lista)
    scrollbar.pack()
    scrollbar.place(x=469, y=50)
    lista_cadastros = Listbox(janela_lista, yscrollcommand=scrollbar.set, width=100)
    for linhas in arquivo_1:
        lista_cadastros.insert(END, str(linhas))
    lista_cadastros.pack()
    lista_cadastros.place(x=0, y=50)
    scrollbar.config(command=lista_cadastros.yview)
    arquivo_1.close()
    # fonte de toda a minha dor e sofrimento #
    janela_lista.mainloop()


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
lbl3 = Label(janela_cadastro, text='Qual é o ano de lançamento desse álbum?', background='light grey')
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
btn_abrir_janela = Button(janela_cadastro, text='Mostrar álbuns cadastrados', command=mostrar_janela)
btn_abrir_janela.pack()
btn_abrir_janela.place(x=450, y=450)
# botão que leva a função que abre a segunda janela #
janela_cadastro.mainloop()
