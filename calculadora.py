import customtkinter as ctk

from tkinter import messagebox, Toplevel

import re  # Biblioteca para expressões regulares

import os

# Caminho do diretório onde o script está localizado
diretorio_atual = os.path.dirname(os.path.abspath(__file__))

# Caminho completo para o arquivo cor_padrao.txt na mesma pasta do script
arquivo_padrao_cor = os.path.join(diretorio_atual, "cor_padrao.txt")

# Variável de controle para monitorar se a janela de cores está aberta
janela_cores_aberta = False
janela_cores = None


class Janela(ctk.CTk):
    """Classe que representa a janela principal da calculadora."""

    def __init__(self, tit="", siz="300x500"):
        """
        Inicializa a janela da calculadora.
        
        :param tit: Título da janela.
        :param siz: Tamanho da janela (ex: "300x500").
        """
        super().__init__()
        self.title(tit)  
        self.geometry(siz) 
        self.maxsize(450,500)
        self.minsize(300,300)

        self.bind("<Key>", self.key_pressed)  # Vincular o evento de tecla à janela
        
    def key_pressed(self, event):
        """
        Processa o evento de tecla pressionada.
        
        :param event: Evento de teclado.
        """

        # Mapeamento das teclas para suas funções
        mapeamento = {
            "Return": calcular,
            "BackSpace": backspace,
            "Delete": limpar,
            "Escape": limpar
        }

        # Detectar Shift + % (em teclados com layout específico ou Shift + 5 em outros teclados)
        if event.keysym == "percent" or (event.keysym == "5" and event.state & 0x1):
            adicionar_texto("%")
            
        # Adicionar texto para caracteres válidos
        if event.char in "0123456789+-*/^,":
            adicionar_texto(event.char)
        
        # Chamar a função correspondente se a tecla estiver mapeada
        if event.keysym in mapeamento:
            mapeamento[event.keysym]()
            
            
class Objetos:
    """Classe que gerencia os objetos da calculadora."""

    def __init__(self, janela):
        """
        Inicializa os objetos da calculadora.
        
        :param janela: Instância da janela da calculadora.
        """
        self.janela = janela
        self.display_text = ""  # Armazenar o texto do display
        self.max_digitos = 25  # Limite de 25 caracteres no display
        
        
    def criar_label(self, x, y, rx, ry, txt, ancora="e", cor_frente="darkgreen"):
        """
        Cria um label na janela.
        
        :param x: Posição relativa no eixo x.
        :param y: Posição relativa no eixo y.
        :param rx: Largura relativa do label.
        :param ry: Altura relativa do label.
        :param txt: Texto a ser exibido no label.
        :param ancora: Alinhamento do texto no label.
        :param cor_frente: Cor de fundo do label.
        :return: O widget label criado.
        """
        self.label = ctk.CTkLabel(
            self.janela, 
            font=("arial", 14, "bold"), 
            text=txt, 
            bg_color=cor_frente, 
            anchor=ancora, 
            padx=10, 
            pady=5
            )
            
        self.label.place(
            relx=x, 
            rely=y, 
            relwidth=rx, 
            relheight=ry
            )
        
        return self.label  # Retorna o widget criado


    def criar_botao(self, x, y, rx, ry, txt, cor_frente="green", cor_hover="black", comando=None):    
        """
        Cria um botão na janela.
        
        :param x: Posição relativa no eixo x.
        :param y: Posição relativa no eixo y.
        :param rx: Largura relativa do botão.
        :param ry: Altura relativa do botão.
        :param txt: Texto a ser exibido no botão.
        :param cor_frente: Cor de fundo do botão.
        :param cor_hover: Cor do botão ao passar o mouse.
        :param comando: Função a ser chamada ao clicar no botão.
        :return: O widget botão criado.
        """
        self.botao = ctk.CTkButton(
            self.janela, 
            text=txt, 
            font=("arial", 15, "bold"), 
            fg_color=cor_frente, 
            hover_color=cor_hover, 
            bg_color="darkgreen", 
            command=comando
            )
            
        self.botao.place(
            relx=x, 
            rely=y, 
            relwidth=rx, 
            relheight=ry
            )
            
        return self.botao  # Retorna o widget criado

    
    # Função para atualizar o texto do display
    def atualizar_display(self, valor):    
        """
        Atualiza o texto exibido no display da calculadora.
        
        :param valor: Valor a ser adicionado ao display.
        """        
        # Contar os caracteres no display sem considerar espaços
        caracteres_sem_espacos = len(self.display_text.replace(" ", ""))
        
        # Verificar se ainda pode adicionar mais caracteres (limite 25)
        if caracteres_sem_espacos < self.max_digitos:
            
            self.display_text += valor  # Adicionar o valor ao texto existente
            
            self.label.configure(text=self.display_text)  # Atualizar o texto no display
            
        else:
            
            messagebox.showinfo("Limite Excedido!", "Limite de 25 caracteres atingido")
            # print("Limite de 25 caracteres atingido")  # Para fins de debug, você pode remover isso depois.

    # Função para limpar o display
    def limpar_display(self):
        """Limpa o texto do display da calculadora."""
        
        self.display_text = ""
        
        self.label.configure(text=self.display_text)


