import re

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def serialize(root, end="#"):
    val = [root.val]
    if root.left != None:
        val.extend(serialize(root.left))
    else:
        val.append(end)

    if root.right != None:
        val.extend(serialize(root.right))
    else:
        val.append(end)

    return val


def deserialize(source, end='#'):
    def helpMethod(index):
        if source[index] == end:
            return None, index + 1

        value = source[index]
        left, index = helpMethod(index + 1)
        right, index = helpMethod(index)
        return Node(value, left, right), index
    return helpMethod(0)[0]


node = Node('root', Node('left', Node('left.left')), Node('right'))
serializedString = serialize(node)
print(serializedString)

checkStr = deserialize(serialize(node)).left.left.val == 'left.left'
print(checkStr)