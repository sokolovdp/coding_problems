import itertools
import operator
import functools


def solution_1():
    t = [10, 15, 3, 7]
    k = 17

    for v1, v2 in itertools.combinations(t, 2):
        if (v1 + v2) == k:
            print(v1, v2)
            break


def solution_2():
    data = [1, 2, 3, 4, 5]
    output = []

    def calculate_prod(values: list) -> int:
        return functools.reduce(operator.mul, values, 1)

    for i in range(len(data)):
        product = data[0:i] + data[i+1:]
        output.append(calculate_prod(product))
    print(output)


def solution_3():

    class Node:
        def __init__(self, val, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right

    def traverse(tree: Node, log: list):
        if tree is not None:
            log.append(tree.val)
            traverse(tree.left, log)
            traverse(tree.right, log)

    def serialize(tree: Node) -> str:
        log = []
        traverse(tree, log)
        return '|'.join(log)

    def retraverse(node:Node, log: list) -> Node:
        pass

    def deserialize(node_str: str) -> Node:
        values = node_str.split('|')

        right = values[values.index('right'):]
        left = values[1:values.index('right')]
        print(left, right)
        return Node(1)

    node = Node('root', Node('left', Node('left.left')), Node('right'))

    result = serialize(node)
    deserialize(result)

    # assert deserialize(serialize(node)).left.left.val == 'left.left'


if __name__ == '__main__':
    # solution_1()
    # solution_2()
    solution_3()
