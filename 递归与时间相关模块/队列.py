import collections

#创建一个队列
queue = collections.deque()
print(queue)
#入队列
queue.append("A")
print(queue)
queue.append("B")
print(queue)
queue.append("C")
print(queue)
queue.append("D")
print(queue)

#出队列
res1 = queue.popleft()
print(res1)
print(queue)