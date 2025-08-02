from pydub import AudioSegment
from random import randint
count = 0
audioOut = AudioSegment.silent(duration=0)
while count < 50:
	# 10 is a special number here. It doesn't have a soundbite, so it's used
	# as a line break to split up different sections of audio
	number = randint(0,10)
	if number != 10:
		clip = AudioSegment.from_mp3(f'./samples/{number}.mp3')
		audioOut = audioOut + clip + AudioSegment.silent(duration=500)
	if number == 10:
		audioOut = audioOut + AudioSegment.silent(duration=1250)
	count += 1
audioOut.export("output.mp3", format="mp3")