from pytube import YouTube
import unicodedata
import os

PATH = "/"

def make_shell_string(str):
	str = str.replace(" ", "\\ ")
	str = str.replace("(", "\\(")
	str = str.replace(")", "\\)")
	str = str.replace("\"", "\\\"")
	str = str.replace("\'", "\\\'")
	str = str.replace(",", "")
	str = str.replace("/", "")
	return str

class Stripper():
	def __init__(self, name):
		path = "/music/" + name + ".wav"
		video = PATH+"video.mp4"
		cmd = "ffmpeg -i " + video + " -ab 160k -ac 2 -ar 44100 -vn " + path
		os.popen(cmd)
		os.remove(video)

class Charon(YouTube):
	def __init__(self, url):
		YouTube.__init__(self, url)
		self.name = unicodedata.normalize("NFKD", self.title).encode('ascii', 'ignore').replace(" ", "_")
		self.name = make_shell_string(self.name)

	def download(self):
		self.streams.filter(subtype="mp4").first().download(PATH, filename="video")
		Stripper(self.name)


if __name__ == '__main__':
	import sys
	Charon(sys.argv[1]).download()
