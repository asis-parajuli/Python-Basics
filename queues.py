# FIFO = First IN - First Out
# if we use queues in a list of thousand item and when we remove the first item other 999 items should be shifted in the memory
# for that we need to use deque
from collections import deque
queue = deque([])
queue.append(1)
queue.append(2)
queue.append(3)
queue.popleft()
print(queue)
if not queue:
    print("empty")
