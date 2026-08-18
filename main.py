import time
import customtkinter as ctk

ctk.set_appearance_mode("system") #aparência de acordo com o sistema operacional

#boas vindas e personalização do usuário
print("Bem-vindo ao Água! Vamos manter você hidratado.")

meta_input = input("Digite a quantidade de água que você deseja beber por hora (padrão: 100 ml): ")
meta_ml = int(meta_input) if meta_input.strip() != "" else 100 #dose padrão

#contagem do sucesso do usuário
total_ml_bebidos = 0
vezes_bebeu = 0

print(f"Você definiu sua meta de beber {meta_ml} ml de água por hora.")
print("Água! iniciado com sucesso. Você receberá uma notificação a cada hora para se lembrar de beber água.")

def mostrar_notificacao():
    global total_ml_bebidos, vezes_bebeu, meta_ml

    janela = ctk.CTk()
    janela.iconbitmap("icone.ico")  # Substitua pelo caminho do seu ícone
    janela.title("Água!")
    janela.geometry("360x220")
    janela.attributes("-topmost", True)

    titulo = ctk.CTkLabel(
        janela, text="Hora do gole!", font=("Helvetica", 18, "bold"),
        text_color="#EB84CA"
    )
    titulo.pack(pady=(15, 5))

    mensagem = ctk.CTkLabel(
        janela,
        text=f"De gole em gole a pele fica hidratada!\n Pausa para {meta_ml} ml de água.",
        font=("Helvetica", 12),
    )
    mensagem.pack(pady=5)

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
        text="Bebi!",
        command=lambda: confirmar(janela),  # Envia a janela para a função
        fg_color="#EB84CA",
        hover_color="#DB59CE",
        corner_radius=20,
    )
    botao.pack(pady=15)

    janela.mainloop()

INTERVALO_SEGUNDOS = 3600  # 1 hora em segundos
while True:
    time.sleep(INTERVALO_SEGUNDOS)
    mostrar_notificacao()