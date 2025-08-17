class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = 0
        self.rear = 0
        
    def is_empty(self):
        return self.front == self.rear
    
    def is_full(self):
        return self.front == (self.rear+1) % self.size
    
    def size(self):
        return (self.rear - self.front + self.size) % self.size
    
    def enqueue(self, item):
        if self.is_full():
            print("Queue is Full")
            return
        self.rear = (self.rear + 1) % self.size
        self.queue[self.rear] = item
        
    def dequeue(self):
        if self.is_empty():
            print("Queue is Empty")
            return None
        self.front = (self.front + 1) % self.size
        return self.queue[self.front]
    
    def display(self):
        if self.is_empty():
            print("Queue is Empty")
            return 
        
        i = (self.front + 1) % self.size
        elements = []       # 큐 내용을 저장할 임시 리스트
        while i != (self.rear + 1) % self.size:
            elements.append(self.queue[i])
            i = (i + 1) % self.size
        print("Queue:", elements)
        
q = CircularQueue(5) 