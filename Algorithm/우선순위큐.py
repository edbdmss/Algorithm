# 1. heapq
import heapq

num1 = []

heapq.heappush(num1, 5)       # 새로운 원소 추가
heapq.heappop(num1)           # 최솟값 반환
heapq.heappushpop(num1, 10)   # 새 원소 추가 후 바로 최솟값 반환
heapq.heapreplace(num1, 15)   # 루트 값(최솟값) 제거 후 새 원소 추가




# 2. queue.PriorityQueue 
from queue import PriorityQueue

num2 = PriorityQueue()

num2.put(5)
num2.get()
num2.empty()    # True/False 반환
num2.full()     # True/Fasle 반환




# 3. 직접 클래스 구현 (최대값)
class MyselfPriorityQueue:
    
    def __init__(self):
        self.num3 = []
    
    def is_empty(self):
        return len(self.num3) == 0
    
    def push(self, x):
        self.num3.append(x)
        self._siftup(len(self.num3) - 1)
    
    def pop(self):
        if self.is_empty():
            return None
        self._swap(0, len(self.num3) - 1)
        max_item = self.num3.pop()
        self._siftdown(0)
        return max_item
    
    
    # ===== 내부 헬퍼 함수 =====
    def _siftup(self, index):           # 새로 삽입된 원소가 부모보다 크면 위로 교환
        parent = (index - 1) // 2
        if index > 0 and self.num3[index] > self.num3[parent]:
            self._swap(index, parent)
            self._siftup(parent)  # 재귀 호출
    
    
    def _siftdown(self, index):
        child = 2 * index + 1
        if child >= len(self.num3):
            return
        
        # 오른쪽 자식이 더 크면 선택
        if child + 1 < len(self.num3) and self.num3[child + 1] > self.num3[child]:
            child += 1
        if self.num3[child] > self.num3[index]:
            self._swap(child, index)
            self._siftdown(child)
        
        
    def _swap(self, i, j):
        self.num3[i], self.num3[j] = self.num3[j], self.num3[i]
        
        
    def peek(self):
        if self.is_empty():
            return None
        return self.num3[0]


queue = MyselfPriorityQueue()
queue.push(5)
queue.push(1)
queue.push(3)

queue.pop()




''' 
- 숫자만 넣는경우
숫자 하나만 넣어도 작은 값이 먼저 나오는 최소힙으로 동작한다. 이 경우, 숫자가 그 자체로 우선순위가 됨

- (우선순위, 데이터) 형태를 사용하는 경우
단순 숫자가 아니라 데이터와 우선순위를 함께 관리하고 싶을때

'''