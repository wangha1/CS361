def kwic(str1, *arguments, **keywords):
	ignoreWords = [];
	listPairs = False;	
	keys = sorted(keywords.keys());
	for kw in keys:
		if(kw == "ignoreWords"):
			ignoreWords = keywords[kw];
		elif(kw == "listPairs"):
			listPairs = keywords[kw];
		elif(kw == "periodsToBreaks"):
			if(keywords[kw] == True):
				str1 = PTB(str1);
		else:
			print "Invalid argument.";
			return 1;
	list1 = str1.split("\n");
	if(str1 == ""):
		if(listPairs):
			return ([],[]);
		return [];
	if(listPairs == True):
		listP = [];
		for item in list1:
			listP.append(stripPunc(item));
		Pairs = LP(listP);
	list2 = [];
	for i in range(len(list1)):
		line = [];
		line.append(list1[i]);
		words = [];
		words = line[0].split();
		for x in range(len(words)):
			temp = [];
			temp = shift(words,x - 1);
			flag = 0;
			for y in range(len(ignoreWords)):
				if(temp[0] == ignoreWords[y].lower()):
					flag = 1;
					break;
			if(flag == 0): 
				list2.append((temp,i));
	list2.sort(key = lambda s :" ".join(s[0]).lower());
	if(listPairs == True):
		result = (list2,Pairs);
		return result
	return list2;

def shift(l,i):
	return l[i:] + l[:i]

def PTB(oldStr):
	line = ""
	lines = []
	lastChar1 = None
	lastChar2 = None
	breakChars = map(chr, xrange(ord('a'),ord('z')+1))
	for c in oldStr:
		if (c == " ") and (lastChar1 == ".") and (lastChar2 in breakChars):
			lines.append(line)
			line = ""
		line += c
		lastChar2 = lastChar1
		lastChar1 = c
	lines.append(line)
	return lines

def LP(lineLi):
	lineList = lineLi;
	words = [];
	pair = [];
	list_of_pairs = [];
	for i in range(len(lineList)):
		words.append(list(set(lineList[i].split())));
	for i in range(len(words)):
		list_of_pairs = list_of_pairs + [[words[i][p1], words[i][p2]] for p1 in range(len(words[i])) for p2 in range(p1+1,len(words[i]))];
	for i in range(len(list_of_pairs)):
		list_of_pairs[i].sort();
	for i in range(len(list_of_pairs)):
		per = i * 100 / len(words)
		newper = ((i+1)*100)/len(words)
		if((newper-per) != 0):
			print str(newper) + "% on list pairs"
		count = list_of_pairs.count(list_of_pairs[i]);
		if(count >= 2):
			temp = (tuple(list_of_pairs[i]),count);
			pair.append(temp);	
	pair = list(set(pair));
	pair = sorted(pair);
	return pair;
	
				

def stripPunc(wordList):
    return filter (lambda c: c not in [".",",","?","!",":"], word.lower())

