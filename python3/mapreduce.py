#!/usr/local/bin/python3
import os
from optparse import OptionParser
import inspect
import pprint
import threading

class GenericInputData(object):

    def __init__(self):
        self.__private_field = 'test_private_field'

    def read(self):
        raise NotImplementedError

    @classmethod
    def generate_inputs(cls, config):
        raise NotImplementedError


class PathInputData(GenericInputData):

    def __init__(self, path):
        super().__init__()
        self.path = path

    def read(self):
        return open(self.path).read()

    @classmethod
    def generate_inputs(cls, config):
        data_dir = config['data_dir']
        files = [file for file in os.listdir(data_dir) if file is not 'get-pip.py' and not file.endswith(".pyc")]
        print("Input Files: ", files)
        for filename in files:
            yield cls(os.path.join(data_dir, filename))


class GenericWorker(object):

    def __init__(self, input_data):
        self.input_data = input_data
        self.result = None

    def map(self):
        raise NotImplementedError

    def reduce(self, other):
        raise NotImplementedError

    @classmethod
    def create_workers(cls, input_class, config):
        workers = []
        for input_data in input_class.generate_inputs(config):
            workers.append(cls(input_data))
        return workers


class LineCountWorker(GenericWorker):

    def __init__(self, input_data):
        super().__init__(input_data)
        self.__private_field = 1

    def map(self):
        data = self.input_data.read()
        self.result = data.count('\n')

    def reduce(self, other):
        self.result += other.result


def execute(workers):
    threads = [threading.Thread(target=w.map) for w in workers]
    for t in threads: t.start()
    for t in threads: t.join()

    first, rest = workers[0], workers[1:]
    for other in rest:
        first.reduce(other)

    return first.result


def mapreduce(worker_class, input_class, config):
    workers = worker_class.create_workers(input_class, config)
    return execute(workers)

if __name__ == '__main__':
    print("Running mapreduce to count new lines in files under: %s" % os.getcwd())
    config = {'data_dir': os.getcwd()}
    result = mapreduce(LineCountWorker, PathInputData, config)
    print("Total lines are: %s" % result)
    print(LineCountWorker.__dict__)
