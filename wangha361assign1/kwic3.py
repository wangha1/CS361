def kwic(str1):
	list1 = str1.split("\n");
	if(str1 == ""):
		return [];
	list2 = [];
	for i in range(len(list1)):
		line = [];
		line.append(list1[i])
		words = [];
		words = line[0].split(" ");
		if(len(words) > 1):
			for x in range(len(words)):
				temp = [];
				if(x == len(words)):
					y = -1;
				else:
					y = x
				temp = shift(words,y);
				list2.append((temp,i));
		else:
			list2.append((words, i));

	list2.sort();
	return list2;

def shift(l,i):
	return l[i:] + l[:i]

