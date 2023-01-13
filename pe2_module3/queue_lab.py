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
    
que = Queue()
que.put(1)
que.put("dog")
que.put(False)
print(que.__dict__)
try:
    for i in range(4):
        print(que.get())
except:
    print("Queue error")