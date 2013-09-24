import sys
from webSurf import lookupYoutube
myfile = "/Users/Aaron/Desktop/Developer/Data/tmp/youtubelink.txt"
f = open(myfile, 'w')
print(len(sys.argv))
line = ""
if(sys.argv[len(sys.argv) - 1] == "-auto"):
	for i in range(1, len(sys.argv) - 1):
		line+=sys.argv[i] + " "
	link = lookupYoutube(line, False)
else:
	for i in range(1, len(sys.argv)):
		line+=sys.argv[i] + " "
	link = lookupYoutube(line)

f.write(link)