# Função de callback para cada botão que adiciona o texto ao display
def adicionar_texto(valor):
    """
    Adiciona texto ao display da calculadora.
    
    :param valor: Valor a ser adicionado.
    """
    objetos.atualizar_display(valor)

# Função para limpar o display
def limpar():
    """Limpa o display da calculadora."""
    objetos.limpar_display()

def backspace():
    """Remove o último caractere do display da calculadora."""
    if objetos.display_text:  # Verifica se há algo para apagar
        
        objetos.display_text = objetos.display_text[:-1]
        
        objetos.label.configure(text=objetos.display_text)

def inverter_sinal():
    """Inverte o sinal do número exibido no display da calculadora."""
    
    if objetos.display_text:
        
        if objetos.display_text.startswith("-"):
            
            objetos.display_text = objetos.display_text[1:]  # Remove o sinal de menos
        
        else:
            
            objetos.display_text = "-" + objetos.display_text  # Adiciona o sinal de menos
        
        objetos.label.configure(text=objetos.display_text)

# Função para copiar o texto do display para a área de transferência
def copiar_para_clipboard():
    """Copia o texto do display para a área de transferência."""
    
    root.clipboard_clear()  # Limpa a área de transferência
    
    root.clipboard_append(objetos.display_text)  # Copia o conteúdo do display para a área de transferência
    
    messagebox.showinfo("Copiado", "Texto copiado para a área de transferência!")  # Mensagem de confirmação
    

def calcular():
    """Calcula a expressão matemática exibida no display e atualiza o display com o resultado."""
    try:
        # Substituir vírgulas por pontos na expressão antes de calcular
        expressao = objetos.display_text.replace(",", ".")
        
        # Identificar e calcular a porcentagem de cada número que tem '%'
        expressao = re.sub(r'(\d+(\.\d+)?)%', r'(\1/100)', expressao)
        
        # Usar a expressão modificada (substituindo '^' por '**' para potências)
        resultado = eval(expressao.replace("^", "**"))
        
        # Arredondar o resultado para no máximo 6 casas decimais
        if isinstance(resultado, float):
            resultado = round(resultado, 6)
        
        # Converter o resultado para string
        resultado_str = str(resultado)

        # Atualizar o display com o resultado, substituindo pontos por vírgulas
        objetos.label.configure(text=resultado_str.replace(".", ","))
        objetos.display_text = resultado_str  # Atualiza o display com o resultado (mantendo o ponto internamente)
        
    except Exception as e:
        messagebox.showerror("Erro", "Expressão inválida")


# Função para salvar a cor padrão em um arquivo de texto
def salvar_cor_padrao(cor):
    """
    Salva a cor padrão em um arquivo de texto.
    
    :param cor: Cor padrão a ser salva.
    """
    with open(arquivo_padrao_cor, 'w') as arquivo:
        arquivo.write(cor)

# Função para carregar a cor padrão do arquivo
def carregar_cor_padrao():
    """
    Carrega a cor padrão do arquivo de texto, se existir.
    
    :return: Cor padrão salva ou "Verde" se não existir o arquivo.
    """
    if os.path.exists(arquivo_padrao_cor):
        with open(arquivo_padrao_cor, 'r') as arquivo:
            return arquivo.read().strip()  # Retorna a cor salva sem espaços
    return "Verde"  # Retorna "Verde" como padrão se não houver arquivo

# Esquemas de cores com identificadores
esquemas_cores = {
    "Branco": ("white", "gray", "black", "black"),
    "Verde": ("green", "white", "darkgreen", "black"),
    "Azul": ("blue", "white", "darkblue", "black"),
    "Preto": ("black", "white", "gray", "black"),
    "Vermelho": ("red", "white", "darkred", "black"),
    "Roxo": ("#32003A", "white", "#322C3A", "black"),
    "Laranja": ("#FF4000", "white", "#650000", "black"),
    "Cinza": ("gray", "white", "black", "gray")
}

# Dicionário para armazenar os IntVar dos checkboxes
checkbox_vars = {}

