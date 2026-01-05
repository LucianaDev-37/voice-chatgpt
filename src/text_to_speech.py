from gtts import gTTS
from pathlib import Path

# Texto que será convertido em áudio
texto = (
    'Python é uma linguagem de programação de alto nível, '
    'interpretada, com sintaxe simples e fácil leitura. '
    'Ela é muito utilizada em desenvolvimento web, '
    'ciência de dados, inteligência artificial e automação.'
)

# Garante que a pasta audio exista
audio_dir = Path('audio')
audio_dir.mkdir(exist_ok=True)

# arquivo de saída
output_file = audio_dir / 'response.mp3'

# áudio com gTTS
tts = gTTS(text=texto, lang='pt', slow=False)
tts.save(output_file)

print(f'Áudio gerado com sucesso em: {output_file.resolve()}')
