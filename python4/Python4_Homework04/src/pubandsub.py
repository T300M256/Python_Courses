"""
publish and subscribe "the observer pattern" implementation
"""

class Publisher:
    def __init__(self):
        self.subscribers = []
    def subscribe(self, subscriber):
        if subscriber in self.subscribers:
            raise ValueError("Multiple subscription are not allowed")
        self.subscribers.append(subscriber)
    def unsubscribe(self, subscriber1):
        if subscriber1 not in self.subscribers:
            raise ValueError("Can only unsubscribe subscribers")
        self.subscribers.remove(subscriber1)
        print("...successful unsub of", subscriber1)
    def publish(self, s):
        print("SUBS:", self.subscribers)
        for subscriber in self.subscribers:
            ## apparently this for loop is skipping
            ## some of the items in the list...when
            ## unsubscribed is invoked
            print("PUB TO", subscriber)
            subscriber(s)
            
if __name__ == '__main__':
    def multiplier(s):
        print(2*s)
    
    class SimpleSubscriber:
        def __init__(self, name, publisher):
            self.name = name
            self.publisher = publisher
            publisher.subscribe(self.process)
            self.pcount = 0
        def process(self,s):
            self.pcount += 1
            print(self.name, ":", s.upper(),"proc num",self.pcount)
            if self.pcount >= 3:
                # unsubscribe after three
                print("UNSUB", self.name)
                self.publisher.unsubscribe(self.process)
        def __repr__(self):
            return self.name
            
    publisher = Publisher()
    publisher.subscribe(multiplier)
    for i in range(6):
        newsub = SimpleSubscriber("Sub"+str(i),publisher)
        line = input("Input {}: ".format(i))
        publisher.publish(line)