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
                ),
                 # request_options define o tempo máximo de espera (em milissegundos)
                request_options={"timeout": 30000} 
            )
            
            # Verifica se a resposta veio vazia (Tratamento de resposta inesperada)
            if not response.text:
                return "[ERRO DE RESPOSTA] O modelo nao retornou nenhum texto. Tente novamente."
            
            return response.text
            
        except errors.APIError as e:
            # Tratamento de erro específico para a API (C03)
            if e.code == 400:
                return "[ERRO DE CREDENCIAL] A chave de API e invalida ou expirou. Gere uma nova chave no Google AI Studio."
            elif e.code in [429, 503]:
                return "[ERRO DE DISPONIBILIDADE] O servico do Gemini esta sobrecarregado ou indisponivel. Tente novamente mais tarde."
            elif e.code == 404:
                return "[ERRO DE MODELO] O modelo selecionado nao foi encontrado."
            else:
                return f"[ERRO DA API] Falha na comunicacao com o Gemini (Codigo {e.code})."
                
        except Exception as e:
            # Tratamento de erro genérico (ex: falta de internet)
            return f"Ocorreu um erro inesperado. Verifique sua conexao com a internet.\nDetalhes: {e}"