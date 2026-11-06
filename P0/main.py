import os
from dotenv import load_dotenv
from google import genai

# 1. Carrega as variáveis do arquivo .env
load_dotenv()

# 2. Pega a chave da API
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("Erro: A chave GEMINI_API_KEY nao foi encontrada no arquivo .env")
    exit()

# 3. Inicializa o cliente do Google GenAI
client = genai.Client(api_key=api_key)

def resumir_texto(texto_original):
    """Envia o texto para o Gemini e retorna o resumo."""
    try:
        # Faz a chamada para o modelo
        response = client.models.generate_content(
            model='gemini-3.8-flash',
            contents=texto_original,
            config=genai.types.GenerateContentConfig(
                system_instruction="Voce e um assistente especialista em resumir textos. Resuma o texto fornecido pelo usuario em exatamente 3 topicos com marcadores (bullet points). Seja direto e objetivo.",
                temperature=0.5,
            )
        )
        return response.text
    except Exception as e:
        return f"Ocorreu um erro ao chamar a API: {e}"

if __name__ == "__main__":
    print("=" * 40)
    print("RESUMIDOR DE TEXTOS COM IA (Gemini)")
    print("=" * 40)
    print("Cole o texto que voce quer resumir e pressione ENTER duas vezes para finalizar:\n")

    # Coleta o texto do usuário (multilinha)
    linhas = []
    while True:
        linha = input()
        if linha == "":
            break
        linhas.append(linha)
    
    texto_completo = "\n".join(linhas)

    if not texto_completo.strip():
        print("Nenhum texto foi inserido. Encerrando.")
    else:
        print("\nProcessando com o Gemini, aguarde...\n")
        resultado = resumir_texto(texto_completo)
        
        print("-" * 40)
        print("RESUMO GERADO:")
        print("-" * 40)
        print(resultado)
        print("-" * 40)