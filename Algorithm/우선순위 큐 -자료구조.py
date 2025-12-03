class PriorityQueue:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.array = [None] * capacity
        self.size = 0
        
    def isEmpty(self):
        return self.size == 0
    
    def isFull(self):
        return self.size == self.capacity
    
    def enqueue(self, e):
        if not self.isFull():
            self.array[self.size] = e       # 새로운 요소 배열의 맨 뒤에 추가
            self.size += 1
        
    # 배열에 저장된 값이 클수록 우선순위가 높다고 가정한 단순 우선순위 큐
    def findMaxindex(self):     # 우선순위가 가장 높은 요소의 인덱스 highest를 구해 반환
        if self.isEmpty():
            return -1
        
        highest = 0
        for i in range(1, self.size):       # 우선순위를 값 자체로 비교
            if self.array[i] > self.array[highest]:
                highest = i
        return highest
    
    
    def dequeue(self):
        highest = self.findMaxindex() 
        
        if highest != -1:
            self.size -= 1
            self.array[highest], self.array[self.size] = self.array[self.size], self.array[highest]
        
        return self.array[self.size]
    
    
    # 우선순위가 가장 높은 요소를 찾아 peek
    def peek(self): 
        highest = self.findMaxindex()
        if highest != -1:
            return self.array[highest]
        
    def __str__(self):
        return str(self.array[0:self.size])
    