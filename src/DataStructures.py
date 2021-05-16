from sms import send

class Queue:

    def __init__(self, mode, current_queue=[]):
        self._queue = current_queue
        # depending on the _mode, the queue has to behave like a FIFO or LIFO
        if mode is None:
            raise "Please specify a queue mode FIFO or LIFO"
        else:
            self._mode = mode
    
    def enqueue(self, item):
        self._queue.append(item)
    def dequeue(self):
        if self._mode == 'LIFO':
            person = self._queue.pop(0)
        else:
            person = self._queue.pop()
        
        try:
            send(body=f"{person} it's your turn!")
            print("Message successfully sended")
        except Exception as error:
            print("Sending the message failed")
    def get_queue(self):
        return self._queue
    def size(self):
        return len(self._queue)
    def load_saved_queue(self, saved_queue):
        self._queue = [*saved_queue]
