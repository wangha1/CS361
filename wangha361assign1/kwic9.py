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
		return [];
	if(listPairs == True):
		listP = [];
		for item in list1:
			listP.append(item);
		Pairs = LP(listP);
	list2 = [];
	for i in range(len(list1)):
		line = [];
		line.append(list1[i]);
		words = [];
		words = line[0].split(" ");
		if(words.count("") != 0 ):
			words.remove("");
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
	newStr = oldStr.replace("\n"," ");
	num = newStr.count(".");
	index = 0
	for i in range(num):
		index = newStr.find(".",index);
		if(newStr[index - 1].islower() and newStr[index + 1].isspace()):
			newStr = newStr[:index+1] + '\n' + newStr[index+2:];
		index = index + 1;
	return newStr

def LP(lineLi):
	lineList = lineLi;
	words = [];
	pair = [];
	list_of_pairs = [];
	for i in range(len(lineList)):
		lineList[i] = lineList[i].lower();
		words.append(list(set(stripPunc(lineList[i].split(" ")))));
	for i in range(len(words)):
		if(words[i].count("") != 0):
			words[i].remove("");
		list_of_pairs = list_of_pairs + [[words[i][p1], words[i][p2]] for p1 in range(len(words[i])) for p2 in range(p1+1,len(words[i]))];
	for i in range(len(list_of_pairs)):
		list_of_pairs[i].sort();
	for i in range(len(list_of_pairs)):
		count = list_of_pairs.count(list_of_pairs[i]);
		if(count >= 2):
			temp = (tuple(list_of_pairs[i]),count);
			pair.append(temp);	
	pair = list(set(pair));
	pair = sorted(pair);
	return pair;
	
				

def stripPunc(wordList):
    puncList = [".",";",":","!","?","/","\\",",","#","@","$","&",")","(","\""]
    for punc in puncList:
        for word in wordList:
            wordList=[word.replace(punc,"") for word in wordList]
    return wordList

