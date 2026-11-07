import os
from google import genai
from google.genai import errors

class LLMService:
    def __init__(self):
        self.client = genai.Client()

    def resumir_texto(self, texto_original):
        """Envia o texto para o Gemini e retorna o resumo ou uma mensagem de erro amigável."""
        try:
            response = self.client.models.generate_content(
                model='gemini-3.8-flash',
                contents=texto_original,
                config=genai.types.GenerateContentConfig(
                    system_instruction="Voce e um assistente especialista em resumir textos. Resuma o texto fornecido pelo usuario em exatamente 3 topicos com marcadores (bullet points). Seja direto e objetivo.",
                    temperature=0.5,
                )
            )
            return response.text
            
        except errors.APIError as e:
            # Tratamento de erro específico para a API (C03)
            if e.code == 400:
                return "Erro de API: Verifique se a sua chave no arquivo .env esta correta e ativa."
            elif e.code == 404:
                return "Erro de API: O modelo selecionado nao foi encontrado. Verifique o nome do modelo."
            else:
                return f"Erro na API do Gemini (Codigo {e.code}): {e.message}"
                
        except Exception as e:
            # Tratamento de erro genérico (ex: falta de internet)
            return f"Ocorreu um erro inesperado. Verifique sua conexao com a internet.\nDetalhes: {e}"