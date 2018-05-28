#!/usr/local/bin/python3
import pprint

class ToDictMixin(object):

    def to_dict(self):
        return self._traverse_dict(self.__dict__)

    def _traverse_dict(self, dict_instance):
        result = {}
        for key, val in dict_instance.items():
            result[key] = self._traverse(key, val)
        return result

    def _traverse(self, key, val):
        if isinstance(val, ToDictMixin):
            return val.to_dict()
        elif isinstance(val, dict):
            return self._traverse_dict(val)
        elif isinstance(val, list):
            return [self._traverse(key, i) for i in val]
        elif hasattr(val, '__dict__'):
            return val.to_dict()
        else:
            return val


class BinaryTree(ToDictMixin):

    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class BinaryTreeWithParent(BinaryTree):

    def __init__(self, value, left=None, right=None, parent=None):
        super().__init__(value, left=left, right=right)
        self.parent = parent

    def _traverse(self, key, val):
        if isinstance(val, BinaryTreeWithParent) and key == 'parent':
            return val.value # Prevent cycles
        else:
            return super()._traverse(key, val)


if __name__ == '__main__':
    print("Testing mixin concept using ToDictMixin applied to BinaryTreeWithParent")

    tree = BinaryTree(7, right=BinaryTree(6, left=BinaryTree(5, left=BinaryTree(4), right=BinaryTree(3))))

    print("BinaryTree serialized: ", tree.to_dict())

    parent_tree_root = BinaryTreeWithParent(7)
    parent_tree_root.right = BinaryTreeWithParent(6, parent=parent_tree_root)
    parent_tree_root.right.left = BinaryTreeWithParent(5, parent=parent_tree_root.right)

    print("BinaryTreeWithParent serialized: ", parent_tree_root.to_dict())
