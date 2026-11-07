import os
from dotenv import load_dotenv
from llm_service import LLMService

# Carrega as variáveis do arquivo .env
load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")
if __name__ == "__main__":
    print("=" * 40)
    print("RESUMIDOR DE TEXTOS COM IA (Versao 2.0)")
    print("=" * 40)

    # Nome do arquivo que o usuário deve criar
    arquivo_entrada = "texto.txt"

 # Verifica se o arquivo existe
    if not os.path.exists(arquivo_entrada):
        print(f"Erro: O arquivo '{arquivo_entrada}' nao foi encontrado.")
        print(f"Por favor, crie um arquivo chamado '{arquivo_entrada}' na pasta P0 e cole o texto nele.")
    else:
        print(f"Lendo o arquivo '{arquivo_entrada}'...")
        
        # Abre e lê o arquivo
        with open(arquivo_entrada, "r", encoding="utf-8") as f:
            texto_completo = f.read()

        if not texto_completo.strip():
            print("O arquivo esta vazio. Insira um texto para resumir.")
        else:
            print("Processando com o Gemini, aguarde...\n")
            
            # Instancia o serviço e chama o método
            service = LLMService()
            resultado = service.resumir_texto(texto_completo)
            
            print("-" * 40)
            print("RESUMO GERADO:")
            print("-" * 40)
            print(resultado)
            print("-" * 40)