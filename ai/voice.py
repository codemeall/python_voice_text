from gtts import gTTS
import pyglet
pyglet.lib.load_library('avbin')
pyglet.have_avbin=True
import time,os

def tts(text, lang):
	file = gTTS (text = text, lang = lang)
	filename = '/tmp/temp.mp3'
	file.save(filename)

	music = pyglet.media.load(filename, streaming = False)
	music.play()

	time.sleep(music.duration)
	# os.remove(filename)
	 

tts('Nothing', 'en')


#Installed AvBin with the below link help and incliuded the avbin below the piglet
#https://stackoverflow.com/questions/10302873/python-pyglet-avbin-how-to-install-avbin