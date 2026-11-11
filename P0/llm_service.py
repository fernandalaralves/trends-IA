import logging
from google import genai
from google.genai import errors
import config

# Configuração de log (nível INFO mostra o que está acontecendo)
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class LLMService:
    def __init__(self):
        self.client = genai.Client()

    def resumir_texto(self, texto_original):
        try:
            response = self.client.models.generate_content(
                model=config.MODEL_NAME,
                contents=texto_original,
                config=genai.types.GenerateContentConfig(
                    system_instruction="Voce e um assistente especialista em resumir textos. Resuma o texto fornecido pelo usuario em exatamente 3 topicos com marcadores (bullet points). Seja direto e objetivo.",
                    temperature=config.TEMPERATURE,
                ),
                 # request_options define o tempo máximo de espera (em milissegundos)
                request_options={"timeout": config.TIMEOUT_MS} 
            )
            
            # Verifica se a resposta veio vazia (Tratamento de resposta inesperada)
            if not response.text:
                logger.warning("O modelo retornou uma resposta vazia.")
                return "[ERRO DE RESPOSTA] O modelo nao retornou nenhum texto. Tente novamente."

                logger.info("Chamada concluida com sucesso.")
            return response.text
            
        except errors.APIError as e:
            logger.error("Erro na API do Gemini. Codigo: %s", e.code) # Não logamos a mensagem inteira para não vazar dados
            if e.code == 400:
                return "[ERRO DE CREDENCIAL] A chave de API e invalida ou expirou. Gere uma nova chave no Google AI Studio."
            elif e.code in [429, 503]:
                return "[ERRO DE DISPONIBILIDADE] O servico do Gemini esta sobrecarregado ou indisponivel. Tente novamente mais tarde."
            elif e.code == 404:
                return "[ERRO DE MODELO] O modelo selecionado nao foi encontrado."
            else:
                return f"[ERRO DA API] Falha na comunicacao com o Gemini (Codigo {e.code})."
                
        except Exception as e:
            logger.error("Falha de comunicacao ou timeout: %s", type(e).__name__)
            return f"Ocorreu um erro inesperado. Verifique sua conexao com a internet.\nDetalhes: {e}"