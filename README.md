# Água! - Lembrete pessoal de hidratação
Pop-ups para lembrar você de se hidratar durante o dia com pequenos goles, sem pressão!
---

## funcionalidades
- **⚙️ Configuração Inicial:** Defina sua meta de água em ml por hora assim que abre o aplicativo.
- **🔔 Notificações Automáticas:** Lembretes visuais na tela a cada (uma) hora.
- **📊 Acompanhamento de progresso:** Veja quanto de água já bebeu e quantas pausas fez no dia direto no pop-up.
- **📌 Bandeja do Windows (System Tray):** O app roda discretamente perto do relógio com opção de encerrar pelo botão direito.

## A ideia por trás do projeto:
A necessidade pessoal da desenvolvedora de beber água (e não lembrar disso) acabou por inspirar esse programinha super amigável. Nada de pressão para beber um litro por vez, às vezes pequenos goles já fazem diferença.

---

## 🎁 Como Baixar e Usar (Windows)

Não precisa ter o Python instalado!

1. Vá na aba de [**Releases**](../../releases) aqui do repositório.
2. Baixe o arquivo `Água!.zip`.
3. Extraia o arquivo em qualquer pasta do seu computador.
4. Abra a pasta e dê dois cliques no **`Água.exe`** para iniciar! ✨
5. Para encerrar é só clicar com o botão direito no ícone do app na bandeja e finalizar o aplicativo.

---

## 💻 Como Rodar o Código Localmente (Desenvolvedores)

Se você quiser explorar ou modificar o código-fonte:

### Pré-requisitos
- Python 3.10 ou superior instalado.

### Passo a Passo
- Clone este repositório
- Crie e ative o ambiente virtual (venv)
- Instale as dependências (pip install -r requirements.txt)
- Execute o aplicativo

---

## Tecnologias utilizadas

* **Python 3**
* **CustomTkinter** (para notificações personalizadas)
* **Pystray** (integração com a bandeja do windows)
* **PyInstaller** (Compilação do script para executável)
* **Git e Github** (para controle de versão)

---

## 🧠 O que aprendi neste projeto

Durante o desenvolvimento do **Água!**, explorei diversos conceitos práticos de programação em Python, interface gráfica e empacotamento de software:

- **🐍 Lógica e Estado em Python:** Manipulação de variáveis globais, escopo de funções e controle do fluxo de execução com loops e temporizadores (`time.sleep`).
- **🎨 Interface Gráfica Moderna (GUI):** Construção de janelas dinâmicas, botões, campos de texto (`Entry`) e estilização com a biblioteca `CustomTkinter`.
- **📌 Aplicação em Segundo Plano:** Gerenciamento do ciclo de vida da aplicação e controle da bandeja de sistema do Windows (*System Tray*) com `pystray`.
- **⚙️ Resolução de Desafios Técnicos:** Lidar com comportamentos assíncronos (threads), gerenciamento correto do encerramento de processos com `os._exit()` e tratamento seguro no carregamento de ativos (`icone.ico`).
- **📦 Empacotamento para Produção:** Transformação do script Python em um arquivo executável standalone (`.exe`) com `PyInstaller` e gerenciamento de dependências via `requirements.txt`.
- **🛠️ Controle de Versão:** Boas práticas com `Git` e `GitHub` (commits semânticos, uso do `.gitignore` para pastas de build e criação de documentação).


Projeto desenvolvido com foco no aprendizado de Python e GUIs, contando com o apoio de Inteligência Artificial como assistente de código e mentora de arquitetura.
