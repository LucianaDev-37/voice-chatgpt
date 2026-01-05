import whisper
from pathlib import Path

# Caminho do projeto
BASE_DIR = Path(__file__).resolve().parent.parent

# áudio gravado
audio_file = BASE_DIR / 'audio' / 'input.wav'

print('Carregando Whisper...')

# modelo
model = whisper.load_model('small')

print(' Transcrevendo áudio...')

# Transcrição
result = model.transcribe(
    str(audio_file),
    language='pt',
    fp16=False
)

transcription = result['text']

print('\nTEXTO TRANSCRITO:')
print(transcription)
