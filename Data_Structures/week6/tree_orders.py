import sys
import threading
sys.setrecursionlimit(10**6)  # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeOrders:
    def read(self):
        self.n = int(sys.stdin.readline())
        self.key = [0 for _ in range(self.n)]
        self.left = [0 for _ in range(self.n)]
        self.right = [0 for _ in range(self.n)]
        for i in range(self.n):
            a, b, c = map(int, sys.stdin.readline().split())
            self.key[i] = a
            self.left[i] = b
            self.right[i] = c

    def inOrder(self):
        self.result = []

        def inOrder_recursive(root):
            if root == -1:
                return
            inOrder_recursive(self.left[root])
            self.result.append(self.key[root])
            inOrder_recursive(self.right[root])

        inOrder_recursive(0)
        return self.result

    def preOrder(self):
        self.result = []

        def preOrder_recursive(root):
            if root == -1:
                return
            self.result.append(self.key[root])
            preOrder_recursive(self.left[root])
            preOrder_recursive(self.right[root])

        preOrder_recursive(0)
        return self.result

    def postOrder(self):
        self.result = []

        def postOrder_recursive(root):
            if root == -1:
                return
            postOrder_recursive(self.left[root])
            postOrder_recursive(self.right[root])
            self.result.append(self.key[root])

        postOrder_recursive(0)
        return self.result

def main():
    tree = TreeOrders()
    tree.read()
    print(" ".join(str(x) for x in tree.inOrder()))
    print(" ".join(str(x) for x in tree.preOrder()))
    print(" ".join(str(x) for x in tree.postOrder()))

threading.Thread(target=main).start()
