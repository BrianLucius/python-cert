class QueueError(IndexError):
    def __init__(self):
        print("QueueError: Can not get a value from an empty queue.")

class Queue:
    def __init__(self):
        self.__queue = []
    
    def put(self, elem):
        self.__queue.append(elem)
    
    def get(self):
        if len(self.__queue) > 0:
            val = self.__queue[0]
            del self.__queue[0]
            return val
        else:
            raise QueueError
    
class SuperQueue(Queue):
    def __init__(self):
        Queue.__init__(self)
        
    def isempty(self):
        if len(self._Queue__queue) == 0:
            return True
        else: 
            return False
    
que = SuperQueue()
que.put(1)
que.put("dog")
que.put(False)

for i in range(4):
    if not que.isempty():
        print(que.get())
    else:
        print("Queue Empty")
