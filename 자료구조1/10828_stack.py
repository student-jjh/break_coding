import sys


class stack:
	def __init__(self):
		self.stack=[]
	def push(self,number):
		self.stack.append(number)
	def pop(self):
		if self.stack==[]:
			return -1
		else:
			return self.stack.pop()
	def size(self):
		return len(self.stack)
	def empty(self):
		if self.stack==[]:
			return 1
		else:
			return 0
	def top(self):
		if self.stack==[]:
			return -1
		else:
			return self.stack[-1]

sentence_num=int(input(''))


s=stack()
for i in range(sentence_num):
	order=sys.stdin.readline().rstrip()
	orders=order.split(" ")
	if orders[0]=="push":
		s.push(int(orders[1]))
	elif orders[0]=="pop":
		print(s.pop())
	elif orders[0]=="size":
		print(s.size())
	elif orders[0]=="empty":
		print(s.empty())
	elif orders[0]=="top":
		print(s.top())  		