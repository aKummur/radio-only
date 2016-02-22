from scipy.io import wavfile

rate, a = wavfile.read("test.wav")
f = open('log', 'w')
print rate
for i in a:
	f.write('%-4s, %s\n'%(i[0], i[1]))
f.close()