from pytube import YouTube
import moviepy.editor as mp

import re
import os


print("============= Conversor de Video em Audio Mp3 =============")
#Link e diretorio arquivo
link = input("Digite o link do video que deseja baixar: ") #O  link do video
path = input("Digite o Diretório que deseja salvar o video : ") #Local onde o video será salvo
yt = YouTube(link)

#Download iniciado
print("Baixando ... ")
ys = yt.streams.filter(only_audio=True).first().download(path)
print("Download foi completado!")

#Converter mp4 para mp3
print("Convertendo Arquivo ...")
for file in os.listdir(path):
    if re.search('mp4', file):
        mp4_path = os.path.join(path, file)
        mp3_path = os.path.join(path, os.path.splitext(file)[0]+'.mp3')
        new_file = mp.AudioFileClip(mp4_path)
        new_file.write_audiofile(mp3_path)
        os.remove(mp4_path)
print("Sucesso")