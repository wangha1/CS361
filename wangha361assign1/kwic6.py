def kwic(str1, *arguments, **keywords):
	ignoreWords = [];
	listPairs = False;
	PeriodsToBreaks = False;	
	keys = sorted(keywords.keys());
	for kw in keys:
		if(kw == "ignoreWords"):
			ignoreWords = keywords[kw];
		elif(kw == "listPairs"):
			listPairs = keywords[kw];
		elif(kw == "periodsToBreaks"):
			periodsToBreaks = keywords[kw];
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
				if(temp[0] == ignoreWords[y]):
					flag = 1;
					break;
			if(flag == 0): 
				list2.append((temp,i));
	list2.sort(key = lambda s :" ".join(s[0]).lower());
	return list2;

def shift(l,i):
	return l[i:] + l[:i]
