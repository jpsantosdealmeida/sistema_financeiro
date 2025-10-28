import customtkinter as ctk
from tkinter import ttk
from tkcalendar import Calendar
from model.categoria import Categoria
from model.transacao import Transacao
from controller.categoria_controller import CategoriaController
from controller.trasacao_controller import TransacaoController

class TelaPrincipal:
    def __init__(self,master):
        self.master = master
        self.widgets()


    def widgets(self):
        self.fontes_padroes()
        self.header()
        self.menu()
        self.main()
        self.funcoes()

    def funcoes(self):
        self.view_treeview()

    def fontes_padroes(self):
        self.fonte_titulo = ctk.CTkFont('Poppins',22,'bold')
        self.fonte_subtitulo = ctk.CTkFont('Roboto Medium',16,'normal')
        self.fonte_labels = ctk.CTkFont('Segoe UI',14,'normal')
        self.fonte_botoes_entradas = ctk.CTkFont('Nunito',15,'bold')

    def header(self):
        # Frame Barra azul 
        self.frame_titulo_main = ctk.CTkFrame(self.master,fg_color='#2E86DE')
        self.frame_titulo_main.grid(row=0,column=0,sticky='nswe')
        self.frame_titulo_main.columnconfigure(0,weight=1)

        # -- Título -- 
        self.label_titulo_dinamico = ctk.CTkLabel(
            self.frame_titulo_main,
            text='FinCatch',
            text_color='white',
            font=self.fonte_titulo)
        self.label_titulo_dinamico.grid(row=0,column=0,sticky='we')
    
    def menu(self):
        # Frame menus
        self.frame_menu = ctk.CTkFrame(self.master,fg_color='white')
        self.frame_menu.rowconfigure(1,weight=1)
        self.frame_menu.columnconfigure((0,1,2,3),weight=1)
        self.frame_menu.grid(row=1,column=0,padx=15,sticky='nswe')
        # Início
        self.btn_inicio = ctk.CTkButton(self.frame_menu,text='Início',font=self.fonte_subtitulo,text_color='black',fg_color='transparent',hover_color="#E3E5E8",command=self.aba_inicio)
        self.btn_inicio.grid(row=0,column=0,padx=15,pady=10)

        # Transações
        self.btn_transacoes = ctk.CTkButton(self.frame_menu,text='Transações',font=self.fonte_subtitulo,text_color='black',fg_color='transparent',hover_color="#E3E5E8",command=self.aba_transacoes)
        self.btn_transacoes.grid(row=0,column=1,padx=15,pady=10)

        # Categorias
        self.btn_categorias = ctk.CTkButton(self.frame_menu,text='Categorias',font=self.fonte_subtitulo,text_color='black',fg_color='transparent',hover_color="#E3E5E8")
        self.btn_categorias.grid(row=0,column=2,padx=15,pady=10)

        # Configurações
        self.btn_configs = ctk.CTkButton(self.frame_menu,text='Configurações',font=self.fonte_subtitulo,text_color='black',fg_color='transparent',hover_color="#E3E5E8")
        self.btn_configs.grid(row=0,column=3,padx=15,pady=10)

    
    def main(self):
        # Frame principal que contém a área da esquerda e direita
        self.frame_main = ctk.CTkFrame(self.master, fg_color='white')
        self.frame_main.grid(row=2, column=0, sticky='nsew', padx=10, pady=10)
        
        # permitir expansão
        self.master.rowconfigure(2, weight=1)
        self.master.columnconfigure(0, weight=1)
        
        # duas colunas internas
        self.frame_main.columnconfigure(0, weight=1)  # esquerda menor
        self.frame_main.columnconfigure(1, weight=3)  # direita maior
        self.frame_main.rowconfigure(0, weight=1)
        
        # ----- FRAME LEFT: Resumo do mês -----
        self.frame_left = ctk.CTkFrame(self.frame_main, fg_color='lightblue', corner_radius=10)
        self.frame_left.grid(row=0, column=0, sticky='nsew', padx=(0,10))
        self.frame_left.rowconfigure((0,1,2,3), weight=1)
        self.frame_left.columnconfigure(0, weight=1)
        
        # Exemplo de labels:
        ctk.CTkLabel(self.frame_left, text="Resumo do mês", font=self.fonte_subtitulo).grid(row=0, column=0, pady=5)
        ctk.CTkLabel(self.frame_left, text="Saldo atual: R$ 1.000,00").grid(row=1, column=0)
        ctk.CTkLabel(self.frame_left, text="Gastos: R$ 500,00").grid(row=2, column=0)
        ctk.CTkLabel(self.frame_left, text="Receitas: R$ 1.500,00").grid(row=3, column=0)
        
        # ----- FRAME RIGHT: Transações -----
        self.frame_right = ctk.CTkFrame(self.frame_main, fg_color='lightgray', corner_radius=10)
        self.frame_right.grid(row=0, column=1, sticky='nsew')
        
        # permitir expansão
        self.frame_right.rowconfigure(1, weight=1)  # table cresce
        self.frame_right.columnconfigure(0, weight=1)
        
        # Filtros
        self.frame_filtros = ctk.CTkFrame(self.frame_right)
        self.frame_filtros.grid(row=0, column=0, sticky='we', pady=5)

        # valores das categorias em transações (filtro 0)
        self.entrada_filtro_data_inicio = ctk.CTkEntry(self.frame_filtros,placeholder_text='De: ',width=90)
        self.entrada_filtro_data_inicio.grid(row=0,column=0,pady=3,padx=5)

        # valores de tipo em transações (filtro 1)
        self.entrada_filtro_data_termino = ctk.CTkEntry(self.frame_filtros,placeholder_text='Até: ',width=90)
        self.entrada_filtro_data_termino.grid(row=0,column=1,pady=3,padx=5)


        # valores das categorias em transações (filtro 2)
        self.filtro_categoria = ctk.CTkComboBox(self.frame_filtros,values=TransacaoController.filtro_categoria_transacoes(),width=110)
        self.filtro_categoria.set('Categoria')
        self.filtro_categoria.grid(row=0,column=2,pady=3,padx=5)

        # valores de tipo em transações (filtro 3)
        self.filtro_tipo = ctk.CTkComboBox(self.frame_filtros,values= TransacaoController.filtro_tipo_transacoes(),width=100)
        self.filtro_tipo.set('')        
        self.filtro_tipo.grid(row=0,column=3,pady=3,padx=5)

        # botão de filtrar de acordo com o que foi preenchido
        self.btn_filtrar_view = ctk.CTkButton(self.frame_filtros,text='Filtrar',width=100,command=self.btn_filtrar)
        self.btn_filtrar_view.grid(row=0,column=4,pady=3,padx=5)


        self.entrada_filtro_data_inicio.bind('<ButtonRelease>',self.click_dtinicio)
        self.entrada_filtro_data_termino.bind('<ButtonRelease>',self.click_dttermino)

        # Table Treeview
        self.frame_treeview = ctk.CTkFrame(self.frame_right,fg_color='blue')
        self.frame_treeview.grid(row=1, column=0, sticky='nsew', pady=5)
        self.frame_treeview.columnconfigure(0,weight=1)
        self.frame_treeview.rowconfigure(0,weight=1)

        self.treeview_sistema = ttk.Treeview(self.frame_treeview,show='headings',columns=('col1','col2','col3','col4','col5'))

        # cabeçalho as colunas
        self.treeview_sistema.heading('col1',text='Data')
        self.treeview_sistema.heading('col2',text='Categoria')
        self.treeview_sistema.heading('col3',text='Tipo')
        self.treeview_sistema.heading('col4',text='Valor')
        self.treeview_sistema.heading('col5',text='Observ.')

        # ajuste colunas
        self.treeview_sistema.column('col1',width=90)
        self.treeview_sistema.column('col2',width=100)
        self.treeview_sistema.column('col3',width=70)
        self.treeview_sistema.column('col4',width=100)
        self.treeview_sistema.column('col5',width=175)

        self.treeview_sistema.grid(row=0,column=0,sticky='nswe')
        
        # Botões
        self.frame_botoes = ctk.CTkFrame(self.frame_right)
        self.frame_botoes.columnconfigure((0,1,2,3),weight=1)
        self.frame_botoes.grid(row=2, column=0, sticky='we', pady=5)

        self.btn_nova_transacao = ctk.CTkButton(
            self.frame_botoes,
            text='Nova Transação',
            font=self.fonte_botoes_entradas,
            height=35)
        self.btn_nova_transacao.grid(row=0,column=0,padx=5,pady=5)

        self.btn_editar = ctk.CTkButton(
            self.frame_botoes,
            text='Editar',
            font=self.fonte_botoes_entradas,
            height=35,
            width=80)
        self.btn_editar.grid(row=0,column=1,padx=5,pady=5)

        self.btn_excluir = ctk.CTkButton(
            self.frame_botoes,
            text='Excluir',
            font=self.fonte_botoes_entradas,
            height=35,
            width=80)
        self.btn_excluir.grid(row=0,column=2,padx=5,pady=5)

        self.btn_atualizar = ctk.CTkButton(
            self.frame_botoes,
            text='Atualizar',
            font=self.fonte_botoes_entradas,
            height=35,
            width=80)
        self.btn_atualizar.grid(row=0,column=3,padx=5,pady=5)

    def click_dtinicio(self,e):
        tela_calendario_dtinicio = ctk.CTkToplevel()
        def selecao_dtinicio(e):
            self.data_inicio_selecionada = self.calendario_filtro_inicio.get_date()
            self.entrada_filtro_data_inicio.insert(0,self.data_inicio_selecionada)
            tela_calendario_dtinicio.destroy()

        tela_calendario_dtinicio.bind('<ButtonRelease>',selecao_dtinicio)

        tela_calendario_dtinicio.transient(self.master)   # Diz que o Toplevel pertence à janela master
        tela_calendario_dtinicio.grab_set()         # Bloqueia interação com a janela principal
        tela_calendario_dtinicio.focus_force()

        self.calendario_filtro_inicio = Calendar(tela_calendario_dtinicio,date_pattern='dd/mm/yyyy')
        self.calendario_filtro_inicio.pack()

    def click_dttermino(self,e):
        tela_calendario_dttermino = ctk.CTkToplevel()

        def selecao_dttermino(e):
            data_termino_selecionada = self.calendario_filtro_termino.get_date()
            self.entrada_filtro_data_termino.insert(0,data_termino_selecionada)
            tela_calendario_dttermino.destroy()

        tela_calendario_dttermino.bind('<ButtonRelease>',selecao_dttermino)        


        tela_calendario_dttermino.transient(self.master)   # Diz que o Toplevel pertence à janela master
        tela_calendario_dttermino.grab_set()         # Bloqueia interação com a janela principal
        tela_calendario_dttermino.focus_force()

        self.calendario_filtro_termino = Calendar(tela_calendario_dttermino,date_pattern='dd/mm/yyyy')
        self.calendario_filtro_termino.pack()
           
    def btn_filtrar(self):
        view_filtrada = TransacaoController.view_treeview_filtrada(
            dt_inicio=self.entrada_filtro_data_inicio.get(),
            dt_final=self.entrada_filtro_data_termino.get(),
            categoria=self.filtro_categoria.get(),
            tipo=self.filtro_tipo.get()
        )

        if view_filtrada:
            for id in self.treeview_sistema.get_children():
                self.treeview_sistema.delete(id)
            for linha_filtrada in view_filtrada:
                self.treeview_sistema.insert('',ctk.END,text='',values=(linha_filtrada[0],linha_filtrada[1],linha_filtrada[2],linha_filtrada[3],linha_filtrada[4]))

    def btn_filtrar_transacao(self):
        view_filtrada_transacao = TransacaoController.view_treeview_transacoes_filtrada(
            dt_inicio=self.entrada_filtro_data_inicio.get(),
            dt_final=self.entrada_filtro_data_termino.get(),
            categoria=self.filtro_categoria.get(),
            tipo=self.filtro_tipo.get()
        )

        if view_filtrada_transacao:
            for id in self.treeview_transacoes.get_children():
                self.treeview_transacoes.delete(id)
            for linha_filtrada in view_filtrada_transacao:
                self.treeview_transacoes.insert('',ctk.END,text='',values=(linha_filtrada[0],linha_filtrada[1],linha_filtrada[2],linha_filtrada[3],linha_filtrada[4],linha_filtrada[5]))
        
    def view_treeview(self):
        self.linhas_view_frame_main = TransacaoController.view_treeview()
        
        for id in self.treeview_sistema.get_children():
            self.treeview_sistema.delete(id)
        if self.linhas_view_frame_main:
            for linha in self.linhas_view_frame_main:
                self.treeview_sistema.insert('',ctk.END,text='',values=(linha[0],linha[1],linha[2],linha[3],linha[4]))

    def view_treeview_transacoes(self):
        self.linhas_view_frame_transacoes = TransacaoController.view_treeview_transacoes()
        
        for id in self.treeview_transacoes.get_children():
            self.treeview_transacoes.delete(id)
        if self.linhas_view_frame_transacoes:
            for linha in self.linhas_view_frame_transacoes:
                self.treeview_transacoes.insert('',ctk.END,text='',values=(linha[0],linha[1],linha[2],linha[3],linha[4],linha[5]))

    def aba_inicio(self):
        self.treeview_transacoes.grid_remove()
        self.treeview_sistema.grid()


    def aba_transacoes(self):
        # Ocultando treview aba início
        self.treeview_sistema.grid_remove()  

        # Criando Frame histórico transações      
        self.treeview_transacoes = ttk.Treeview(self.frame_treeview,show='headings',columns=('col1','col2','col3','col4','col5','col6'))        

        # cabeçalho as colunas
        self.treeview_transacoes.heading('col1',text='ID')
        self.treeview_transacoes.heading('col2',text='Tipo')
        self.treeview_transacoes.heading('col3',text='Valor')
        self.treeview_transacoes.heading('col4',text='Descrição')
        self.treeview_transacoes.heading('col5',text='Dt Transação')
        self.treeview_transacoes.heading('col6',text='Dt Registro')

        # ajuste colunas
        self.treeview_transacoes.column('col1',width=70)
        self.treeview_transacoes.column('col2',width=80)
        self.treeview_transacoes.column('col3',width=70)
        self.treeview_transacoes.column('col4',width=115)
        self.treeview_transacoes.column('col5',width=100)      
        self.treeview_transacoes.column('col6',width=100)      

        self.treeview_transacoes.grid(row=0,column=0,sticky='nswe')
        self.view_treeview_transacoes()
        self.btn_filtrar_view.configure(command=self.btn_filtrar_transacao)

       