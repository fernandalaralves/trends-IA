import unittest
from unittest.mock import patch, MagicMock
from llm_service import LLMService  

class TestLLMService(unittest.TestCase):

    @patch('llm_service.genai.Client') #simula cleinte do google
    def test_resumir_texto_sucesso(self, mock_client):
        mock_instance = mock_client.return_value
        mock_response = MagicMock()
        mock_response.text = "* Topico 1\n* Topico 2\n* Topico 3"
        mock_instance.models.generate_content.return_value = mock_response

        service = LLMService()
        resultado = service.resumir_texto("Texto de teste")
        
        self.assertIn("Topico 1", resultado)
        self.assertNotIn("ERRO", resultado)

    @patch('llm_service.genai.Client')
    def test_resposta_vazia_simulada(self, mock_client):
        # Simula o LLM retornando vazio
        mock_instance = mock_client.return_value
        mock_response = MagicMock()
        mock_response.text = None
        mock_instance.models.generate_content.return_value = mock_response

        service = LLMService()
        resultado = service.resumir_texto("Texto de teste")
        
        self.assertIn("[ERRO DE RESPOSTA]", resultado)

if __name__ == '__main__':
    unittest.main()