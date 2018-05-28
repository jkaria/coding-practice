#!/usr/local/bin/python3

class Field(object):

    def __init__(self):
        self.name = None
        self.internal_name = None

    def __get__(self, instance, instance_type):
        if instance is None: return self
        # print("Accessing Field: {:s}".format(self.name))
        return getattr(instance, self.internal_name, '')

    def __set__(self, instance, value):
        # print("Setting Field: {:s}".format(self.name))
        setattr(instance, self.internal_name, value)


class MetaForClassAttributes(type):
    def __new__(meta, cls_name, bases, cls_dict):
        print("__new__: ", meta, cls_name, bases, cls_dict)
        for key, val in cls_dict.items():
            print("key: {k:<15}, val: {v}".format(k=key, v=val))
            if isinstance(val, Field):
                val.name = key
                val.internal_name = '_' + key
        return type.__new__(meta, cls_name, bases, cls_dict)


class DatabaseRecord(object, metaclass=MetaForClassAttributes):
    pass


class Customer(DatabaseRecord):
    first_name = Field()
    last_name  = Field()
    prefix     = Field()
    suffix     = Field()

if __name__ == '__main__':
    print("Testing Metaclass concept to Annotate Class Attributes!")
    customer = Customer()
    customer.first_name = 'Jaydeep'
    customer.last_name  = 'Karia'
    customer.prefix     = 'Mr.'

    print(customer.__dict__)
    print("{:<15}: {}".format('First Name', customer.first_name))
    print("{:<15}: {}".format('Last Name', customer.last_name))
    print("{:<15}: {}".format('Prefix', customer.prefix))
    print("{:<15}: {}".format('Suffix', customer.suffix))
    print("{:<15}: {:s}".format('Suffix(:s)', customer.suffix))
