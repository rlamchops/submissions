import urllib2
import sys
def compareTitles(possibleTitles, titles, string):
	numWords = 0
	words = string.rsplit(" ")
	for word in words:
		numWords = numWords + 1
	#Allows us to see how many words are in the title
	currVid = 0
	for vid in titles:
		numWordsRight = 0
		for word in words:
			#Uppercase comparisons to make uncase sensitive
			vid = vid.upper()
                        word = word.upper()
			#Look for search word in video title
                        if(vid.find(word) != -1):
                                numWordsRight = numWordsRight + 1
		#See if the song were looking for is a remix
          	if(string.find("remix") == -1):
			#If it isnt, make sure that the video isnt a remix either
			if(vid.find("remix") != -1):
				print("Poop")
				numWordsRight = numWordsRight - 3 
		if(numWordsRight == numWords):
			#All of the search words are in the video title
			return currVid	
		#If you dont break immeadiatly, save your options so you can later choose the best one
		possibleTitles.append(numWordsRight)
		currVid = currVid + 1
	#If no option is perfect, find the best option
	max = 0
	maxIndex = 0
	index = 0
	for i in possibleTitles:
		if(i > max):
			maxIndex = index
			max = i
		index = index + 1
	#Give a warning on bad performance
	if( max < numWords * 3 / 4):
		print("This title was hard to find and might be downloading the wrong song")
		print("Check your spelling")
		print("I'm downloading anyways")
	return maxIndex
def lookupYoutube(string, pick = True):
	words = string.rsplit(" ")
	link = "http://www.youtube.com/results?client=safari&rls=en&q="
	for each in words:
		link += each + "+"
	link = link.rstrip('+')
	link += "&oe=UTF-8&um=1&ie=UTF-8&sa=N&tab=w1"
	page = urllib2.urlopen(link)
	data = page.read()
	currLine = ""
	inTag = False
	inVideo = False
	vidLink = ""
	num = 1
	links = []
	titles = []
	for line in data:
		if(line == "<"):
			inTag = True
		if(inTag):
			currLine += line
		if(inVideo):
			vidLink += line
		if(line == ">"):
			if(inVideo):			
				watch = "youtube.com"+vidLink[vidLink.find('/watch'):]
				watch = watch.rstrip('">')
                        	title = vidLink[vidLink.find("title=") + 7:vidLink.find("data-sessionlink") - 2]       
                                links.append(watch)
				titles.append(title)
				inVideo = False
                                vidLink = ""
				num += 1
			if(currLine.find('h3 class="yt-lockup2-title"') != -1):
				inVideo = True
			currLine = ""
			inTag = False
	input = 2
	if(pick):
		num = 0
		for title in titles:
			num = num + 1
			print(str(num) + " " + title)
		#Give a nice out if they are picking
		while(True):
			input = raw_input("Pick a video: ")
			try:
				input = int(input)
				if(input <= num):
					input = input - 1
					break
			except:
				pass
			#Empty except statement
	else:
		possibleVideos = []
		bestVid = compareTitles(possibleVideos, titles, string)
		print("Downloading Video: "+titles[bestVid])
		input = bestVid
	return links[input]	

def definition(word):
		inTag = False
		search = "http://dictionary.reference.com/browse/" + word +"?s=t"
		page = urllib2.urlopen(search)
	        data = page.read()
		string = ""
		for line in data:
			if(line == "<"):
				inTag = True
			if(line == ">"):
				#print(string)
				inTag = False
				if(string.startswith("<meta")):
					#print(string)
                                	if(string.find('name="description') != -1):	
						str = string.split(",", 1)
						str[1] = str[1].upper()
						str[1] = str[1].lstrip(" ")
						if(str[1].startswith("A FREE ONLINE DICTIONARY WITH")):
							#Not a word
							print("Not a word :(")
							return -1
						if(str[1].find('SEE MORE."/') != -1):
							split = str[1].find('"SEE MORE."/', 1) - 11
							str[1] = str[1][0:split]
							str[1] = str[1].lower()
							print(str[1])
						return str[1];
				string = ""
			if(inTag):
				string += line

