# P1 — Nível Básico: Análise Inicial e Prompt Protótipo

**Projeto:** Sistemas Agentes / Trends-IA
**Etapa:** P1 — Nível Básico (compreensão do problema e análise inicial)
**Tag/release:** `p1-basico`

**Escopo:** projeto de análise e experimentação. Não inclui desenvolvimento de sistema completo, integração com sistemas acadêmicos, dados reais de estudantes, interface, banco de dados, implantação, treinamento/ajuste de modelos, automação real de decisões ou envio automático de mensagens. Todas as mensagens usadas são fictícias.

---

## 1. Contexto do caso

Cenário fictício: uma instituição de ensino quer avaliar o uso de IA em um sistema de apoio acadêmico que atende estudantes em dúvidas, cálculos e decisões administrativas. A proposta chegou como um bloco único ("usar IA para tudo"), e esta etapa tem como objetivo decompor a proposta em atividades menores e decidir, para cada uma, se a IA é adequada, se há alternativa mais simples e qual o risco envolvido.

A decisão central desta etapa: a escolha de usar IA depende da natureza e do risco de cada funcionalidade — não é um "aprovar/rejeitar" único para todo o sistema.

---

## 2. Decomposição da proposta em atividades menores

| # | Atividade                                         | Natureza predominante      |
|---|---------------------------------------------------|----------------------------|
| A | Interpretar mensagem livre e classificar a dúvida | Interpretação de linguagem |
| B | Redigir resposta personalizada a dúvida simples   | Geração de texto           |
| C | Calcular média ponderada e verificar situação     | Aplicação de regra         |
| D | Consultar informação em FAQ/calendário            | Consulta a informação      |
| E | Decidir elegibilidade a bolsa/auxílio             | Decisão de impacto         |
| F | Sugerir plano de estudos personalizado            | Combinação                 |
| G | Encaminhar caso sensível ao setor correto         | Decisão + interpretação    |

### 2.1 Funcionalidades escolhidas para análise profunda

| Funcionalidade                | Perfil exigido                   | Por que foi escolhida                                            |
|-------------------------------|----------------------------------|------------------------------------------------------------------|
| **A — Triagem/classificação** | Aparentemente adequada a LLM     | Há variação linguística e ambiguidade que regras tratam mal      |
| **C — Cálculo de média**      | Resolvível de forma mais simples | É regra determinística; LLM erra aritmética e não é auditável    |
| **E — Elegibilidade a bolsa** | Decisão de impacto relevante     | Afeta benefício financeiro; erro gera injustiça e risco jurídico |

**Justificativa:** A cobre o caso em que a IA agrega valor real; C cobre o caso em que a IA é a ferramenta errada; E cobre o caso em que o risco exige cautela máxima. Juntas, demonstram que a decisão sobre IA **depende da natureza e do risco** de cada funcionalidade.

---

## 3. Análise detalhada por funcionalidade (8 perguntas)

### 3.1 Funcionalidade A — Triagem/classificação de mensagens

| Pergunta                      | Resposta                                                                                                    |
|-------------------------------|-------------------------------------------------------------------------------------------------------------|
| **Entrada**                   | Texto livre do estudante.                                                                                   |
| **Resultado esperado**        | Categoria + urgência + setor + justificativa curta.                                                         |
| **LLM é adequado?**           | **Sim** — interpretação de linguagem com variação e ambiguidade.                                            |
| **Erros possíveis**           | Classificação errada; categoria inventada; sensibilidade ao prompt; ignorar caso sensível; setor alucinado. |
| **Impacto dos erros**         | **Moderado a alto** — atraso no atendimento; caso sensível mal classificado é grave.                       |
| **Alternativa mais simples?** | Classificador por palavras-chave + formulário estruturado (baixa cobertura).                               |
| **Revisão humana?**           | **Sim** — obrigatória para `saude`/`assedio`; amostragem nas demais.                                       |

### 3.2 Funcionalidade C — Cálculo de média e verificação de aprovação

| Pergunta                      | Resposta                                                                                         |
|-------------------------------|--------------------------------------------------------------------------------------------------|
| **Entrada**                   | Notas, pesos e regra do curso (média ≥ 6,0; frequência ≥ 75%).                                   |
| **Resultado esperado**        | Média calculada e situação (aprovado/recuperação/reprovado).                                     |
| **LLM é adequado?**           | **Não** — regra determinística; LLM erra aritmética e não é auditável.                            |
| **Erros possíveis**           | Erro de cálculo; confundir `≥` com `>`; inventar critério; arredondamento indevido.               |
| **Impacto dos erros**         | **Alto** — afeta diretamente a situação do estudante.                                            |
| **Alternativa mais simples?** | **Sim, e é a correta:** função determinística (fórmula/script).                                  |
| **Revisão humana?**           | Não para o cálculo; revisão apenas da *regra* cadastrada.                                        |

