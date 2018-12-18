import os
import librosa

def run(audio):
        y, sr = librosa.load(audio)
	librosa.output.write_wav('prueba.wav', y, sr)
        os.system("sox prueba.wav -r 16000 -c 1 -b 16 result.wav")
	os.system("deepspeech output_graph.pb quz_alphabet.txt result.wav >> result.txt")
	archivo = open("result.txt", "r") 
	contenido = archivo.read()
	os.system("rm result.txt")
	return contenido
