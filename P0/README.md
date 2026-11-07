# Resumidor de Textos com IA (Gemini)

Este projeto foi desenvolvido como parte do P0 (Primeiro fluxo com LLM). É uma aplicação Python que utiliza a API do Google Gemini para resumir textos longos em 3 tópicos principais.

## Funcionalidades
- Lê o conteúdo de um arquivo `texto.txt`.
- Envia o texto para o modelo Gemini (via API REST).
- Retorna um resumo estruturado em até 3 tópicos.
- Possui tratamento de erros amigável (caso a API falhe ou a chave seja inválida).

## Pré-requisitos
- Python 3.10 ou superior
- Uma chave de API do Google Gemini (obtida no Google AI Studio)

## Como executar

## Como executar o projeto

 **Clone o repositório:**
   ```bash
   git clone https://github.com/fernandalaraalves/trends-IA.git
   cd trends-IA/P0

  **Crie e ative um ambiente virtual:**
  ```bash
  python -m venv venv
# No Windows (Git Bash):
source venv/Scripts/activate
# No Linux/Mac:
# source venv/bin/activate

  **Instale as dependências:**
 ```bash
 pip install -r requirements.txt

 **Configure a chave de API:**
 env
 GEMINI_API_KEY=coloque_a_sua_chave_no_env

 **Prepare o texto:**
 Crie um arquivo chamado texto.txt dentro da pasta P0 e cole o texto que você deseja resumir.


 **Execute a aplicação:**
```bash
 python main.py
   
   Estrutura do Projeto:
- main.py: Ponto de entrada da aplicação (interface com o usuário e leitura de arquivo).

- llm_service.py: Módulo responsável pela comunicação com a API do Gemini e tratamento de erros.

- requirements.txt: Lista de dependências do projeto.

- .env: Arquivo (não versionado) para armazenar credenciais sensíveis.

- texto.txt: Arquivo de entrada com o texto a ser resumido.