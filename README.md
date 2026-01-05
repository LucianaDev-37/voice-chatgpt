# 🎙️ Voice-ChatGPT

Assistente de voz desenvolvido em Python que realiza um pipeline completo de:
**voz → texto → resposta → voz**, utilizando Whisper, ChatGPT (simulado) e gTTS.

---

## 🚀 Funcionalidades

- 🎤 Grava áudio pelo microfone
- 📝 Transcreve voz em texto com Whisper
- 🤖 Gera resposta no estilo ChatGPT
- 🔊 Converte a resposta em áudio (Text-to-Speech)

---

## 🛠️ Tecnologias Utilizadas

- Python
- Whisper (Speech-to-Text)
- gTTS (Text-to-Speech)
- Git & GitHub
- Virtual Environment (venv)

---

## ▶️ Como Executar

```bash
python src/main.py

## 📌 Observações

- A integração com a API da OpenAI está preparada no código, mas foi simulada
  neste projeto para evitar custos e problemas de quota.
- O projeto pode ser facilmente adaptado para uso com uma chave real via `.env`.

