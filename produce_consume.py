'''_
@author: Curtis Yu
@contact: cuyu@splunk.com
@since: 2/24/16
'''
from collections import deque
import threading
import time

global Products, ConsumeQueue, ProductLock


class ThreadModel(threading.Thread):
    def __init__(self, name, role, interval):
        threading.Thread.__init__(self)
        self.name = name
        self.role = role
        self.interval = interval

    def run(self):
        global Products, ConsumeQueue
        if self.role == 'producer':
            while True:
                time.sleep(self.interval)
                Products += 1
                print '{0} have produced 1 product.'.format(self.name)
                print 'Totally have [{0}] products now.'.format(Products)
        elif self.role == 'consumer':
            while True:
                # 1. Must put acquire lock before the judgement!(otherwise the Products may be less than 0)
                ProductLock.acquire()
                if Products > 0:
                    if len(ConsumeQueue) > 0:
                        # Consume in a FIFO order if the queue is not empty
                        if ConsumeQueue[0] == self.name:
                            self.consume()
                            ConsumeQueue.popleft()
                        # 2. Make sure every branch of the if statement will release the lock!
                        ProductLock.release()
                    else:
                        self.consume()
                        ProductLock.release()
                        time.sleep(self.interval)
                else:
                    ProductLock.release()
                    ConsumeQueue.append(self.name)
                    # Sleep until have next demand
                    time.sleep(self.interval)

    def consume(self):
        global Products
        Products -= 1
        print '{0} have consumed 1 product.'.format(self.name)
        print 'Totally have [{0}] products now.'.format(Products)


if __name__ == "__main__":
    Products = 0
    ConsumeQueue = deque(maxlen=100)
    ProductLock = threading.Lock()
    producer_01 = ThreadModel('Producer_01', 'producer', 1)
    consumer_01 = ThreadModel('Consumer_01', 'consumer', 3)
    consumer_02 = ThreadModel('Consumer_02', 'consumer', 4)
    consumer_03 = ThreadModel('Consumer_03', 'consumer', 2)

    producer_01.start()
    consumer_01.start()
    consumer_02.start()
    consumer_03.start()
