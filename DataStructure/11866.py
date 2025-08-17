# 2. 원형 큐 직접 구현 
 
class Circlequeue():
    def __init__(self, n):
        self.n = n+1        # 원형 큐에서는 n=5 크기의 큐를 만들고 싶으면 n+1=6으로 설정
        self.queue = [None] * self.n
        self.start = 0
        self.rear = 0
        
    def is_full(self):
        return self.start == (self.rear + 1) % self.n
    
    def is_empty(self):
        return self.start == self.rear
    
    def enqueue(self, item):
        if self.is_full():
            return 
        self.rear = (self.rear + 1) % self.n
        self.queue[self.rear] = item
    
    def dequeue(self):
        if self.is_empty():
            return None
        self.start = (self.start + 1) % self.n
        return self.queue[self.start]    
    
    def __str__(self):
        return str(self.queue)   
    
n, k = map(int, input().split())
q = Circlequeue(n)

for i in range(1, n+1):
    q.enqueue(i)

result = []
while not q.is_empty():
    
    for i in range(k-1):
        q.enqueue(q.dequeue())      # dequeue의 반환값은 업데이트된 front 위치의 요소
    result.append(q.dequeue())

print("<"+', '.join(map(str, result))+">")