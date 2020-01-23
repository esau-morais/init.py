from sqlite3 import *
from tkinter import *
from tkinter import ttk

from emoji import *


class softwareICE:
    def __init__(self, master=None):
        self.janela_principal = Frame(master)
        self.janela_principal.pack(side=TOP)

        self.janela_principal = janela.title(
            'Igreja Cristã Evangélica em Tuntum - MA')

        self.janela_principal = janela.geometry('800x500')

        self.fonte_cursiva = ('Blastimo', 64)

        self.fonte_padrao = ('Poppins Light', 14)

        self.janela_principal = janela.configure(bg='#7f0000')

        self.tit_principal = Label(self.janela_principal, text='ICE - Tuntum',
                                   font=self.fonte_cursiva, bg='#7f0000')  # Main label background
        self.tit_principal['fg'] = ('White')
        self.tit_principal['pady'] = 30
        self.tit_principal.pack(pady=20)

        self.botao_principal = Frame(master)
        self.botao_principal.pack(anchor=CENTER, pady=40)

        self.botao_01 = Button(self.botao_principal, text='Banco de Dados', highlightthickness=0,
                               activebackground='#990000', relief=RAISED,
                               anchor=W, activeforeground='White', pady=10, cursor='hand2')
        self.botao_01['font'] = self.fonte_padrao
        self.botao_01['bg'] = '#660000'
        self.botao_01['fg'] = ('White')
        self.botao_01['command'] = self.banco_de_dados
        self.botao_01.pack(side=LEFT)

        self.botao_02 = Button(self.botao_principal, text='Registro', highlightthickness=0,
                               activebackground='#990000', relief=RAISED,
                               activeforeground='White', pady=10, cursor='hand2')
        self.botao_02['font'] = self.fonte_padrao
        self.botao_02['bg'] = ('#660000')
        self.botao_02['fg'] = ('White')
        self.botao_02['command'] = self.pagina_de_registros
        self.botao_02.pack(side=RIGHT)

    def pagina_de_registros(self, master=None):
        self.janela_registro = Toplevel()

        self.janela_registro.title('Registro de Membros e Congregados')

        self.janela_registro.geometry('800x500')

        self.janela_registro.configure(bg='#7f0000')

        self.tit_principal = Label(self.janela_registro, text='Registros',
                                   font=self.fonte_cursiva, bg='#7f0000')  # Main label background
        self.tit_principal['fg'] = ('White')
        self.tit_principal['pady'] = 30
        self.tit_principal.pack(pady=20)

        self.registros = Frame(self.janela_registro)
        self.registros.pack(anchor=CENTER, pady=40)

        self.registro_01 = Button(self.registros, text='Congregados', highlightthickness=0,
                                  activebackground='#990000', relief=RAISED,
                                  anchor=W, activeforeground='White', pady=10, cursor='hand2')
        self.registro_01['font'] = self.fonte_padrao
        self.registro_01['bg'] = '#660000'
        self.registro_01['fg'] = ('White')
        self.registro_01['command'] = self.registro_de_congregados
        self.registro_01.pack(side=LEFT)

        self.registro_02 = Button(self.registros, text='Membros', highlightthickness=0,
                                  activebackground='#990000', relief=RAISED,
                                  activeforeground='White', pady=10, cursor='hand2')
        self.registro_02['font'] = self.fonte_padrao
        self.registro_02['bg'] = ('#660000')
        self.registro_02['fg'] = ('White')
        self.registro_02['command'] = self.registro_de_membros
        self.registro_02.pack(side=RIGHT)

    def registro_de_congregados(self, master=None):
        self.janela_registro_de_congregados = Toplevel()

        self.janela_registro_de_congregados.title('Registro de Congregados')

        self.janela_registro_de_congregados.geometry('800x500')

        self.janela_registro_de_congregados.configure(bg='#7f0000')

        self.tit_principal = Label(self.janela_registro_de_congregados, text='Registro de Congregados', font=(
            'Blastimo', 36), bg='#7f0000')  # Main label background
        self.tit_principal['fg'] = ('White')
        self.tit_principal.grid(pady=20, row=0)

        self.congregados = Frame(self.janela_registro_de_congregados)
        self.congregados['bg'] = ('#7f0000')
        self.congregados.grid(pady=40)

        self.nome_completo = Label(
            self.congregados, text='Nome Completo', font=(self.fonte_padrao))
        self.nome_completo['bg'] = ('#7f0000')
        self.nome_completo['fg'] = ('#ffffff')
        self.nome_completo.grid(padx=10, row=1, column=0)

        self.entrada_de_nome_completo = Entry(self.congregados)
        self.entrada_de_nome_completo.grid(padx=10, row=1, column=1)

        self.sexo = Label(self.congregados, text='Sexo',
                          font=(self.fonte_padrao))
        self.sexo['bg'] = ('#7f0000')
        self.sexo['fg'] = ('#ffffff')
        self.sexo.grid(padx=10, row=2, column=0)

        self.entrada_de_sexo = Entry(self.congregados)
        self.entrada_de_sexo.grid(padx=10, row=2, column=1)

        self.data_de_nascimento = Label(
            self.congregados, text='Data de Nascimento', font=(self.fonte_padrao))
        self.data_de_nascimento['bg'] = ('#7f0000')
        self.data_de_nascimento['fg'] = ('#ffffff')
        self.data_de_nascimento.grid(padx=10, row=3, column=0)

        self.entrada_de_data_de_nascimento = Entry(self.congregados)
        self.entrada_de_data_de_nascimento.grid(padx=10, row=3, column=1)

        self.endereco = Label(
            self.congregados, text='Endereço', font=(self.fonte_padrao))
        self.endereco['bg'] = ('#7f0000')
        self.endereco['fg'] = ('#ffffff')
        self.endereco.grid(padx=10, row=4, column=0)

        self.entrada_de_endereco = Entry(self.congregados)
        self.entrada_de_endereco.grid(padx=10, row=4, column=1)

        self.estado_civil = Label(
            self.congregados, text='Estado Civil', font=(self.fonte_padrao))
        self.estado_civil['bg'] = ('#7f0000')
        self.estado_civil['fg'] = ('#ffffff')
        self.estado_civil.grid(padx=10, row=5, column=0)

        self.entrada_de_estado_civil = Entry(self.congregados)
        self.entrada_de_estado_civil.grid(padx=10, row=5, column=1)

        self.escolaridade = Label(
            self.congregados, text='Escolaridade', font=(self.fonte_padrao))
        self.escolaridade['bg'] = ('#7f0000')
        self.escolaridade['fg'] = ('#ffffff')
        self.escolaridade.grid(padx=10, row=6, column=0)

        self.entrada_de_escolaridade = Entry(self.congregados)
        self.entrada_de_escolaridade.grid(padx=10, row=6, column=1)

        self.naturalidade = Label(
            self.congregados, text='Naturalidade', font=(self.fonte_padrao))
        self.naturalidade['bg'] = ('#7f0000')
        self.naturalidade['fg'] = ('#ffffff')
        self.naturalidade.grid(padx=10, row=7, column=0)

        self.entrada_de_naturalidade = Entry(self.congregados)
        self.entrada_de_naturalidade.grid(padx=10, row=7, column=1)

        self.igreja_anterior = Label(
            self.congregados, text='Igreja Anterior', font=(self.fonte_padrao))
        self.igreja_anterior['bg'] = ('#7f0000')
        self.igreja_anterior['fg'] = ('#ffffff')
        self.igreja_anterior.grid(padx=10, row=1, column=3)

        self.entrada_de_igreja_anterior = Entry(self.congregados)
        self.entrada_de_igreja_anterior.grid(padx=10, row=1, column=4)

        self.data_de_conversao = Label(
            self.congregados, text='Data de Conversão', font=(self.fonte_padrao))
        self.data_de_conversao['bg'] = ('#7f0000')
        self.data_de_conversao['fg'] = ('#ffffff')
        self.data_de_conversao.grid(padx=10, row=2, column=3)

        self.entrada_de_data_de_conversao = Entry(self.congregados)
        self.entrada_de_data_de_conversao.grid(padx=10, row=2, column=4)

        self.registrar_ = Button(self.congregados, text='Registrar', highlightthickness=0,
                                 activebackground='#990000', relief=RAISED,
                                 anchor=S, activeforeground='White', cursor='hand2')
        self.registrar_['font'] = ('Poppins Light', 12)
        self.registrar_['bg'] = '#660000'
        self.registrar_['fg'] = ('White')
        self.registrar_['command'] = self.acionar_botao
        self.registrar_.grid(row=8, column=1, columnspan=3, ipadx=50)

        self.autenticador = Label(
            self.congregados, text='', font=('Courier 10 Pitch', 21))
        self.autenticador['bg'] = ('#7f0000')
        self.autenticador.grid(row=8, column=2, columnspan=3)

    def registro_de_membros(self, master=None):
        self.janela_registro_de_membros = Toplevel()

        self.janela_registro_de_membros.title('Registro de Membros')

        self.janela_registro_de_membros.geometry('800x500')

        self.janela_registro_de_membros.configure(bg='#7f0000')

        self.tit_principal = Label(self.janela_registro_de_membros, text='Registro de Membros', font=(
            'Blastimo', 36), bg='#7f0000')  # Main label background
        self.tit_principal['fg'] = ('White')
        self.tit_principal.grid(pady=20, row=0)

        self.membros = Frame(self.janela_registro_de_membros)
        self.membros['bg'] = ('#7f0000')
        self.membros.grid(pady=40)

        self.nome_completo = Label(
            self.membros, text='Nome Completo', font=(self.fonte_padrao))
        self.nome_completo['bg'] = ('#7f0000')
        self.nome_completo['fg'] = ('#ffffff')
        self.nome_completo.grid(padx=10, row=1, column=0)

        self.entrada_de_nome_completo = Entry(self.membros)
        self.entrada_de_nome_completo.grid(padx=10, row=1, column=1)

        self.sexo = Label(self.membros, text='Sexo', font=(self.fonte_padrao))
        self.sexo['bg'] = ('#7f0000')
        self.sexo['fg'] = ('#ffffff')
        self.sexo.grid(padx=10, row=2, column=0)

        self.entrada_de_sexo = Entry(self.membros)
        self.entrada_de_sexo.grid(padx=10, row=2, column=1)

        self.data_de_nascimento = Label(
            self.membros, text='Data de Nascimento', font=(self.fonte_padrao))
        self.data_de_nascimento['bg'] = ('#7f0000')
        self.data_de_nascimento['fg'] = ('#ffffff')
        self.data_de_nascimento.grid(padx=10, row=3, column=0)

        self.entrada_de_data_de_nascimento = Entry(self.membros)
        self.entrada_de_data_de_nascimento.grid(padx=10, row=3, column=1)

        self.endereco = Label(self.membros, text='Endereço',
                              font=(self.fonte_padrao))
        self.endereco['bg'] = ('#7f0000')
        self.endereco['fg'] = ('#ffffff')
        self.endereco.grid(padx=10, row=4, column=0)

        self.entrada_de_endereco = Entry(self.membros)
        self.entrada_de_endereco.grid(padx=10, row=4, column=1)

        self.estado_civil = Label(
            self.membros, text='Estado Civil', font=(self.fonte_padrao))
        self.estado_civil['bg'] = ('#7f0000')
        self.estado_civil['fg'] = ('#ffffff')
        self.estado_civil.grid(padx=10, row=5, column=0)

        self.entrada_de_estado_civil = Entry(self.membros)
        self.entrada_de_estado_civil.grid(padx=10, row=5, column=1)

        self.escolaridade = Label(
            self.membros, text='Escolaridade', font=(self.fonte_padrao))
        self.escolaridade['bg'] = ('#7f0000')
        self.escolaridade['fg'] = ('#ffffff')
        self.escolaridade.grid(padx=10, row=6, column=0)

        self.entrada_de_escolaridade = Entry(self.membros)
        self.entrada_de_escolaridade.grid(padx=10, row=6, column=1)

        self.naturalidade = Label(
            self.membros, text='Naturalidade', font=(self.fonte_padrao))
        self.naturalidade['bg'] = ('#7f0000')
        self.naturalidade['fg'] = ('#ffffff')
        self.naturalidade.grid(padx=10, row=7, column=0)

        self.entrada_de_naturalidade = Entry(self.membros)
        self.entrada_de_naturalidade.grid(padx=10, row=7, column=1)

        self.igreja_anterior = Label(
            self.membros, text='Igreja Anterior', font=(self.fonte_padrao))
        self.igreja_anterior['bg'] = ('#7f0000')
        self.igreja_anterior['fg'] = ('#ffffff')
        self.igreja_anterior.grid(padx=10, row=1, column=3)

        self.entrada_de_igreja_anterior = Entry(self.membros)
        self.entrada_de_igreja_anterior.grid(padx=10, row=1, column=4)

        self.data_de_conversao = Label(
            self.membros, text='Data de Conversão', font=(self.fonte_padrao))
        self.data_de_conversao['bg'] = ('#7f0000')
        self.data_de_conversao['fg'] = ('#ffffff')
        self.data_de_conversao.grid(padx=10, row=2, column=3)

        self.entrada_de_data_de_conversao = Entry(self.membros)
        self.entrada_de_data_de_conversao.grid(padx=10, row=2, column=4)

        self.registrar_ = Button(self.membros, text='Registrar', highlightthickness=0,
                                 activebackground='#990000', relief=RAISED,
                                 anchor=CENTER, activeforeground='White', cursor='hand2')
        self.registrar_['font'] = ('Poppins Light', 12)
        self.registrar_['bg'] = '#660000'
        self.registrar_['fg'] = ('White')
        self.registrar_['command'] = self.acionar_botao
        self.registrar_.grid(row=8, column=1, columnspan=3, ipadx=50)

        self.autenticador = Label(
            self.membros, text='', font=('Courier 10 Pitch', 21))
        self.autenticador['bg'] = ('#7f0000')
        self.autenticador.grid(row=8, column=2, columnspan=3)

    def banco_de_dados(self, master=None):
        self.janela_banco_de_dados = Toplevel()

        self.janela_banco_de_dados.title('Registro de Membros')

        self.janela_banco_de_dados.geometry('800x500')

        self.janela_banco_de_dados.configure(bg='#7f0000')

        self.tit_principal = Label(self.janela_banco_de_dados, text='Banco de Dados', font=(
            'Blastimo', 36), bg='#7f0000')  # Main label background
        self.tit_principal['fg'] = ('White')
        self.tit_principal.pack(pady=20)

    def acionar_botao(self, master=None):
        self.conex = connect('banco_de_dados.db')
        self.cursor = self.conex.cursor()

        self.cursor.execute("""
    CREATE TABLE IF NOT EXISTS dados (
    nome_completo TEXT,
    sexo TEXT,
    data_de_nascimento TEXT,
    endereco TEXT,
    estado_civil TEXT,
    escolaridade TEXT,
    naturalidade TEXT,
		igreja_anterior TEXT,
		data_de_conversao TEXT
    );
  """)

        self.dados = [
            self.entrada_de_nome_completo.get(),
            self.entrada_de_sexo.get(),
            self.entrada_de_data_de_nascimento.get(),
            self.entrada_de_endereco.get(),
            self.entrada_de_estado_civil.get(),
            self.entrada_de_escolaridade.get(),
            self.entrada_de_naturalidade.get(),
            self.entrada_de_igreja_anterior.get(),
            self.entrada_de_data_de_conversao.get()
        ]

        self.cursor.execute("""
    INSERT INTO dados (nome_completo, sexo, data_de_nascimento, endereco, estado_civil, escolaridade, naturalidade, igreja_anterior, data_de_conversao) 
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, self.dados)

        self.conex.commit()

        if self.dados[0] == '' or self.dados[1] == '' or self.dados[2] == '' or self.dados[3] == '' or self.dados[4] == '' or self.dados[5] == '' or self.dados[6] == '' or self.dados[7] == '' or self.dados[8] == '':
            self.autenticador['text'] = emojize(':warning:')
            self.autenticador['fg'] = 'Yellow'

            self.cursor.execute(
                "DELETE FROM dados WHERE nome_completo=?", (self.entrada_de_nome_completo.get(),))
            self.cursor.execute("DELETE FROM dados WHERE sexo=?",
                                (self.entrada_de_sexo.get(),))
            self.cursor.execute("DELETE FROM dados WHERE data_de_nascimento=?",
                                (self.entrada_de_data_de_nascimento.get(),))
            self.cursor.execute(
                "DELETE FROM dados WHERE endereco=?", (self.entrada_de_endereco.get(),))
            self.cursor.execute(
                "DELETE FROM dados WHERE estado_civil=?", (self.entrada_de_estado_civil.get(),))
            self.cursor.execute(
                "DELETE FROM dados WHERE escolaridade=?", (self.entrada_de_escolaridade.get(),))
            self.cursor.execute(
                "DELETE FROM dados WHERE naturalidade=?", (self.entrada_de_naturalidade.get(),))
            self.cursor.execute(
                "DELETE FROM dados WHERE data_de_conversao=?", (self.entrada_de_data_de_conversao.get(),))
            self.cursor.execute(
                "DELETE FROM dados WHERE igreja_anterior=?", (self.entrada_de_igreja_anterior.get(),))

            self.cursor.fetchall()

            self.conex.commit()
        else:
            self.autenticador['text'] = emojize(':heavy_check_mark:')
            self.autenticador['fg'] = 'White'

            self.cursor.execute("SELECT * FROM dados")

            self.conex.commit()

        self.entrada_de_nome_completo.delete(0, END)
        self.entrada_de_sexo.delete(0, END)
        self.entrada_de_data_de_nascimento.delete(0, END)
        self.entrada_de_endereco.delete(0, END)
        self.entrada_de_estado_civil.delete(0, END)
        self.entrada_de_escolaridade.delete(0, END)
        self.entrada_de_naturalidade.delete(0, END)
        self.entrada_de_igreja_anterior.delete(0, END)
        self.entrada_de_data_de_conversao.delete(0, END)


if __name__ == '__main__':
    janela = Tk()

    softwareICE(janela)

    janela.mainloop()
