from pathlib import Path
import whisper
from gtts import gTTS

# CONFIGURAÇÕES

LANGUAGE = "pt"
AUDIO_INPUT = Path("audio/input.wav")
AUDIO_OUTPUT = Path("audio/response.mp3")

# 1. SPEECH TO TEXT
def speech_to_text(audio_file):
    print('Carregando modelo Whisper...')
    model = whisper.load_model('small')

    print('Transcrevendo áudio...')
    result = model.transcribe(
        str(audio_file),
        language=LANGUAGE,
        fp16=False
    )

    texto = result["text"]
    print('\nTEXTO TRANSCRITO:')
    print(texto)
    return texto

# 2. CHATGPT (SIMULADO)

def get_chatgpt_response(texto):
    print('\n Gerando resposta (simulada)...')

    resposta = (
        'Python é uma linguagem de programação de alto nível, '
        'interpretada, com sintaxe simples e fácil leitura. '
        'Ela é muito utilizada em desenvolvimento web, '
        'ciência de dados, inteligência artificial e automação.'
    )

    print("\nRESPOSTA DO CHATGPT:")
    print(resposta)
    return resposta

# 3. TEXT TO SPEECH

def text_to_speech(texto):
    print('\nConvertendo texto em áudio...')

    AUDIO_OUTPUT.parent.mkdir(exist_ok=True)

    tts = gTTS(text=texto, lang=LANGUAGE, slow=False)
    tts.save(AUDIO_OUTPUT)

    print(f'Áudio salvo em: {AUDIO_OUTPUT.resolve()}')

# PIPELINE COMPLETO
def main():
    if not AUDIO_INPUT.exists():
        print('Arquivo de áudio não encontrado.')
        return

    texto = speech_to_text(AUDIO_INPUT)
    resposta = get_chatgpt_response(texto)
    text_to_speech(resposta)

    print('\nProcesso finalizado com sucesso!')


if __name__ == '__main__':
    main()