### 3.3 Funcionalidade E — Elegibilidade a bolsa/auxílio

| Pergunta                      | Resposta                                                                                               |
|-------------------------------|--------------------------------------------------------------------------------------------------------|
| **Entrada**                   | Dados do estudante + edital de critérios em linguagem natural.                                         |
| **Resultado esperado**        | Elegível / não elegível / pendente, com justificativa auditável.                                       |
| **LLM é adequado?**           | **Parcialmente** — extração do edital e explicação; decisão final deve ser regra.                      |
| **Erros possíveis**           | Interpretar mal o edital; ignorar exceções; alucinar critério; viés; decisão não reproduzível.         |
| **Impacto dos erros**         | **Muito alto** — afeta benefício financeiro; gera injustiça e risco jurídico.                          |
| **Alternativa mais simples?** | Motor de regras a partir do edital estruturado.                                                        |
| **Revisão humana?**           | **Sim, obrigatória** — decisão final por comissão.                                                     |

---

## 4. Prompt protótipo (Funcionalidade A — triagem)

**Contexto:**
Você é assistente de triagem de uma secretaria acadêmica fictícia. Receberá mensagens de estudantes e deve classificá-las para encaminhamento ao setor correto.

**Tarefa:**
Classificar a mensagem em uma das categorias: `prazo_entrega`, `nota`, `matricula`, `bolsa`, `saude`, `assedio`, `outro`. Indicar urgência (`alta`/`media`/`baixa`), setor responsável e justificativa curta.

**Instruções:**
- Baseie-se apenas no texto fornecido; não invente informações.
- Se houver menção a saúde, sofrimento ou assédio, classifique como `saude`/`assedio` e urgência `alta`, independentemente do resto.
- Se ambíguo, use `outro` e urgência `media`.
- Responda **somente** em JSON, sem texto adicional.

**Formato esperado:**

```json
{"categoria": "...", "urgencia": "...", "setor": "...", "justificativa": "..."}
```

---

## 5. Execução com 3 exemplos fictícios

> Execução em interface de IA, com o prompt da seção 4. Mensagens **fictícias**.

### 5.1 Resumo dos resultados

| Exemplo | Tipo     | Categoria obtida | Urgência | Setor                  |
|---------|----------|------------------|----------|------------------------|
| 1       | Simples  | `prazo_entrega`  | `media`  | `secretaria_academica` |
| 2       | Sensível | `saude`          | `alta`   | `apoio_estudantil`     |
| 3       | Ambíguo  | `outro`          | `baixa`  | `secretaria_academica` |

### 5.2 Saídas completas

**Exemplo 1 — simples**

Mensagem: "Boa tarde, perdi o prazo do trabalho de história por causa de uma gripe. Posso entregar amanhã?"

```json
{"categoria": "prazo_entrega", "urgencia": "media", "setor": "secretaria_academica", "justificativa": "Pedido de prorrogação de prazo por motivo de saúde leve, sem menção a sofrimento grave."}
```

**Exemplo 2 — sensível**

Mensagem: "Não estou aguentando mais, tenho crises de ansiedade antes das provas e não sei a quem recorrer."

```json
{"categoria": "saude", "urgencia": "alta", "setor": "apoio_estudantil", "justificativa": "Menção explícita a sofrimento psíquico; acionar apoio estudantil com prioridade."}
```

**Exemplo 3 — ambíguo**

Mensagem: "Qual o horário da secretaria na sexta?"

```json
{"categoria": "outro", "urgencia": "baixa", "setor": "secretaria_academica", "justificativa": "Dúvida informacional simples; não se encaixa nas categorias específicas."}
```

### 5.3 Observações de execução (evidência de C05)

| Fenômeno                    | O que foi observado                                               | Evidência                  |
|-----------------------------|-------------------------------------------------------------------|----------------------------|
| **Variação**                | Categoria do Exemplo 2 mudou ao remover a instrução de priorização | `saude` → `prazo_entrega` |
| **Incerteza**               | Urgência do Exemplo 2 oscilou entre execuções                     | `alta` ↔ `media`           |
| **Alucinação**              | Modelo sugeriu setor inexistente sem a instrução "não invente"    | `setor_coordenacao_geral`  |
| **Sensibilidade ao prompt** | Exemplo 1 mudou de categoria ao enfraquecer a instrução de saúde   | `prazo_entrega` ↔ `saude`  |

**Conclusão:** o LLM é útil para triagem, mas variação, incerteza e sensibilidade ao prompt confirmam a necessidade de revisão humana em casos sensíveis e de instruções explícitas e testadas.



