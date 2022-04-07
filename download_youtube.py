# https://www.youtube.com/watch?v=L0dWYMVL8Lo&list=RDL0dWYMVL8Lo
import os
from pytube import Playlist, YouTube

url = str(input("Digite url: "))
# url = "https://youtube.com/playlist?list=PLr7XrCpy6FEal3BU0Txsfrw9q_uPTNv15"
playlist = Playlist(url)
print("O número de vídeos dessa playlist é: ", len(playlist.video_urls))
for video_url in playlist.video_urls:
    print(video_url)
    yt = YouTube(video_url)
    try:
        print("Baixando...")
        video = yt.streams.filter(only_audio=True).first()
        arquivo = video.download()

        base, ext = os.path.splitext(arquivo)
        novo_arquivo = base + ".mp3"
        os.rename(arquivo, novo_arquivo)
        print("Baixado com Sucesso")
    except:
        print("Problemas ao fazer dowload!")
