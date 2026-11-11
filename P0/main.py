import os
import sys
from dotenv import load_dotenv
from llm_service import LLMService

# Carrega as variáveis do arquivo .env
load_dotenv()

def validar_configuracao():
    """Valida se a chave de API está presente (Tratamento de credencial ausente)"""
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key or api_key.strip() == "" or api_key == "sua_chave_aqui":
        print("\n[ERRO DE CONFIGURACAO] Chave de API nao encontrada.")
        print("1. Crie um arquivo '.env' na pasta P0.")
        print("2. Adicione a linha: GEMINI_API_KEY=sua_chave_real_aqui")
        print("Consulte o arquivo .env.example para referencia.")
        sys.exit(1) # Encerra o programa de forma controlada

    if __name__ == "__main__":
         print("=" * 40)
         print("RESUMIDOR DE TEXTOS COM IA (Versao 2.0)")
         print("=" * 40)

         validar_configuracao()  
         arquivo_entrada = "texto.txt"

 # Verifica se o arquivo existe
    if not os.path.exists(arquivo_entrada):
        print(f"Erro: O arquivo '{arquivo_entrada}' nao foi encontrado.")
        print(f"Por favor, crie um arquivo chamado '{arquivo_entrada}' na pasta P0 e cole o texto nele.")
        sys.exit(1)
        
        # Abre e lê o arquivo
        with open(arquivo_entrada, "r", encoding="utf-8") as f:
            texto_completo = f.read()

        if not texto_completo.strip():
            print("O arquivo esta vazio. Insira um texto para resumir.")
            sys.exit(1)

            print(f"Lendo o arquivo '{arquivo_entrada}'...")
            print("Processando com o Gemini, aguarde...\n")
            
            # Instancia o serviço e chama o método
            service = LLMService()
            resultado = service.resumir_texto(texto_completo)
            
            print("-" * 40)
            print("RESUMO GERADO:")
            print("-" * 40)
            print(resultado)
            print("-" * 40)