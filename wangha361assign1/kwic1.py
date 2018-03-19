def kwic(str):
	list1 = str.split();
	if(list1 == []):
		return list1;
	list2 = [];
	for i in range(len(list1)):
		temp = [];
		temp.append(list1[i])
		list2.append((temp, i));
	return list2;

