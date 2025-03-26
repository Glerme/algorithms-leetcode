from collections import deque


class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert_recursive(data, self.root)

    def _insert_recursive(self, data, node):
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert_recursive(data, node.left)

        else:
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert_recursive(data, node.right)

    def search(self, data):
        return self._search_recursive(self.root, data)

    def _search_recursive(self, node, data):
        if node is None:
            return False
        if node.data == data:
            return True
        elif data < node.data:
            return self._search_recursive(node.left, data)
        else:
            return self._search_recursive(node.right, data)

    def dfs(self, data):
        return self._dfs_recursive(self.root, data)

    def _dfs_recursive(self, node, data):
        if node:
            pass
        if node is None:
            return False
        if node.data == data:
            return True
        if self._dfs_recursive(node.left, data):
            return True
        if self._dfs_recursive(node.right, data):
            return True

    def pre_order_transversal(self):
        result = []

        self._pre_order_recursive(self.root, result)

        return result

    def _pre_order_recursive(self, node, result):
        if node:
            result.append(node.data)
            self._pre_order_recursive(node.left, result)
            self._pre_order_recursive(node.right, result)

    def in_order(self):
        result = []

        self._in_order_recursive(self.root, result)

        return result

    def _in_order_recursive(self, node, result):
        if node:
            self._in_order_recursive(node.left, result)
            result.append(node.data)
            self._in_order_recursive(node.right, result)

    def post_order(self):
        result = []

        self._post_order_recursive(self.root, result)

        return result

    def _post_order_recursive(self, node, result):
        if node:
            self._post_order_recursive(node.left, result)
            self._post_order_recursive(node.right, result)
            result.append(node.data)

    def bfs(self, data):
        if self.root is None:
            return False

        queue = deque()
        queue.append(self.root)

        while queue:
            node = queue.popleft()

            if node.data == data:
                return True

            if node.left:
                queue.append(node.left)

            if node.right:
                queue.append(node.right)

        return False


if __name__ == "__main__":
    bt = BinaryTree()

    bt.insert(5)
    bt.insert(3)
    bt.insert(1)
    bt.insert(10)
    bt.insert(7)
    bt.insert(15)
    bt.insert(20)

    print("pre order transversal: ", bt.pre_order_transversal())
    print("in order: ", bt.in_order())
    print("post order: ", bt.post_order())
    print("dfs: ", bt.dfs(20))
    print("bfs: ", bt.bfs(20))
