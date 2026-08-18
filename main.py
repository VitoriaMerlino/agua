import time
import customtkinter as ctk

ctk.set_appearance_mode("system") #aparência de acordo com o sistema operacional

meta_ml = 100  # valor padrão
#contagem do sucesso do usuário
total_ml_bebidos = 0
vezes_bebeu = 0

#print(f"Você definiu sua meta de beber {meta_ml} ml de água por hora.")
#print("Água! iniciado com sucesso. Você receberá uma notificação a cada hora para se lembrar de beber água.\nBoa sorte!🌟")

def mostrar_notificacao():
    global total_ml_bebidos, vezes_bebeu, meta_ml

    janela = ctk.CTk()
    janela.iconbitmap("icone.ico")  # Substitua pelo caminho do seu ícone
    janela.title("Água!")
    janela.geometry("360x220")
    janela.attributes("-topmost", True)

    titulo = ctk.CTkLabel(
        janela, text="✨ Hora do Gole! ✨", font=("Helvetica", 18, "bold"),
        text_color="#EB84CA"
    )
    titulo.pack(pady=(15, 5))

    mensagem = ctk.CTkLabel(
        janela,
        text=f"💧 De gole em gole a pele fica hidratada!\n🌸 Pausa para {meta_ml} ml de água.",
        font=("Helvetica", 12),
    )
    mensagem.pack(pady=5)

    progresso = ctk.CTkLabel(
        janela,
        text=(
            f"📊 Hoje você já bebeu: {total_ml_bebidos} ml ({vezes_bebeu}"
            " pausas)"
        ),
        font=("Helvetica", 11, "italic"),
        text_color="#6B7280",
    )
    progresso.pack(pady=(0, 10))

    def confirmar(janela_alvo):
        global total_ml_bebidos, vezes_bebeu, meta_ml
        total_ml_bebidos += meta_ml
        vezes_bebeu += 1
        print(
            f"Você bebeu {meta_ml} ml de água. Total de água bebida:"
            f" {total_ml_bebidos} ml em {vezes_bebeu} vezes."
        )
        janela_alvo.destroy()

    botao = ctk.CTkButton(
        janela,
        text="Bebi! 💖",
        command=lambda: confirmar(janela),  # Envia a janela para a função
        fg_color="#EB84CA",
        hover_color="#DB59CE",
        corner_radius=20,
    )
    botao.pack(pady=15)

    janela.mainloop()

def criar_tela_inicial():
    global metal_ml
    #cria a janela de configuração da meta
    janela_config = ctk.CTk()
    janela_config.title("Água! - Configuração de Meta")
    janela_config.geometry("380x280")
    janela_config.iconbitmap("icone.ico") 
    #textos informativos
    titulo =ctk.CTkLabel(
      janela_config,
      text = "Bem-vindo ao Água! 💧",
      font = ("Helvetica", 20, "bold"),  
    )
    titulo.pack(pady=(20, 5))

    subtitulo = ctk.CTkLabel(
        janela_config,
        text = "Defina sua meta de consumo de água por hora (ml):",
        font = ("Helvetica", 13),
        )
    subtitulo.pack(pady=5)

    #campo de entrada para a meta
    entrada_meta = ctk.CTkEntry(
        janela_config,
        placeholder_text="Ex: 100",
        width=200,
        height=30,
        border_width=2,
        corner_radius=10,
        justify="center",
    )
    entrada_meta.pack(pady=15)

    #ação do botão de confirmação
    def salvar_e_iniciar():
        global meta_ml
        valor_digitado = entrada_meta.get().strip()

        if valor_digitado.isdigit() and int(valor_digitado) > 0:
            meta_ml = int(valor_digitado)
        else:
            meta_ml = 100  # valor padrão caso a entrada seja inválida
        janela_config.destroy()

    #botão de iniciar
    botao_iniciar = ctk.CTkButton(
        janela_config,
        text="Iniciar 💧",
        command=salvar_e_iniciar,
        fg_color="#EB84CA",
        hover_color="#DB59CE",
        corner_radius=20,
    )
    botao_iniciar.pack(pady=15)
    janela_config.mainloop()

#primeiro a janela de configuração da meta
criar_tela_inicial()
#agora se inicia o loop
INTERVALO_SEGUNDOS = 3600  # 1 hora em segundos
while True:
    time.sleep(INTERVALO_SEGUNDOS)
    mostrar_notificacao()