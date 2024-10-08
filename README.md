# Relatório de Ocorrências de Problemas Urbanos 

# 🏙️ SolucionaPII

<img src="https://github.com/user-attachments/assets/a36d1fde-ff75-4b1f-871b-9ddb5cae60ee" width="400"></img>
<img src="https://github.com/user-attachments/assets/8dfa2c33-7179-4caa-b3cc-ff72099274d3" width="400"></img>

## 📜 Sobre o sistema

Esta aplicação foi desenvolvida como parte de um pequeno trabalho acadêmico de Engenharia de Software III, da graduação em Análise e Desenvolvimento de Sistemas (ADS). A ideia surgiu a partir de brainstormings e tem como objetivo facilitar o registro de problemas urbanos por parte da população. O sistema permite que os usuários relatem problemas como buracos nas ruas, lixo em terrenos baldios, iluminação pública defeituosa, entre outros.

### 💻 Ferramentas Utilizadas
- **Linguagem de Programação**: Python 🐍;
- **Framework**: Flask 🌐;
- **Banco de Dados**: PostgreSQL 🗄️;
- **Front-end**: HTML e CSS 🖥️;
- **Design**: Baseado em [Coolors](https://coolors.co/), [Fontes](https://fonts.google.com/), [Pinterest](https://br.pinterest.com/) e [Flaticon](https://www.flaticon.com/).

### 🏗️ Estrutura do Sistema
O sistema é dividido em três principais páginas:
- 🔐 **Login**: Tela onde o usuário faz login com suas credenciais.
- 👤 **Cadastro**: Página para novos usuários criarem uma conta com nome, sobrenome, CPF, e-mail, endereço e senha.
- 📍 **Ocorrências**: Formulário para o usuário relatar um problema urbano, detalhando a localização, tipo de problema, descrição, e anexando fotos.

### 🛠️ Como Rodar o Projeto
Para rodar o sistema, você precisará dos seguintes pacotes instalados:

1. Clone o repositório:
   ```bash
   git clone https://github.com/Evertonmacedo054/SolucionaURB

2. Verifique se você já tem o Python instalado:
    ```bash
    python3 --version

3. Crie um ambiente virtual:
    ```bash
    python3 -m venv venv

    source venv/bin/activate  # Para Linux/Mac

    venv\Scripts\activate     # Para Windows

4. Instale o Flask:
    ```bash
    pip install flask

5. Crie o banco de dados
    ```bash
    psql -U postgres
6. Dentro do console do PostgreSQL, execute:
    ```bash
    CREATE DATABASE nome_do_banco;
