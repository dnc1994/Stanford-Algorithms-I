import time
import heapq

low_heap = []
high_heap = []
count = 0
result = 0

with open('Median.txt', 'r') as f:
    for line in f:
        x = int(line.strip())
        if len(high_heap) == 0:
            heapq.heappush(high_heap, x)
        else:
            if x > high_heap[0]:
                heapq.heappush(high_heap, x)
            else:
                if len(low_heap) == 0:
                    heapq.heappush(low_heap, -x)
                else:
                    if x < -low_heap[0]:
                        heapq.heappush(low_heap, -x)
                    else:
                        heapq.heappush(high_heap, x)
        count += 1
        
        size_of_high_heap = 0
        if count % 2 == 0:
            size_of_high_heap = count / 2
            while len(high_heap) > size_of_high_heap:
                heapq.heappush(low_heap, -heapq.heappop(high_heap))
            while len(high_heap) < size_of_high_heap:
                heapq.heappush(high_heap, -heapq.heappop(low_heap))
            result += -low_heap[0]
        else:
            size_of_high_heap = count / 2 + 1
            while len(high_heap) > size_of_high_heap:
                heapq.heappush(low_heap, -heapq.heappop(high_heap))
            while len(high_heap) < size_of_high_heap:
                heapq.heappush(high_heap, -heapq.heappop(low_heap))               
            result += high_heap[0]
            
print(result % 10000)