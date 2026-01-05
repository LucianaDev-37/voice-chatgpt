import sounddevice as sd
from scipy.io.wavfile import write
from pathlib import Path

# Caminho
BASE_DIR = Path(__file__).resolve().parent.parent

# Pasta de áudio
AUDIO_DIR = BASE_DIR / 'audio'
AUDIO_DIR.mkdir(exist_ok=True)

# arquivo de saída
file_path = AUDIO_DIR / 'input.wav'

# Configurações de gravação
fs = 44100
seconds = 6

print('Gravando...')

audio = sd.rec(
    int(seconds * fs),
    samplerate=fs,
    channels=1
)
sd.wait()

write(file_path, fs, audio)

print('Áudio gravado com sucesso!')
print(f'Arquivo salvo em: {file_path}')

