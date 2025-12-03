'''
원형 큐에서는 pop연산을 사용하지 않는다. pop 연산을 사용하면 앞쪽 요소를 제거하면서 뒤에 있는 요소들을
모두 한칸씩 이동해야하므로 O(n)

원형 큐는 O(1)을 목표로 하기 때문에 front/rear 이동만으로 제거하는 방식을 사용한다.
이로써 실제 배열에는 남아있지만 큐 논리상 접근하지 않게된다.
'''

# 원형 큐
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
    
    def peek(self):
        if not self.is_empty():
            return self.queue[(self.front + 1) % self.size]
        else:
            pass
        
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
    
    
        


# 원형 덱
class CircularDeque(CircularQueue):
    def __init__(self, size=10):
        super().__init__(size)
    
    def addRear(self, item):
        self.enqueue(item)
    
    def deleteFront(self):
        return self.dequeue()
    
    def getFront(self):
        return self.peek()
    
    def addFront(self, item):
        if not self.is_full():
            self.queue[self.front] = item
            self.front = (self.front - 1 + self.size) % self.size
        else:
            pass
        
    def deleteRear(self):
        if not self.is_empty():
            item = self.queue[self.rear]
            self.rear = (self.rear -1 + self.size) % self.size
            return item
        else:
            pass
        
    def getRear(self):
        if not self.is_empty():
            return self.queue[self.rear]
        else:
            pass
        