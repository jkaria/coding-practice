#!/usr/local/bin/python3
from queue import Queue
from threading import Thread
from time import time


def process(action, x):
    return "{}({})".format(action.title(), x)


def download(x):
    return process('dowload', x)


def resize(x):
    return process('resize', x)


def upload(x):
    return process('upload', x)


class ClosableQueue(Queue):
    EOQ = "END OF QUEUE"

    def close(self):
        # print(self.__dict__)
        # print(type(self))
        self.put(type(self).EOQ)

    def __iter__(self):
        while True:
            item = self.get()
            try:
                if item is self.EOQ: # NOTE: self.EOQ falls back to class variable if
                                     # no variable with same name is defined in __init__
                    return # no more items in queue
                yield item
            finally:
                self.task_done() # called for each item in queue (including EOQ)
                                 # only then queue.join() returns

class QueueWorker(Thread):
    def __init__(self, p_func, in_q, out_q):
        super().__init__()
        self.p_func = p_func
        self.in_q = in_q
        self.out_q = out_q

    def run(self):
        for item in self.in_q:
            res = self.p_func(item)
            self.out_q.put(res)


if __name__ == "__main__":
    print("Use Queues for work coordination between threads!")
    # print(ClosableQueue.__dict__)
    start = time()
    download_q = ClosableQueue()
    # print(download_q.__dict__)
    resize_q   = ClosableQueue()
    upload_q   = ClosableQueue()
    result_q   = ClosableQueue()

    threads = [
        QueueWorker(download, download_q, resize_q),
        QueueWorker(resize, resize_q, upload_q),
        QueueWorker(upload, upload_q, result_q)
    ]

    print("Starting queue worker threads")
    for t in threads:
        t.start()

    print("Enqueuing dowload work")
    for i in range(10):
        download_q.put("Image {:.1f}".format(i+1))
    print("Closing download_q")
    download_q.close()
    download_q.join()
    print("Closing resize_q")
    resize_q.close()
    resize_q.join()
    print("Closing upload_q")
    upload_q.close()
    upload_q.join()

    print("result_q qsize: {}".format(result_q.qsize()))
    print("Closing result_q")
    result_q.close()
    print("result_q qsize: {}".format(result_q.qsize()))
    for idx, res in enumerate(result_q, 1):
        print("{:<5d} {:s}".format(idx, res))
    result_q.join()
    end = time()
    print("Total elapsed time: {}".format(end-start))
