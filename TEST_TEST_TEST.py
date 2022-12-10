from multiprocessing import Process, Queue


class CustomProcess(Process):
    def __init__(self, q):
        Process.__init__(self)
        self.q = q
        self.otwet = 0

    def run(self):
        self.q.put([self.otwet, True])


if __name__ == '__main__':
    q1 = Queue()
    p = CustomProcess(q1)
    p.start()
    p.join()
    print(q1.get())
    print(q1.get()) # prints "[42, None, 'hello']"
