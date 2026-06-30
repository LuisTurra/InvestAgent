import json
from groq import Groq
from config import GROQ_API_KEY, MODEL_NAME
from llm.prompts import SYSTEM_PROMPT


client = Groq(api_key=GROQ_API_KEY)

STRICT_PROMPT = """
Você é um analista quantitativo de investimentos.

Você NÃO faz cálculos.
Você NÃO inventa dados.
Você APENAS interpreta os dados fornecidos.

REGRAS OBRIGATÓRIAS:

1. O risk_score define o risco:
   - 0 a 33  = BAIXO
   - 34 a 66 = MÉDIO
   - 67 a 100 = ALTO

2. Você NÃO pode alterar o risco.

3. Você deve responder em português do Brasil.

4. Você deve basear sua análise nos seguintes campos:
   - regime
   - technical_score
   - trend_score
   - momentum_score
   - risk_score
   - indicadores (RSI, MACD, EMA, volatilidade)

5. Sua justificativa deve citar os principais sinais (ex: MACD negativo, preço abaixo da EMA20, momentum fraco).

FORMATO DE SAÍDA (JSON obrigatório):

{
  "recommendation": "BUY | HOLD | SELL",
  "risk": "BAIXO | MÉDIO | ALTO",
  "confidence": 0-100,
  "reasoning": "explicação curta em pt-BR citando os principais sinais técnicos"
}
"""


def analyze(summary):

    response = client.chat.completions.create(
        model=MODEL_NAME,
        temperature=0.1,
        response_format={"type": "json_object"},

        messages=[
            {
                "role": "system",
                "content": STRICT_PROMPT
            },
            {
                "role": "user",
                "content": json.dumps(summary)
            }
        ]
    )

    return json.loads(response.choices[0].message.content)