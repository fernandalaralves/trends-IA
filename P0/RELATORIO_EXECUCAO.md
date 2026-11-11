# Relatório de Execução - P0

## Evolução por Nível
*   **Nível Básico:** Criação do script inicial em Python (`main.py`), configuração da chave de API no `.env` e integração direta com a API do Gemini para resumir um texto inserido via terminal.
*   **Nível Intermediário:** Refatoração para separar responsabilidades (`main.py` e `llm_service.py`), leitura de arquivo `texto.txt`, e implementação de tratamento de erros amigável para falhas de API e validação da chave.
*   **Nível Avançado:** Desacoplamento das configurações (`config.py`), implementação de logs seguros (`logging`), criação de testes unitários simulados (`test_main.py`) sem chamar a API real, e documentação final para reprodutibilidade.

## Decisões Principais
1.  **Decisão:** Escolha do modelo `gemini-3.8-flash`.
    *   **Alternativa:** `gemini-2.5-flash`.
    *   **Justificativa:** O modelo 2.5 apresentou erro de indisponibilidade para novas contas (404), então o 3.8 foi adotado por ser a versão recomendada e mais estável no momento.
2.  **Decisão:** Uso de `unittest` e `mocks` para testes.
    *   **Alternativa:** Testes reais consumindo a API.
    *   **Justificativa:** Testes com mocks garantem que a lógica de tratamento de erros e respostas seja validada sem gastar a cota gratuita da API.

## Testes e Resultados
| Teste | Entrada ou situação | Resultado esperado | Resultado obtido |
| :--- | :--- | :--- | :--- |
| Sucesso | Texto válido no `texto.txt` e chave correta | Retorno de um resumo em 3 tópicos | Resumo gerado com sucesso. |
| Credencial Ausente | `.env` renomeado ou vazio | Mensagem amigável de erro de configuração | O programa encerra avisando sobre a chave ausente. |
| Credencial Inválida | Chave falsa no `.env` | Mensagem de erro de credencial inválida | Retorno "[ERRO DE CREDENCIAL] A chave de API e invalida..." |
| Resposta Simulada (Mock) | Execução do `test_main.py` | Validação lógica sem chamar a API | 2 testes executados com sucesso (OK). |

## Falhas e Limitações
*   **O que aconteceu:** Durante o desenvolvimento, o disco local (C:) encheu, impedindo a criação do ambiente virtual (`venv`) e a instalação das dependências.
*   **Como foi identificado:** O terminal retornou o erro `[Errno 28] Espaço insuficiente no disco`.
*   **Como foi tratado:** O ambiente virtual foi recriado usando a flag `--without-pip`, o `pip` foi instalado manualmente via script, e a validação em ambiente limpo foi concluída com sucesso.
*   **Por que permanece:** A limitação de espaço em disco é um problema de hardware local, não do código em si. O projeto em si já está documentado e pronto para rodar em qualquer máquina com espaço suficiente.

## Uso de IA no Desenvolvimento
*   **Ferramenta utilizada:** DeepSeek (Chat).
*   **Tarefa delegada:** Auxílio na criação de testes com mocks e resolução de erros de ambiente (venv, pip, disco cheio).
*   **Resultado aproveitado:** Sugestões de refatoração (separação do `llm_service.py`) e código base para os testes unitários.


## Reflexão Final
*   **Principal aprendizado:** Compreender o ciclo completo de desenvolvimento com IA, desde a configuração do ambiente e integração de API até o tratamento de erros de produção e documentação para terceiros.
*   **Competência mais desenvolvida:** C03 (Tratamento de respostas e falhas sem expor informações sensíveis), devido à implementação do logging e validação de credenciais.
*   **Aspecto a aprimorar:** A gestão de ambientes locais e resolução de conflitos de infraestrutura (como falta de espaço em disco e caminhos com caracteres especiais).

## Vídeo de Demonstração
[Demonstração do projeto](meu_link_em_algum_momento)
