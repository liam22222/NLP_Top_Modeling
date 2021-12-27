from collections import deque

q = deque()
q.append("ליאם")
q.append("אשכנזי")
q.append("גבר")
for item in q:
    print(item)

def transfer(Que):
    return ' '.join(Que)
