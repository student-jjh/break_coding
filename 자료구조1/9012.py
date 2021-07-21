def parenthesis_string(strings):
	for_answer=[]
	for_return='YES'
	for i in strings:
		if i=='(':
			for_answer.append(i)
		elif i==')':
			if for_answer==[]:
				for_return='NO'
			else:
				for_answer.pop()
	if for_answer!=[]:
		for_return='NO'
	return for_return

for_num=int(input(""))
for i in range(for_num):
    strings=input("")
    print(parenthesis_string(strings))