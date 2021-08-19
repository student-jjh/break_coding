from collections import deque

N = int(input("N = "))
card = deque(range(1,N+1))
    
while len(card)>1:
    card.remove(card[0])
    c=card.popleft()
    card.append(c)

print(card[0])