def alterar_cores(cor_display, cor_texto_botao, cor_titulo, cor_menu, cor_padrao):
    """
    Altera as cores dos elementos da calculadora e atualiza o checkbox selecionado.
    """
    # Alterar cores dos botões e display
    for widget in root.winfo_children():
        if isinstance(widget, ctk.CTkButton) and widget.cget("text") != "Ξ":
            widget.configure(fg_color=cor_display, text_color=cor_texto_botao)
        elif isinstance(widget, ctk.CTkLabel):
            widget.configure(fg_color=cor_display, text_color=cor_texto_botao)

    # Alterar a cor do display, botões "Copy" e "Backspace"
    display.configure(fg_color=cor_titulo, text_color=cor_texto_botao)
    but_copiar.configure(fg_color=cor_titulo, text_color=cor_texto_botao)
    but_backspace.configure(fg_color=cor_titulo, text_color=cor_texto_botao)

    # Alterar cor do menu (botão "Ξ")
    but_menu.configure(fg_color=cor_menu, text_color=cor_texto_botao)

    # Marcar o checkbox correspondente e desmarcar os outros
    for cor, var in checkbox_vars.items():
        if cor == cor_padrao:
            var.set(1)
        else:
            var.set(0)


# Função chamada quando o checkbox é marcado
def selecionar_cor_padrao(cor):
    """
    Seleciona a cor padrão, salva no arquivo e atualiza as cores.
    """
    salvar_cor_padrao(cor)
    esquema = esquemas_cores[cor]
    alterar_cores(*esquema, cor)

def criar_checkboxes(janela):
    """
    Cria os checkboxes ao lado dos botões de cor, cada um em uma linha separada.
    """
    for cor, esquema in esquemas_cores.items():
        frame = ctk.CTkFrame(janela_cores)  # Cria um frame para alinhar botão e checkbox
        frame.pack(fill="x", padx=10, pady=5)  # Preenche horizontalmente e adiciona padding

        var = ctk.IntVar(value=1 if cor == cor_padrao else 0)  # Define o valor inicial
        checkbox_vars[cor] = var

        # Botão de cor
        btn = ctk.CTkButton(
            frame,  # Adiciona o botão no frame
            text=cor, 
            fg_color=esquema[0], 
            text_color=esquema[1], 
            command=lambda esq=esquema: alterar_cores(*esq, cor)
        )
        btn.pack(side="left", padx=5)  # Alinha o botão à esquerda com padding

        # Checkbox de seleção
        checkbox = ctk.CTkCheckBox(
            frame,  # Adiciona o checkbox no mesmo frame
            text="Padrão", 
            variable=var, 
            command=lambda c=cor: selecionar_cor_padrao(c)
        )
        checkbox.pack(side="left", padx=5)  # Alinha o checkbox à esquerda


# Função para abrir a janela de seleção de cores com checkboxes
def abrir_fechar_janela_cores():
    global janela_cores_aberta, janela_cores
    
    if janela_cores_aberta:
        if janela_cores is not None:
            janela_cores.destroy()
        janela_cores_aberta = False
    else:
        janela_cores = Toplevel(root)
        janela_cores.title("Selecionar Cores")
        janela_cores.geometry("300x320+600+100")
        criar_checkboxes(janela_cores)
        janela_cores_aberta = True        
        
# Cria os objetos e insere o label e botões na janela
root = Janela("Calculadora")
objetos = Objetos(root)

# Criar botão
but_size_width = 0.225
but_size_height = 0.14
but_pos_x = 0.01
but_pos_y = 0.23

# Definir espaçamento
espacamento = 0.005  # Exemplo de espaçamento entre os widgets

display = objetos.criar_label(
    espacamento, 
    espacamento + 0.11, 
    0.995, 
    0.1, 
    "", 
    "e", 
    "black"
    )
    
but_menu = objetos.criar_botao(
    espacamento + 0.01, 
    espacamento + 0.01, 
    but_size_width - 0.02, 
    but_size_height - 0.05, 
    " Ξ ", 
    "black", 
    comando=abrir_fechar_janela_cores
    )
    
but_copiar = objetos.criar_botao(
    espacamento + but_size_width + 0.02, 
    espacamento + 0.01, 
    but_size_width + 0.12, 
    but_size_height - 0.05, 
    "📝 copiar", 
    "darkgreen", 
    comando=copiar_para_clipboard
    )
    
but_backspace = objetos.criar_botao(
    espacamento + 0.63, 
    espacamento + 0.01, 
    but_size_width + 0.12, 
    but_size_height - 0.05, 
    "⌫", 
    "darkgreen", 
    comando=backspace
    )

# Criar botões com espaçamento
but_divided = objetos.criar_botao(
    but_pos_x + espacamento + 0.75, 
    but_pos_y + espacamento, 
    but_size_width, 
    but_size_height, 
    "/", 
    comando=lambda: adicionar_texto("/")
    )
    
but_del = objetos.criar_botao(
    but_pos_x + espacamento + 0.50, 
    but_pos_y + espacamento, 
    but_size_width, 
    but_size_height, 
    "C", comando=limpar
    )
    
