import os

print(os.getcwd())
os.chdir(os.path.dirname(os.path.abspath(__file__)))
print(os.getcwd())

class Queue:
    def __init__(self):
        self.queue_data = []
    
    def insert_value(self, value):
        self.queue_data.append(value)
    
    def pop_value(self):
        if self.is_empty():
            print('You tried to delete value but the queue is empty!!!!!!!!!')
            return None
        return self.queue_data.pop(0)
    
    def is_empty(self):
        if len(self.queue_data) == 0:
            return True
        return False

# q = Queue()
size = 5
l = [1,2,3]

class QueueOutOfRangeException(Exception):
    pass

class SecondQueue(Queue):
    all_queues = {}

    def __init__(self, queue_name, queue_size):
        super().__init__()
        self.queue_name = queue_name
        self.queue_size = queue_size
        SecondQueue.all_queues[self.queue_name] = self

    def insert_value(self, value):
        if len(self.queue_data) >= self.queue_size:
            raise QueueOutOfRangeException(f"you tried to insert value but out of size queue")
        super().insert_value(value)
        
    # def __str__(self):
    #     return f"Queue Name: {self.queue_name}, Queue Size: {self.queue_size}, Queue Data: {self.queue_data}"
    
    def __repr__(self):
        return f"Queue Name: {self.queue_name}, Queue Size: {self.queue_size}, Queue Data: {self.queue_data}"
    

    @classmethod
    def save(cls):
        queue_file = open('queue.txt','w')
        queue_file.write(str(cls.all_queues))
        queue_file.close()

    @classmethod
    def load(cls):
        queue_file = open('queue.txt','r')
        if len(queue_file.readlines()) >= 1:
            print(queue_file.readlines())
            queue_file.close()
            return
        print('file not have data check if you saved or not')


q1 = SecondQueue('Restaurant1', 20)
q2 = SecondQueue('Restaurant2', 25)

print(SecondQueue.all_queues)

# SecondQueue.save()
print("------------\n\n")
SecondQueue.load()