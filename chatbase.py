import os  # Importe o módulo os para manipular variáveis de ambiente
from google.cloud import texttospeech
import pygame
from tempfile import TemporaryFile

# Definir a variável de ambiente para apontar para o arquivo de credenciais
credentials_file = "/home/jgnunes/Projetos/credencial.json"
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = credentials_file

def falar(texto):
    client = texttospeech.TextToSpeechClient()
    voz = texttospeech.VoiceSelectionParams(
        language_code="pt-BR", ssml_gender=texttospeech.SsmlVoiceGender.FEMALE
    )
    audio_config = texttospeech.AudioConfig(
        audio_encoding=texttospeech.AudioEncoding.MP3
    )
    resposta = client.synthesize_speech(
        input=texttospeech.SynthesisInput(text=texto), voice=voz, audio_config=audio_config
    )

    # Reproduzir o áudio gerado
    with TemporaryFile() as temp_file:
        temp_file.write(resposta.audio_content)
        temp_file.seek(0)

        pygame.mixer.init()
        pygame.mixer.music.load(temp_file)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)

# Lógica do Chat
while True:
    mensagem = input("Você: ")
    # Lógica de conversação para gerar a resposta
    resposta = "Resposta do bot"
    falar(resposta)