but_percent = objetos.criar_botao(
    but_pos_x + espacamento + 0.25, 
    but_pos_y + espacamento, 
    but_size_width, 
    but_size_height, 
    "%", comando=lambda: adicionar_texto("%")
    )
    
but_power = objetos.criar_botao(
    but_pos_x + espacamento, 
    but_pos_y + espacamento, 
    but_size_width, 
    but_size_height, 
    "^ POW", 
    comando=lambda: adicionar_texto("^")
    )
    
but_times = objetos.criar_botao(
    but_pos_x + espacamento + 0.75, 
    but_pos_y + espacamento + 0.15, 
    but_size_width, 
    but_size_height, 
    "X", 
    comando=lambda: adicionar_texto("*")
    )
    
but_9 = objetos.criar_botao(
    but_pos_x + espacamento + 0.50, 
    but_pos_y + espacamento + 0.15, 
    but_size_width, 
    but_size_height, 
    "9", 
    comando=lambda: adicionar_texto("9")
    )
    
but_8 = objetos.criar_botao(
    but_pos_x + espacamento + 0.25, 
    but_pos_y + espacamento + 0.15, 
    but_size_width, 
    but_size_height, 
    "8", 
    comando=lambda: adicionar_texto("8")
    )
    
but_7 = objetos.criar_botao(
    but_pos_x + espacamento, 
    but_pos_y + espacamento + 0.15, 
    but_size_width, 
    but_size_height, 
    "7", 
    comando=lambda: adicionar_texto("7")
    )

but_minus = objetos.criar_botao(
    but_pos_x + espacamento + 0.75, 
    but_pos_y + espacamento + 0.30, 
    but_size_width, 
    but_size_height, 
    "-", 
    comando=lambda: adicionar_texto("-")
    )
    
but_6 = objetos.criar_botao(
    but_pos_x + espacamento + 0.50, 
    but_pos_y + espacamento + 0.30, 
    but_size_width, 
    but_size_height, 
    "6", 
    comando=lambda: adicionar_texto("6")
    )
    
but_5 = objetos.criar_botao(
    but_pos_x + espacamento + 0.25, 
    but_pos_y + espacamento + 0.30, 
    but_size_width, 
    but_size_height, 
    "5", 
    comando=lambda: adicionar_texto("5")
    )
    
but_4 = objetos.criar_botao(
    but_pos_x + espacamento, 
    but_pos_y + espacamento + 0.30, 
    but_size_width, 
    but_size_height, 
    "4", 
    comando=lambda: adicionar_texto("4")
    )

but_plus = objetos.criar_botao(
    but_pos_x + espacamento + 0.75, 
    but_pos_y + espacamento + 0.45, 
    but_size_width, 
    but_size_height, 
    "+", 
    comando=lambda: adicionar_texto("+")
    )
    
but_3 = objetos.criar_botao(
    but_pos_x + espacamento + 0.50, 
    but_pos_y + espacamento + 0.45, 
    but_size_width, 
    but_size_height, 
    "3", 
    comando=lambda: adicionar_texto("3")
    )
    
but_2 = objetos.criar_botao(
    but_pos_x + espacamento + 0.25, 
    but_pos_y + espacamento + 0.45, 
    but_size_width, 
    but_size_height, 
    "2", 
    comando=lambda: adicionar_texto("2")
    )
    
but_1 = objetos.criar_botao(
    but_pos_x + espacamento, 
    but_pos_y + espacamento + 0.45, 
    but_size_width, 
    but_size_height, 
    "1", 
    comando=lambda: adicionar_texto("1")
    )

but_equal = objetos.criar_botao(
    but_pos_x + espacamento + 0.75, 
    but_pos_y + espacamento + 0.60, 
    but_size_width, 
    but_size_height, 
    "=", 
    comando=calcular
    )
    
but_comma = objetos.criar_botao(
    but_pos_x + espacamento + 0.50, 
    but_pos_y + espacamento + 0.60, 
    but_size_width, 
    but_size_height, 
    ",", 
    comando=lambda: adicionar_texto(",")
    )

but_0 = objetos.criar_botao(
    but_pos_x + espacamento + 0.25, 
    but_pos_y + espacamento + 0.60, 
    but_size_width, 
    but_size_height, 
    "0", 
    comando=lambda: adicionar_texto("0")
    )

but_negate = objetos.criar_botao(
    but_pos_x + espacamento, 
    but_pos_y + espacamento + 0.60, 
    but_size_width, 
    but_size_height, 
    "+/-", 
    comando=inverter_sinal
    )


# Carregar a cor padrão ao iniciar o programa
cor_padrao = carregar_cor_padrao()
esquema_padrao = esquemas_cores.get(cor_padrao, esquemas_cores["Verde"])  # Usa o esquema "Verde" se a cor não for encontrada
alterar_cores(*esquema_padrao, cor_padrao)

root.mainloop()

