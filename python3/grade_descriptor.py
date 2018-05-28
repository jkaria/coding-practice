#!/usr/local/bin/python3
from weakref import WeakKeyDictionary

class Grade(object):

    def __init__(self):
        self._values = WeakKeyDictionary()

    def __get__(self, instance, instance_type):
        print("__get__: %r, %r" % (instance, instance_type))
        # print("Before: ", self.__dict__)
        if instance is None: return self
        return self._values.get(instance, 0)

    def __set__(self, instance, value):
        print("__set__: %r, %r" % (instance, value))
        if not (0 <= value <= 100):
            raise ValueError("Grade % must be between 0 and 100")
        print("Before: ", self._values)
        self._values[instance] = value
        print("After: ", self._values)


class Exam(object):
    # NOTE: these are class attributes!
    math = Grade()
    science = Grade()
    history = Grade()



if __name__ == "__main__":
    print("Testing 'Descriptors' concept for Grade class")
    exam1 = Exam()
    exam1.math = 99
    # NOTE: THIS IS ACCESSED AS
    # Exam.__dict__['math'].__set__(exam1, 99)
    # and when reading the attribute
    # Exam.__dict__['math'].__get__(exam1, Exam)
    exam1.science = 92
    exam1.history = 88
    print("Exam1 grades -> math: %d, science: %d, history: %d" % (exam1.math,
                                                                  exam1.science,
                                                                  exam1.history))
    print(exam1.__dict__)

    exam2 = Exam()
    exam2.math = 91
    exam2.science = 93
    exam2.history = 95
    print("Exam2 grades -> math: %d, science: %d, history: %d" % (exam2.math,
                                                                  exam2.science,
                                                                  exam2.history))
    print(exam2.__dict__)
    print(Exam.__dict__)
    print(Grade.__dict__)

    # assert exam1.math is not exam2.math

    exam1.history = 500
