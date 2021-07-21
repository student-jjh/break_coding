def ok_sequence(lists):
	count=1
	start=0
	for_answer=[]
	for_check=[]
	for_return=[]
	for j in range(len(lists),0,-1):
		for_check.append(j)
	while count<lists[0]:
		if start<lists[count]:
			while lists[count] not in for_answer:
				for_answer.append(for_check.pop())
				for_return.append('+')
			start=lists[count]
			for_answer.pop()
			for_return.append('-')
		else:
			if for_answer[-1]!=lists[count]:
				return "NO"
			else:
				for_answer.pop()
				for_return.append('-')
		count+=1
	for_return.append('-')
	return for_return	 
			 

number=int(input(''))
lista=[]
for i in range(number):
    k=int(input(""))
    lista.append(k)
if ok_sequence(lista)=='NO':
	print("No")
else:
	for i in ok_sequence(lista):
		print(i)
