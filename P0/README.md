# Resumidor de Textos com IA (Gemini)

Este projeto foi desenvolvido como parte do P0 (Primeiro fluxo com LLM). É uma aplicação Python que utiliza a API do Google Gemini para resumir textos longos em 3 tópicos principais.

## Pré-requisitos
- Python 3.10 ou superior
- Uma chave de API do Google Gemini (obtida no Google AI Studio)

## Como executar

### 1. Clone o repositório.
### 2. Crie e ative um ambiente virtual:
   ```bash
   python -m venv venv
   source venv/Scripts/activate  # Windows (Git Bash)

   Instale as dependências:

bash
pip install -r requirements.txt
Crie um arquivo .env na pasta P0 e adicione sua chave:

env
GEMINI_API_KEY=adicione_sua_chave_no_env
Execute o projeto:

bash
python main.py
text

### 3. Suba para o GitHub
No terminal, na raiz do seu projeto (`trends-IA`), rode:
```bash
git add .
git commit -m "feat(P0): conclui nivel basico do resumidor de textos com Gemini"
git push origin main
