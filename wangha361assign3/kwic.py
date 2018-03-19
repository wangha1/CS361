class Kwic:
	def __init__(self, ignoreWords=[], periodsToBreaks=False):
		self.Text = ""
		self.periodsToBreaks = periodsToBreaks
		self.ignoreWords = ignoreWords
	
	def reset(self):
		self.Text = ""
	
	def addText(self, Text):
		self.Text += Text

	def index(self):
		lines = self.splitBreaks(self.Text, self.periodsToBreaks)
		splitLines = map(lambda l: l.split(), lines)
		shiftedLines = [map(lambda x:(x,i), self.shift(splitLines[i])) for i in xrange(0,len(splitLines))]
		flattenedLines = [l for subList in shiftedLines for l in subList]
		filteredLines = filter(lambda l: not self.ignorable(l[0][0], self.ignoreWords), flattenedLines)
		return sorted(filteredLines, key = lambda l: (map(cleanWord, l[0]),l[1]))

	def listPairs(self):
		lines = self.splitBreaks(self.Text, self.periodsToBreaks)
		splitLines = map(lambda l: l.split(), lines)
		pairs = {}
		for l in splitLines:
			seen = set([])
			for wu1 in l:
				wc1 = cleanWord(wu1)
				if(len(wc1) == 0):
					continue
				for wu2 in l:
					wc2 = cleanWord(wu2)
					if wc1 < wc2:
						if (wc1,wc2) in seen:
							continue
						seen.add((wc1,wc2))
						if (wc1,wc2) in pairs:
							pairs[(wc1,wc2)] += 1
						else:
							pairs[(wc1,wc2)] = 1
		return map(lambda wp: (wp, pairs[wp]), sorted(filter(lambda wp: pairs[wp] > 1, pairs.keys())))


	def shift(self,line):
		return [line[i:] + line[:i] for i in xrange(0,len(line))]


	def ignorable(self,word,ignoreWords):
		return cleanWord(word) in map(lambda w: w.lower(), ignoreWords)
	
	def splitBreaks(self,string, periodsToBreaks):
		if not periodsToBreaks:
			return string.split("\n")
		else:
			line = ""
			lines = []
			lastChar1 = None
			lastChar2 = None
			breakChars = map(chr, xrange(ord('a'),ord('z')+1))
			for c in string:
				if (c == " ") and (lastChar1 == ".") and (lastChar2 in breakChars):
					lines.append(line)
					line = ""
				line += c
				lastChar2 = lastChar1
				lastChar1 = c
			lines.append(line)
			return lines

def cleanWord(word):
	return filter (lambda c: c not in [".",",","?","!",":"], word.lower())
