class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def pre_order(node):
    if node is None:
        return []
    result = [node.data]
    result += pre_order(node.left)
    result += pre_order(node.right)
    return result

def in_order(node):
    if node is None:
        return []
    result = in_order(node.left)
    result.append(node.data)
    result += in_order(node.right)
    return result

def post_order(node):
    if node is None:
        return []
    result = post_order(node.left)
    result += post_order(node.right)
    result.append(node.data)
    return result
