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
	list2 = [];
	for i in range(len(list1)):
		line = [];
		line.append(list1[i]);
		words = [];
		words = line[0].split(" ");
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
